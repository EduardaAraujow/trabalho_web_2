from app import db

class Controller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    resources = db.relationship("Resource", backref='controller', lazy=True)

    def __repr__(self):
        return '<Controller %r>' % self.name


    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "resources":self.resources
        }