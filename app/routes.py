from flask import Flask, request, jsonify
from app import app, db
from app.models import User, Like
from app.match_algorithm import MatchAlgorithm
import json


@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    new_user = User(
        name=data['name'],
        age=data['age'],
        height=data['height'],
        preferred_age_min=data['preferred_age_min'],
        preferred_age_max=data['preferred_age_max'],
        preferred_height_min=data['preferred_height_min'],
        preferred_height_max=data['preferred_height_max']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201


@app.route('/update_preferences/<int:user_id>', methods=['PUT'])
def update_user_preferences(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.json
    user.preferred_age_min = data.get('preferred_age_min', user.preferred_age_min)
    user.preferred_age_max = data.get('preferred_age_max', user.preferred_age_max)
    user.preferred_height_min = data.get('preferred_height_min', user.preferred_height_min)
    user.preferred_height_max = data.get('preferred_height_max', user.preferred_height_max)
    db.session.commit()
    return jsonify({'message': 'User preferences updated successfully'}), 200


@app.route('/potential_matches/<int:user_id>', methods=['GET'])
def get_potential_matches(user_id):
    potential_matches = MatchAlgorithm.find_potential_matches(user_id)
    matches = []
    for match in potential_matches:
        match_dict = {
            'id': match.id,
            'name': match.name,
            'age': match.age,
            'height': match.height
        }
        matches.append(match_dict)
    return jsonify(matches), 200


@app.route('/like/<int:user_id>/<int:liked_user_id>', methods=['POST'])
def like_user(user_id, liked_user_id):
    MatchAlgorithm.like_user(user_id, liked_user_id)
    if MatchAlgorithm.check_match(user_id, liked_user_id):
        return jsonify({'message': 'Match created!'}), 201
    return jsonify({'message': 'User liked'}), 201


@app.route('/unlike/<int:user_id>/<int:liked_user_id>', methods=['POST'])
def unlike_user(user_id, liked_user_id):
    MatchAlgorithm.unlike_user(user_id, liked_user_id)
    MatchAlgorithm.remove_match(user_id, liked_user_id)
    return jsonify({'message': 'User unliked'}), 200


if __name__ == '__main__':
    app.run(debug=True)