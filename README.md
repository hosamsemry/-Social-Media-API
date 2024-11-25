﻿# Social Media API
This is a Social Media API built using Django and Django Rest Framework (DRF). It provides core functionality for managing users, profiles, posts, comments, and the ability to follow/unfollow other users.
<br><br>
## Features

### User Management
- User Registration: Users can register with a username, email, and password.
- Authentication: Token-based authentication using dj-rest-auth.
- Profile Management: Each user has a profile with a bio, profile picture, and their posts.

### Posts
- Create, Update, and Delete Posts: Users can manage their own posts.
- View Posts: Publicly viewable posts with details like the author and post content.
- Comment on Posts: Add, view, and manage comments on posts.
- Comment Count: Display the number of comments on a post in the list view.

### Follow System
- Follow Users: Authenticated users can follow other users.
- Unfollow Users: Authenticated users can unfollow users they are already following.
- Check Follow Status: Check if a user is following another user.

### Search
- Search Profiles: Search for user profiles based on their username or name.
<br><br>
## Technologies Used
- Django: The core web framework used for backend development.
- Django Rest Framework (DRF): Facilitates the creation of RESTful APIs for communication between the frontend and backend.
- Python: The primary programming language used for backend logic implementation.
- PostgreSQL: An efficient relational database management system used for data storage.

## Future Enhancements
- Notifications: Notify users when they are followed or receive comments on their posts.
- Like System: Allow users to like posts and comments.
- Media Management: Add support for multimedia posts (images, videos, etc.).
- Analytics: Provide user engagement metrics such as the number of followers, post views, etc.
<br><br>
## Contributing
Contributions are welcomed! Please feel free to submit a Pull Request.


