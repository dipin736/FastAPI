from fastapi import FastAPI, HTTPException
from schemas import UserRegistration
from postgresdatabase import SessionLocal
from models import User,Profile


app = FastAPI()


@app.post('/register')
def register_user(user_registration: UserRegistration):
    db = SessionLocal()

    # Check if email already exists
    existing_user = db.query(User).filter_by(email=user_registration.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail='Email already exists.')

    # Check if phone already exists
    existing_user = db.query(User).filter_by(phone=user_registration.phone).first()
    if existing_user:
        raise HTTPException(status_code=400, detail='Phone already exists.')

    # Create user and profile entries
    user = User(
        first_name=user_registration.first_name,
        password=user_registration.password,
        email=user_registration.email,
        phone=user_registration.phone
    )
    profile = Profile(profile_picture=user_registration.profile_picture)
    user.profile = profile

    db.add(user)
    db.commit()

    return {'message': 'User registered successfully.'}

@app.get('/user/{user_id}')
def get_user(user_id: int):
    db = SessionLocal()

    # Retrieve user details and profile picture using user_id
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found.')

    user_details = {
        'id': user.id,
        'first_name': user.first_name,
        'password': user.password,
        'email': user.email,
        'phone': user.phone,
        'profile_picture': user.profile.profile_picture
    }
    return user_details