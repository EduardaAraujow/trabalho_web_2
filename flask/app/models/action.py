from app import db

class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    resources = db.relationship("Resource", backref='action', lazy=True)

    def __repr__(self):
        return '<Action %r>' % self.name


    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name
        }