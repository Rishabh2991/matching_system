# Matchmaking System.

Overview
Design and implement a simplified backend for a matchmaking system for a dating app. The system should efficiently match users based on their preferences. Focus on the backend architecture, data model design, and the algorithm that matches users. You are free to choose the python framework for this task. However, flask would be a bonus.

Requirements:

- User Profiles: Implement a system to manage user profiles. Each profile should include a user ID, name, age, height and preferred age, height range for matches. Feel free to add more attributes.

- Potential Matches: Design and implement an algorithm to find potential matches for a user. The match should be based on user preferences. Describe how your algorithm scales with a large number of users and how it ensures relevant matches.

API Design: Create APIs for the following actions
- Register a new user.
- Update user preferences.
- Fetch potential matches for a user.
- You are free to use any type of databases RDBMS, NoSQL etc. You can use a database for caching (Redis preferred).


High Level Design:

<img width="1113" alt="Screenshot 2024-04-25 at 1 21 25 PM" src="https://github.com/Rishabh2991/matching_system/assets/22934371/a8327da3-d30d-4f90-9ad2-f8e5f7564669">


Dependencies:

- Routes:
    - /register : New User registration
    - /update_preferences/<int:user_id> : API to update and set user preferences
    - /potential_matches/<int:user_id>: Get Potential matches
    - /like/<int:user_id>/<int:liked_user_id>: API to like a certain profile
    - /unlike/<int:user_id>/<int:liked_user_id>: API to dislike a certain profile
- Dependencies:
    - A postgres DB Store to save  : User, Preferences, Likes and Dislikes
    - A redis store to save potential matches and power /potential_matches to a user
- Services:
    -  Fetch potential matches from redis clusters
    -  Save profiles liked/unliked by a user
    -  Save matches based on liked profile history of users
    -  Unlike profiles
    -  Get Matched profiles for a user
