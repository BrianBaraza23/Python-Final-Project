# Python-Final-Project

# Movie Library Data Base - CLI

Date Created: 7 September 2023

## Description

The CLI application allows you to manage a simple database of Movies. The database includes
the movies Title, Actors, Category and rating. You can add delete, update and search for movies
using basic CLI commands.

## Author

Brian Baraza

## Technologies Used

- Python
- SQLAlchemy

## Installation

To use this application, you need to have the following prerequisites:

- Python 3.7+
- SQLAlchemy
- SQLite (for local development)


Follow these steps to set up the project:

1. Clone this repository to your local machine.
2. Install the required packages using pip:

   ```
   pip install SQLAlchemy 
   ```

3. Run the database migration to create the initial tables:

   ```
   python migrate.py
   ```

4. Use the `seeds.py` file to populate the database with sample data:

   ```
   python seeds.py

## Run the Commands
 
 To run the application:

 - Open the file using vs-code
 - Navigate to terminal in vs-code
 - Run "Pipenv shell" in the parent directory
 - "cd" to the app directory
 - Run the "Python cli.py" command 
 - enter the lised commands you wish to execute

## CLI Commands

 - A user is able to add a movie using "add-movie" command.
 - A user is able to delete a movie using the "delete-movie" command.
 - A user is able to rate a movie using the "rate-movie" command.
 - A user is able to search for a movie using the main actor's name via the "search-actor" command.
 - A user is able to search for a movie using the category name via the "search-category" command.
 - A user is able to search for a movie using the movie name via the "search-movie" command.


## License

This project is licensed under the MIT License.

## Contact Information

For any inquiries or assistance, please reach out to:

- Mobile: +254729812144
- Email: barazabrian87@gmail.com

Enjoy using the Movie Library System!
