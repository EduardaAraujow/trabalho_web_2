from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.email


    def to_dict(self):
        return jsonify ({
            "id":self.id,
            "email":self.email,
            "password":self.password
        })