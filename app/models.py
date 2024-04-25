from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    preferred_age_min = db.Column(db.Integer, nullable=False)
    preferred_age_max = db.Column(db.Integer, nullable=False)
    preferred_height_min = db.Column(db.Integer, nullable=False)
    preferred_height_max = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    liked_user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Like {self.user_id} likes {self.liked_user_id}>"


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, nullable=False)
    user2_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Match {self.user1_id} and {self.user2_id}>"