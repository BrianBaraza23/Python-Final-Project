import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Movie, Category 

# Create an SQLite engine 
engine = create_engine('sqlite:///movie_library.db')

# Creating a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--title', prompt='Enter the title of the movie')
@click.option('--actor', prompt='Enter the actor(s) of the movie')
@click.option('--category', prompt='Enter the category of the movie')
@click.option('--rating', prompt='Enter the rating of the movie')
def add_movie(title, actor, category, rating):
    try:
        # Querying the category by name
        category_object = session.query(Category).filter_by(name=category).first()

        if category_object is None:
            # Handle the case where the category doesn't exist
            click.echo(f"Category '{category}' does not exist. Please create it first.")
        else:
            # Create a new Movie instance and add it to the session
            new_movie = Movie(title=title, actor=actor, category=category_object, rating=float(rating))
            session.add(new_movie)

            # Commit the changes to the database
            session.commit()
            click.echo(f"Movie '{title}' added successfully!")

    except Exception as e:
        # Handling any exceptions that might occur during the process
        click.echo(f"An error occurred: {str(e)}")
    finally:
        # Close the session
        session.close()

@cli.command()
@click.option('--title', prompt='Enter the title of the movie to delete')
def delete_movie(title):
    try:
        # Query the movie by title
        movie_to_delete = session.query(Movie).filter_by(title=title).first()

        if movie_to_delete:
            # Delete the movie from the database
            session.delete(movie_to_delete)
            session.commit()
            click.echo(f"Movie '{title}' deleted successfully!")
        else:
            click.echo(f"Movie '{title}' not found in the database.")

    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        session.close()

@cli.command()
@click.option('--title', prompt='Enter the title of the movie to search')
def search_movie(title):
    try:
        # Query movies by title containing the entered title
        movies = session.query(Movie).filter(Movie.title.contains(title)).all()

        if movies:
            click.echo(f"Movies matching '{title}':")
            for movie in movies:
                click.echo(f"Title: {movie.title}, Actor(s): {movie.actor}, Category: {movie.category.name}, Rating: {movie.rating}")
        else:
            click.echo(f"No movies found with the title '{title}'.")

    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        session.close()

@cli.command()
@click.option('--category', prompt='Enter the category to search')
def search_category(category):
    try:
        # Query movies by category name
        movies = session.query(Movie).join(Category).filter(Category.name == category).all()

        if movies:
            click.echo(f"Movies in category '{category}':")
            for movie in movies:
                click.echo(f"Title: {movie.title}, Actor(s): {movie.actor}, Category: {movie.category.name}, Rating: {movie.rating}")
        else:
            click.echo(f"No movies found in category '{category}'.")

    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        session.close()

@cli.command()
@click.option('--actor', prompt='Enter the actor to search')
def search_actor(actor):
    try:
        # Query movies by actor name
        movies = session.query(Movie).filter(Movie.actor.contains(actor)).all()

        if movies:
            click.echo(f"Movies starring '{actor}':")
            for movie in movies:
                click.echo(f"Title: {movie.title}, Actor(s): {movie.actor}, Category: {movie.category.name}, Rating: {movie.rating}")
        else:
            click.echo(f"No movies found starring '{actor}'.")

    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        session.close()

@cli.command()
@click.option('--title', prompt='Enter the title of the movie to rate')
@click.option('--rating', prompt='Enter the new rating for the movie')
def rate_movie(title, rating):
    try:
        # Query the movie by title
        movie_to_rate = session.query(Movie).filter_by(title=title).first()

        if movie_to_rate:
            # Update the movie's rating
            movie_to_rate.rating = float(rating)
            session.commit()
            click.echo(f"Movie '{title}' rated successfully!")

        else:
            click.echo(f"Movie '{title}' not found in the database.")

    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        session.close()

# Add a welcome message and instructions
@click.command()
def welcome():
    click.echo("Welcome to Baraza movie store!")
    click.echo("Use our state-of-the-art CLI to manage your movie collection.")
    click.echo("Available commands:")
    click.echo("  add_movie: Add a new movie to the database")
    click.echo("  delete_movie: Delete a movie from the database")
    click.echo("  search_movie: Search for a movie by title")
    click.echo("  search_category: Search for movies by category")
    click.echo("  search_actor: Search for movies by actor")
    click.echo("  rate_movie: Rate a movie")
    click.echo("  help: Show this message and exit")

if __name__ == '__main__':
    cli.add_command(welcome)
    cli()
