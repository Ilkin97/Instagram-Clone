"""
markdown
# Instagram Clone

This is an Instagram Clone project built using Django for the backend and React for the frontend. The project replicates the basic functionality of Instagram, allowing users to create accounts, upload photos, follow other users, like posts, and comment on them.

## Features

- User authentication (sign up, login, logout)
- Create, update, and delete posts
- Like and comment on posts
- Follow and unfollow users
- View posts of users you follow
- Responsive design optimized for both desktop and mobile

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: React, Redux (for state management)
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Styling**: CSS, Bootstrap
- **Deployment**: Docker (for containerization)

## Installation

### Clone the repository

bash
git clone https://github.com/Ilkin97/instagram-clone.git


### Backend Setup (Django)

1. Navigate to the backend directory:

    bash
    cd backend
    

2. Create and activate a virtual environment:

    bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    

3. Install dependencies:

    bash
    pip install -r requirements.txt
    

4. Apply migrations:

    bash
    python manage.py migrate
    

5. Create a superuser for the admin panel:

    bash
    python manage.py createsuperuser
    

6. Run the backend server:

    bash
    python manage.py runserver
    

### Frontend Setup (React)

1. Navigate to the frontend directory:

    bash
    cd frontend
    

2. Install dependencies:

    bash
    npm install
    

3. Start the frontend development server:

    bash
    npm start
    

The React app will now be running on `http://localhost:3000`, and the Django API will be running on `http://localhost:8000`.

### Docker Setup (Optional)

If you prefer to use Docker, there is a `docker-compose.yml` file that sets up both the frontend and backend.

1. Build the Docker containers:

    bash
    docker-compose build
    

2. Run the Docker containers:

    bash
    docker-compose up
    

The app will be accessible on `http://localhost:8000` for the backend and `http://localhost:3000` for the frontend.

## Endpoints

- **POST** `/api/auth/signup/` - Sign up
- **POST** `/api/auth/login/` - Login
- **POST** `/api/posts/` - Create a post
- **GET** `/api/posts/` - List all posts
- **GET** `/api/posts/{id}/` - Get a specific post
- **PUT** `/api/posts/{id}/` - Update a post
- **DELETE** `/api/posts/{id}/` - Delete a post
- **POST** `/api/posts/{id}/like/` - Like a post
- **POST** `/api/posts/{id}/comment/` - Comment on a post

## Contributing

Feel free to fork the repository and submit pull requests. If you have any suggestions or issues, open an issue and we'll work on it together!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Django and React communities for their excellent frameworks and documentation.
- Special thanks to the contributors and maintainers of open-source libraries and tools that made this project possible.

"""