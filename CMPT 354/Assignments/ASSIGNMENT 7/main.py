import pyodbc
import datetime
import uuid

def connect_to_database():
    conn = pyodbc.connect(
                          'driver={ODBC Driver 18 for SQL Server};'
                          'server=cypress.csil.sfu.ca;'
                          'uid=s_rla122;'
                          'pwd=H367QQaTR4EAR4F6;'
                          'Encrypt=yes;'
                          'TrustServerCertificate=yes'
                          )
    return conn

def login(conn):
    while True:
        user_id = input("Enter your user ID: ")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_yelp WHERE user_id = ?", user_id)
        if cursor.fetchone():
            return user_id
        else:
            print("Invalid user ID. Please try again.")



def search_business(conn):
    min_stars = input("Enter minimum number of stars: ")
    city = input("Enter city: ")
    name = input("Enter part of the business name: ")

    cursor = conn.cursor()
    query = """SELECT * FROM business WHERE stars >= ? AND city LIKE ? AND name LIKE ?"""
    cursor.execute(query, min_stars, f'%{city}%', f'%{name}%')

    businesses = cursor.fetchall()
    if businesses:
        for business in businesses:
            print(business)
    else:
        print("No businesses found.")



def search_users(conn):
    name = input("Enter the user's name: ")
    min_review_count = input("Enter minimum review count: ")
    min_average_stars = input("Enter minimum average stars: ")

    cursor = conn.cursor()

    # SQL query for search
    query = """
            SELECT user_id, name, review_count, useful, funny, cool, average_stars, yelping_since
            FROM user_yelp
            WHERE name LIKE ? AND review_count >= ? AND average_stars >= ?
            ORDER BY name
            """

    # Execute query with given parameters
    cursor.execute(query, (f'%{name}%', min_review_count, min_average_stars))

    # Fetch & display results
    users = cursor.fetchall()
    if users:
        print("Search Results: ")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Review Count: {user[2]}, Useful: {user[3]}, Funny: {user[4]}, Cool: {user[5]}, Average Stars: {user[6]}, Yelping Since: {user[7]}")

    else:
        print("No users found matching the criteria.")

def add_friend(conn, user_id):
    friend_id = input("Enter the user ID of the friend: ")

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM user_yelp WHERE user_id = ?", friend_id)
    if cursor.fetchone()[0] == 0:
        print("Error: Friend user ID not found.")
        return

    cursor.execute("SELECT COUNT(*) FROM friendship WHERE user_id = ? AND friend = ?", user_id, friend_id)
    if cursor.fetchone()[0] > 0:
        print("You are already friends with this user.")
        return

    cursor.execute("INSERT INTO friendship (user_id, friend) VALUES (?, ?)", user_id, friend_id)
    conn.commit()
    print("Friend successfully added!")


def review_business(conn, user_id):
    business_id = input("Enter business ID: ")

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM business WHERE business_id = ?", business_id)
    if cursor.fetchone()[0] == 0:
        print("Error: Business ID not found.")
        return

    stars_input = input("Enter number of stars (1-5): ")

    if stars_input.isdigit():
        stars = int(stars_input)
        if 1 <= stars <= 5:
            cursor.execute("INSERT INTO review (review_id, user_id, business_id, stars, date) VALUES (?, ?, ?, ?, ?)", 
                           generate_review_id(), user_id, business_id, stars, datetime.datetime.now())
            conn.commit()
            print("Review sucessfully submitted!")
        else:
            print("Error: Number of stars must be between 1 and 5.")
    else:
        print("Invalid input. Please enter an integer between 1 and 5.")


def generate_review_id():
    return str(uuid.uuid4()).replace('-', '')[:20]


def main():
    conn = connect_to_database()

    user_id = login(conn)

    while True:
        print("\n1. Search Business\n2. Search Users\n3. Add Friend\n4. Review Business\n5. Exit\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            search_business(conn)
        elif choice == "2":
            search_users(conn)
        elif choice == "3":
            add_friend(conn, user_id)
        elif choice == "4":
            review_business(conn, user_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again from the options displayed above.")

    conn.close()

if __name__ == "__main__":
    main()