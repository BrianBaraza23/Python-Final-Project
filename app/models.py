# from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Table
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# # Define the association table for the many-to-many relationship between movies and actors
# movie_actors = Table(
#     'movie_actors',
#     Base.metadata,
#     Column('movie_id', Integer, ForeignKey('movies.id')),
#     Column('actor_id', Integer, ForeignKey('actors.id'))
# )

# class Movie(Base):
#     __tablename__ = 'movies'

#     id = Column(Integer, primary_key=True)
#     title = Column(String, nullable=False)
#     rating = Column(Float)
#     category_id = Column(Integer, ForeignKey('categories.id'))

#     category = relationship('Category', back_populates='movies')
#     actors = relationship('Actor', secondary=movie_actors, back_populates='movies')

# class Actor(Base):
#     __tablename__ = 'actors'

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)

#     movies = relationship('Movie', secondary=movie_actors, back_populates='actors')

# class Category(Base):
#     __tablename__ = 'categories'

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)

#     movies = relationship('Movie', back_populates='category')

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define the association table for the many-to-many relationship between movies and actors
movie_actors = Table(
    'movie_actors',
    Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    rating = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship('Category', back_populates='movies')
    actors = relationship('Actor', secondary=movie_actors, back_populates='movies')

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    movies = relationship('Movie', secondary=movie_actors, back_populates='actors')

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    movies = relationship('Movie', back_populates='category')

# Create the SQLite database and tables
engine = create_engine('sqlite:///movie_library.db')
Base.metadata.create_all(engine)



