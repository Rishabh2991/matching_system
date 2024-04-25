from app import db
from app.models import User, Like, Match


class MatchAlgorithm:
    @staticmethod
    def find_potential_matches(user_id):
        user = User.query.get(user_id)
        if not user:
            return []

        potential_matches = User.query.filter(
            User.id != user_id,
            User.age >= user.preferred_age_min,
            User.age <= user.preferred_age_max,
            User.height >= user.preferred_height_min,
            User.height <= user.preferred_height_max
        ).all()

        return potential_matches

    @staticmethod
    def create_match(user1_id, user2_id):
        match = Match(user1_id=user1_id, user2_id=user2_id)
        db.session.add(match)
        db.session.commit()

    @staticmethod
    def remove_match(user1_id, user2_id):
        match = Match.query.filter(
            (Match.user1_id == user1_id) & (Match.user2_id == user2_id) |
            (Match.user1_id == user2_id) & (Match.user2_id == user1_id)
        ).first()
        if match:
            db.session.delete(match)
            db.session.commit()

    @staticmethod
    def like_user(user_id, liked_user_id):
        like = Like(user_id=user_id, liked_user_id=liked_user_id)
        db.session.add(like)
        db.session.commit()

    @staticmethod
    def unlike_user(user_id, liked_user_id):
        like = Like.query.filter_by(user_id=user_id, liked_user_id=liked_user_id).first()
        if like:
            db.session.delete(like)
            db.session.commit()

    @staticmethod
    def check_match(user1_id, user2_id):
        match1 = Match.query.filter_by(user1_id=user1_id, user2_id=user2_id).first()
        match2 = Match.query.filter_by(user1_id=user2_id, user2_id=user1_id).first()
        return match1 and match2