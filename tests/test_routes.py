import unittest
from app import app
from unittest.mock import patch

class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_register_user(self):
        data = {
            'name': 'Test User',
            'age': 25,
            'height': 170,
            'preferred_age_min': 20,
            'preferred_age_max': 30,
            'preferred_height_min': 160,
            'preferred_height_max': 180
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 201)

    @patch('routes.MatchAlgorithm.find_potential_matches')
    def test_get_potential_matches(self, mock_find_potential_matches):
        # Mocking find_potential_matches to return a list of potential matches
        mock_find_potential_matches.return_value = [
            {'id': 1, 'name': 'Potential Match 1', 'age': 30, 'height': 175},
            {'id': 2, 'name': 'Potential Match 2', 'age': 28, 'height': 180}
        ]
        user_id = 1
        response = self.app.get(f'/potential_matches/{user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)

    @patch('routes.MatchAlgorithm.like_user')
    @patch('routes.MatchAlgorithm.check_match')
    def test_like_user(self, mock_check_match, mock_like_user):
        # Mocking check_match to return False (no match)
        mock_check_match.return_value = False
        user_id = 1
        liked_user_id = 2
        response = self.app.post(f'/like/{user_id}/{liked_user_id}')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'User liked')

    @patch('routes.MatchAlgorithm.unlike_user')
    @patch('routes.MatchAlgorithm.remove_match')
    def test_unlike_user(self, mock_remove_match, mock_unlike_user):
        user_id = 1
        liked_user_id = 2
        response = self.app.post(f'/unlike/{user_id}/{liked_user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'User unliked')

if __name__ == '__main__':
    unittest.main()