from app import db
from flask import jsonify
class Privilege(db.Model):
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey("resource.id"), primary_key=True)
    allow_boolean = db.Column(db.Boolean, nullable=False)
    
    def __repr__(self):
        return '<Privilege %r>' % self.allow_boolean


    def to_dict(self):
        return {
            "role":self.role.to_dict(),
            "resource_id":self.resource_id,
            "allow_boolean":self.allow_boolean
        }