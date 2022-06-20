from app import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    users = db.relationship("User", backref='role', lazy=True)
    privileges = db.relationship("Privilege", backref='role', lazy=True)

    def __repr__(self):
        return '<Role %r>' % self.name


    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name
        }