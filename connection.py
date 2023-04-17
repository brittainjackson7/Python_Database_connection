######
# Homework 4: Python + MySQL connection
# Students: Jackson Brittain, (jb3924)
######

# TODO 1 (4 points). Import the Mysql connector
import mysql.connector


# TODO 2 (4 points). Create a new class called Connection.
class Connection:


    # TODO 3. Create the __init__ function, that initialize a set of properties for the Connection function
    #    Important: make the properties private by using self.__ prefix for each of the variables
    #
    # Parameters: self
    #             host: the address of mysql server (default=localhost),
    #             user: the MySQL username that has permission to access the database (default=root),
    #             pwd: the password for the user (default=""),
    #             db: the name of the database (default="")
    # Additional property: also initialize a variable self.__mydb with None.
    #                      This variable will later store an open connection
    # Return: None
    # Grading: function header (4 points); processing (4 points)
    def __init__(self, host="localhost", user="root", pwd="", db=""):
        self.__host = host
        self.__user = user
        self.__pwd = pwd
        self.__db = db
        self.__mydb = None

    # TODO 4. Create th function open_con()
    # Process: the function opens a connection by calling the MySQL connector and
    #          stores the connection into the self.__mydb
    # Parameters: self
    # Return: None
    # Grading: function header (4 points); processing (4 points)
    def open_con(self):
        self.__mydb = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__pwd,
            database=self.__db
        )

    # TODO 5. Create the function get_con()
    # Process: the function returns the value of self.__mydb variable
    # Parameters: self
    # Return: self.__mydb
    # Grading: function header (4 points); processing (4 points)
    def get_con(self):
        return self.__mydb

    # TODO 6. Create the function close_con()
    # Process: the function closes the connection and set self.__mydb to None (empty connection)
    # Parameters: self
    # Return: None
    # Grading: function header (4 points); processing (4 points)
    def close_con(self):
        self.__mydb.close()
        self.__mydb = None

    # TODO 7. Create the function run_select()
    #    This function will perform SQL commands that return a table as a result
    # Process: opens a connection (by calling the appropriate function)
    #          creates a cursor for the connection
    #          executes the sql with the values provided as parameters
    #          fetch the results into a list variable
    #          close the connection
    #          return the resulting list
    # Parameters: sql: string that corresponds to the SQL command to be executed
    #             values: tuple with the values to be used when the sql has %s for input values (default=None)
    # Return: result: list of tuples fetched from the cursor
    # Grading: function header (4 points); processing (4 points)
    def run_select(self, sql, values=None):
        self.open_con()
        cursor = self.__mydb.cursor()

        if values is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, values)

        result = cursor.fetchall()
        self.close_con()
        return result


    # TODO 8. Create the function run_change()
    #    This function will perform SQL commands that must be committed (insert/update/delete)
    # Process: opens a connection (by calling the appropriate function)
    #          creates a cursor for the connection
    #          executes the sql with the values provided as parameters
    #          commits the changes
    #          stores the number of affected rows into a result variable
    #          close the connection
    #          return the result
    # Parameters: sql: string that corresponds to the SQL command to be executed
    #             values: tuple with the values to be used when the sql has %s for input values (default=None)
    # Return: result: the number of rows affected by the SQL command
    # Grading: function header (4 points); processing (4 points)
    def run_change(self, sql, values=None):
        self.open_con()
        cursor = self.__mydb.cursor()

        if values is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, values)

        self.__mydb.commit()
        result = cursor.rowcount
        self.close_con()
        return result
