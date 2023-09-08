import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from faker import Faker
from sqlalchemy.orm import sessionmaker
from models import Movie, Actor, Category, Base
from database import engine, init_db

def generate_dummy_data(session):
    fake = Faker()

    # Create categories
    categories = [Category(name=fake.word()) for _ in range(5)]
    session.add_all(categories)
    session.commit()

    # Create actors
    actors = [Actor(name=fake.name()) for _ in range(20)]
    session.add_all(actors)
    session.commit()

    # Create movies
    for _ in range(20):
        title = fake.catch_phrase()
        category = fake.random_element(categories)
        actor = fake.random_element(actors)
        rating = fake.random_int(1, 10)
        
        movie = Movie(title=title, category=category, actor=actor, rating=rating)
        session.add(movie)

    session.commit()

if __name__ == '__main__':
    init_db()  # Initialize the database
    Session = sessionmaker(bind=engine)
    session = Session()

    generate_dummy_data(session)
    session.close()
