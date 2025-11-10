from flask import Blueprint, request, jsonify
from models import db, Customer, Reservation, NewsletterSubscriber
import random
from datetime import datetime

bp = Blueprint('bp', __name__)

@bp.route("/api/reservations", methods=["POST"])
def make_reservation():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        guests = int(data.get("guests"))
        time_slot = data.get("time_slot")

        # Validate required fields
        if not name or not email or not time_slot:
            return jsonify({"error": "Missing required fields"}), 400

        # Convert to datetime
        try:
            time_slot_dt = datetime.fromisoformat(time_slot)
        except ValueError:
            return jsonify({"error": "Invalid date format"}), 400

        # Check if time slot is full (max 30 tables)
        existing_count = Reservation.query.filter_by(time_slot=time_slot_dt).count()
        if existing_count >= 30:
            return jsonify({"error": "Time slot fully booked"}), 409

        # Check or create customer
        customer = Customer.query.filter_by(email=email).first()
        if not customer:
            customer = Customer(name=name, email=email, phone=phone)
            db.session.add(customer)
            db.session.commit()

        # Assign random available table
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

        return jsonify({
            "message": "Reservation successful!",
            "table_number": table_number,
            "time_slot": time_slot
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@bp.route("/api/newsletter", methods=["POST"])
def subscribe_newsletter():
    try:
        data = request.get_json()
        email = data.get("email")

        if not email:
            return jsonify({"error": "Email is required"}), 400

        # Check if already subscribed
        subscriber = NewsletterSubscriber.query.filter_by(email=email).first()
        if subscriber:
            return jsonify({"error": "Email already subscribed"}), 409

        # Save to database
        new_subscriber = NewsletterSubscriber(email=email)
        db.session.add(new_subscriber)
        db.session.commit()

        return jsonify({"message": "Subscription successful!"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
