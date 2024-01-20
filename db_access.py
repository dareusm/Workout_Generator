import sqlite3


# Adding users to database
def add_user(firstName, lastName):
    conn = sqlite3.connect("Users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (NULL, ?, ?)", (firstName, lastName))
    conn.commit()
    conn.close()


# User login
def login(firstName, lastName):
    conn = sqlite3.connect("Users.db")
    c = conn.cursor()

    # Fetch the user with the given firstname
    c.execute("SELECT * FROM Users where first_name = ?", (firstName,))
    name = c.fetchone()
    conn.close()

    # Check if user exists in database and that their last name matches
    if name is not None and name[2] == lastName:
        return True
    else:
        return False
