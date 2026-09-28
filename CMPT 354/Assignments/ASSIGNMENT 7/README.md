# Yelp Database Application README

## Overview
This Yelp Database Application provides a user-friendly command-line interface to interact with the Yelp database. Users can log in, search for businesses and other users, create friendships, and review businesses. The application is built with Python and uses `pyodbc` for database connectivity.

## Prerequisites
- Python 3.x.x installed on your system.
- `pyodbc` library installed. You can install it using `pip3 install pyodbc`.
- Access to the Yelp database with proper configurations.

## Installation
1. Clone or download the application from the repository.
2. Navigate to the application's directory.
3. Ensure that your database connection details are correctly set in the `app.py` file.

## Running the Application
Open a terminal or command prompt, navigate to the application's directory, and run the application using Python:

```bash
python3 main.py
```

## Usage

### Logging In
1. When you start the application, you will be prompted to log in using your user ID.
2. Enter a valid user ID to access the application's features.

### Searching for Businesses
1. Enter the search business option (1) to search for businesses.
2. Enter the criteria for your search, such as minimum stars, city, and business name.

### Searching for Users
1. Select the search users option (2) from the main menu.
2. Provide details like part of the user's name, minimum review count, and minimum average stars.

### Making Friends
1. Enter the add friend option (3) to make a friend.
2. Enter the user ID of the friend you want to add.

### Reviewing a Business
1. Enter the review business option (4) to review a business.
2. Enter the business ID and your star rating for the review.

### Exiting the Application
- To exit the application, select the exit option (5) from the main menu.
- At any point in time, users can <CTRL+C> to terminate the program.