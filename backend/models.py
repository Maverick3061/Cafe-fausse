from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    newsletter = db.Column(db.Boolean, default=False)

    reservations = db.relationship("Reservation", backref="customer", lazy=True)


class Reservation(db.Model):
    __tablename__ = "reservations"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    time_slot = db.Column(db.DateTime, nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    table_number = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "customer_id": self.customer_id,
            "time_slot": self.time_slot.isoformat() if self.time_slot else None,
            "guests": self.guests,
            "table_number": self.table_number,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "customer": {
                "id": self.customer.id,
                "name": self.customer.name,
                "email": self.customer.email,
                "phone": self.customer.phone
            } if self.customer else None
        }


class NewsletterSubscriber(db.Model):
    __tablename__ = "newsletter_subscribers"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {"id": self.id, "email": self.email, "created_at": self.created_at.isoformat() if self.created_at else None}
