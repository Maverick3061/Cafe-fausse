from flask import Blueprint, request, jsonify, current_app
from models import db, Customer, Reservation, NewsletterSubscriber
import random
from datetime import datetime
from flask_mail import Message

bp = Blueprint('bp', __name__)

# Sample static menu (can move to DB later)
SAMPLE_MENU = {
    "starters": [
        {"name": "Bruschetta", "desc": "Tomato, basil, olive oil", "price": 8.5},
        {"name": "Garlic Bread", "desc": "Toasted baguette with garlic butter", "price": 6.0}
    ],
    "mains": [
        {"name": "Grilled Salmon", "desc": "With lemon butter and veg", "price": 22.0},
        {"name": "Ribeye Steak", "desc": "12 oz with mashed potatoes", "price": 28.0}
    ],
    "desserts": [
        {"name": "Tiramisu", "price": 7.5},
        {"name": "Cheesecake", "price": 7.0}
    ],
    "beverages": [
        {"name": "Espresso", "price": 3.0},
        {"name": "Red Wine (glass)", "price": 10.0}
    ]
}

# ------------------------------
# Menu route
# ------------------------------
@bp.route("/menu", methods=["GET"])
def get_menu():
    return jsonify(SAMPLE_MENU), 200


# ------------------------------
# Reservations route
# ------------------------------
bp = Blueprint('bp', __name__)

@bp.route("/reservations", methods=["POST", "GET"])
def handle_reservations():
    if request.method == "POST":
        try:
            data = request.get_json() or {}
            if not data:
                return jsonify({"error": "No JSON data sent"}), 400

            name = data.get("name")
            email = data.get("email")
            phone = data.get("phone")
            guests = int(data.get("guests", 1))
            time_slot = data.get("time_slot")

            if not (name and email and time_slot):
                return jsonify({"error": "Missing required fields"}), 400

            # parse ISO time string
            try:
                time_slot_dt = datetime.fromisoformat(time_slot)
            except Exception:
                return jsonify({"error": "Invalid time_slot format; use ISO 8601"}), 400

            # Find or create customer
            customer = Customer.query.filter_by(email=email).first()
            if not customer:
                customer = Customer(name=name, email=email, phone=phone)
                db.session.add(customer)
                db.session.commit()

            # Max 30 tables per time slot
            existing_count = Reservation.query.filter_by(time_slot=time_slot_dt).count()
            if existing_count >= 30:
                return jsonify({"error": "Time slot fully booked"}), 409

            # Assign table
            taken_tables = [r.table_number for r in Reservation.query.filter_by(time_slot=time_slot_dt).all()]
            available_tables = [t for t in range(1, 31) if t not in taken_tables]
            table_number = random.choice(available_tables)

            # Save reservation
            reservation = Reservation(
                customer_id=customer.id,
                time_slot=time_slot_dt,
                guests=guests,
                table_number=table_number
            )
            db.session.add(reservation)
            db.session.commit()

            # Send confirmation email (optional)
            try:
                msg = Message(
                    subject="Café Fausse Reservation Confirmation",
                    sender=current_app.config.get("MAIL_USERNAME"),
                    recipients=[customer.email],
                    body=(
                        f"Dear {customer.name},\n\n"
                        f"Your reservation is confirmed.\n"
                        f"Date & Time: {reservation.time_slot.strftime('%A, %B %d, %Y %I:%M %p')}\n"
                        f"Table Number: {reservation.table_number}\n"
                        f"Guests: {reservation.guests}\n\n"
                        "Café Fausse\n1234 Culinary Ave\n"
                    )
                )
                mail = getattr(current_app, "mail", None)
                if mail:
                    mail.send(msg)
            except Exception as exc:
                current_app.logger.warning(f"Email send failed: {exc}")

            return jsonify({
                "message": "Reservation successful!",
                "table_number": table_number,
                "time_slot": reservation.time_slot.isoformat()
            }), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    # GET -> list reservations
    reservations = Reservation.query.order_by(Reservation.time_slot.desc()).limit(100).all()
    return jsonify([r.to_dict() for r in reservations]), 200

# ------------------------------
# Newsletter subscription
# ------------------------------
@bp.route("/newsletter", methods=["POST"])
def subscribe_newsletter():
    try:
        data = request.get_json() or {}
        email = data.get("email")
        if not email:
            return jsonify({"error": "Email is required"}), 400

        subscriber = NewsletterSubscriber.query.filter_by(email=email).first()
        if subscriber:
            return jsonify({"error": "Email already subscribed"}), 409

        new_subscriber = NewsletterSubscriber(email=email)
        db.session.add(new_subscriber)
        db.session.commit()
        return jsonify({"message": "Subscription successful!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
