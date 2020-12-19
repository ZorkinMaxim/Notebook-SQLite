import sqlite3


def get_connection():
    con = sqlite3.connect("notebook.sqlite3")
    con.execute("""
        CREATE TABLE IF NOT EXISTS data
        (name TEXT, phone TEXT, age INTEGER)
    """)
    return con


def insert_data(connection, name, phone, age):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO data VALUES (?, ?, ?)", (name, phone, age))
    connection.commit()
    print("The data added successfully!")


def show_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM data")
    for el in cursor.fetchall():
        print(*el)


def delete_by_name(connection, name):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM data WHERE name = ?", (name,))
    connection.commit()
    print("The data deleted successfully!")


def update_data(connection, name, phone, age):
    cursor = connection.cursor()
    cursor.execute("UPDATE data SET phone = ?, age = ? WHERE name = ?", (phone, age, name))
    connection.commit()
    print("The data updated succssfully!")


if __name__ == "__main__":
    print("Welcome to the notebook!")

    action = None

    while action != 'exit':
        con = get_connection()
        action = input("Choose an action [add, read, delete, update]\n")
        if action == 'add':
            try:
                name, phone, age = input("Enter the data (name phone age): ").split(" ")
            except ValueError:
                print("Entered data is wrong")
            else:
                insert_data(con, name, phone, age)
        elif action == 'read':
            show_data(con)
        elif action == 'delete':
            name_to_delete = input("Enter the name of the contact to delete: ")
            delete_by_name(con, name_to_delete)
        elif action == 'update':
            name_to_update = input("Enter the name of the contact to update: ")
            update_phone = input("Enter a new value to the parameter phone: ")
            update_age = int(input("Enter a new value to the parameter age: "))
            update_data(con, name_to_update,update_phone, update_age)
        else:
            con.close()
            print("Bye, bye")
            exit(0)
