from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo

def update_blob(author_id, filename):
    # read file
    data = read_file(filename)

    # prepare update query and data
    query = "UPDATE authors " \
            "SET photo = %s " \
            "WHERE id  = %s"

    args = (data, author_id)

    db_config = read_db_config()

    try:
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
def main():
    update_blob(144, "pictures\pic.jpg")

if __name__ == '__main__':
    main()

def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
def read_blob(author_id, filename):
    # select photo column of a specific author
    query = "SELECT photo FROM authors WHERE id = %s"

    # read database configuration
    db_config = read_db_config()

    try:
        # query blob data form the authors table
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, (author_id,))
        photo = cursor.fetchone()[0]

        # write blob data into a file
        write_file(photo, filename)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
def main():
    read_blob(144,"output\garth_stein.jpg")

if __name__ == '__main__':
    main()