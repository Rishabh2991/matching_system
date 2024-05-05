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
    - /register : New User registration:

      <img width="1134" alt="Screenshot 2024-05-05 at 5 54 31 PM" src="https://github.com/Rishabh2991/matching_system/assets/22934371/40c2faa8-3f46-478c-9547-b35e79efc950">

    - /update_preferences/<int:user_id> : API to update and set user preferences
      
      <img width="1139" alt="Screenshot 2024-05-05 at 5 55 29 PM" src="https://github.com/Rishabh2991/matching_system/assets/22934371/76c17be7-1ee0-43f1-bc34-9362704c333a">


    - /potential_matches/<int:user_id>: Get Potential matches
      <img width="1132" alt="Screenshot 2024-05-05 at 5 56 07 PM" src="https://github.com/Rishabh2991/matching_system/assets/22934371/5bd0f810-e0fc-47ed-846d-57cb75432965">

        
    - /like/<int:user_id>/<int:liked_user_id>: API to like a certain profile
      <img width="1125" alt="Screenshot 2024-05-05 at 5 56 33 PM" src="https://github.com/Rishabh2991/matching_system/assets/22934371/05b6b4b5-10ee-47c5-9558-3150a98dc774">

      
    - /unlike/<int:user_id>/<int:liked_user_id>: API to dislike a certain profile

      <img width="1135" alt="Screenshot 2024-05-05 at 5 56 51 PM" src="https://github.com/Rishabh2991/matching_system/assets/22934371/037545bd-4661-4e31-adeb-dc1195f593dd">

- Dependencies:
    - A postgres DB Store to save  : User, Preferences, Likes and Dislikes

      ![Screenshot 2024-05-05 at 6 24 48 PM](https://github.com/Rishabh2991/matching_system/assets/22934371/980fbfbd-fc3a-4cf8-9be4-9005365b7ac9)

      
    - A redis store to save potential matches and power /potential_matches to a user
- Services:
    -  Fetch potential matches from redis clusters
    -  Save profiles liked/unliked by a user
    -  Save matches based on liked profile history of users
    -  Unlike profiles
    -  Get Matched profiles for a user
