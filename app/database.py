from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database
DATABASE_URL = "sqlite:///./fitbuddy.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# User table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), unique=True, index=True, nullable=False)
    username = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    weight = Column(String(20), nullable=False)
    goal = Column(String(100), nullable=False)
    intensity = Column(String(50), nullable=False)

    original_plan = Column(Text, nullable=True)
    updated_plan = Column(Text, nullable=True)
    nutrition_tip = Column(Text, nullable=True)
    feedback = Column(Text, nullable=True)


# Create database tables
Base.metadata.create_all(bind=engine)


# Get database session
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# Save a new user and workout plan
def save_user(
    db,
    user_id,
    username,
    age,
    weight,
    goal,
    intensity,
    original_plan,
    nutrition_tip
):
    user = User(
        user_id=user_id,
        username=username,
        age=age,
        weight=str(weight),
        goal=goal,
        intensity=intensity,
        original_plan=original_plan,
        nutrition_tip=nutrition_tip
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# Update user's workout plan after feedback
def update_plan(db, user_id, updated_plan, feedback):
    user = db.query(User).filter(User.user_id == user_id).first()

    if user:
        user.updated_plan = updated_plan
        user.feedback = feedback

        db.commit()
        db.refresh(user)

    return user


# Get original workout plan
def get_original_plan(db, user_id):
    user = db.query(User).filter(User.user_id == user_id).first()

    if user:
        return user.original_plan

    return None


# Get a user
def get_user(db, user_id):
    return db.query(User).filter(User.user_id == user_id).first()


# Get all users
def get_all_users(db):
    return db.query(User).all()


# Get all workout plans
def get_all_plans(db):
    return db.query(User).all()