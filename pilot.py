######
# Homework 4: Python + MySQL connection
# Students: <student name>, (<student id>)
#           <student name>, (<student id>)
######

# TODO 1 (4 points). Import your Connection class (from the connection_solution.py file)
from connection import Connection


# The Pilot class is created for you. The __init__ function will initialize the class properties and
# there are get_ and set_ functions for each of the properties. You will complete the class with the
# methodos to save and load data to/from the database based on the primary key (pilot.identification)
class Pilot:

    # __init__()
    # Parameters: self
    #             id: integer that represents the pilot's identification number (primary key, default=0)
    #             name: string that represents the pilot's name (default=""),
    #             salary: decimal that represents the pilot's salary (default=0.0)
    #             bonus: decimal that represents the pilot's gratification (default=0.0)
    #             airline: string that represents the airline company to which the pilot is affiliated
    #                      (default="")
    #             country: string that represents the country of resident. The country indicates where
    #                      the pilot is based (may not be their country of birth, default="")
    # Return: None
    def __init__(self, id=0, name="", salary=0.0, bonus=0.0, airline="", country=""):
        self.__id = id
        self.__name = name
        self.__salary = salary
        self.__bonus = bonus
        self.__airline = airline
        self.__country = country

    # __str__()
    # Prints the object Pilot in a nicely formatted string
    # Parameters: self
    # Return: a string in the format "Pilot <identification>: <name>"
    def __str__(self):
        return "Pilot " + str(self.get_id()) + ": " \
               + self.get_name()

    # set_id()
    # Process: sets the pilot's identification to the value in the parameter
    # Parameters: self
    #             id: the new identification number
    # Return: None
    def set_id(self, id):
        self.__id = id

    # set_name()
    # Process: sets the pilot's name to the value in the parameter
    # Parameters: self
    #             name: the new name
    # Return: None
    def set_name(self, name):
        self.__name = name

    # set_salary()
    # Process: sets the pilot's salary to the value in the parameter
    # Parameters: self
    #             salary: the new salary (as float)
    # Return: None
    def set_salary(self, salary):
        self.__salary = float(salary)

    # set_bonus()
    # Process: sets the pilot's bonus to the value in the parameter
    # Parameters: self
    #             bonus: the new bonus (as float)
    # Return: None
    def set_bonus(self, bonus):
        self.__bonus = float(bonus)

    # set_airline()
    # Process: sets the pilot's affiliation to the value in the parameter
    # Parameters: self
    #             airline: the new airline
    # Return: None
    def set_airline(self, airline):
        self.__airline = airline

    # set_country()
    # Process: sets the pilot's country to the value in the parameter
    # Parameters: self
    #             country: the new country or residence
    # Return: None
    def set_country(self, country):
        self.__country = country

    # get_id()
    # Process: returns the pilot's identification number
    # Parameters: self
    # Return: self.__id
    def get_id(self):
        return self.__id

    # get_name()
    # Process: returns the pilot's name
    # Parameters: self
    # Return: self.__name
    def get_name(self):
        return self.__name

    # get_salary()
    # Process: returns the pilot's salary
    # Parameters: self
    # Return: self.__salary
    def get_salary(self):
        return self.__salary

    # get_bonus()
    # Process: returns the pilot's gratification
    # Parameters: self
    # Return: self.__bonus
    def get_bonus(self):
        return self.__bonus

    # get_airline()
    # Process: returns the pilot's affiliation
    # Parameters: self
    # Return: self.__airline
    def get_airline(self):
        return self.__airline

    # get_country()
    # Process: returns the pilot's country
    # Parameters: self
    # Return: self.__country
    def get_country(self):
        return self.__country

    # TODO 2. Create the function save()
    # Process: - creates a Connection object (the class we created in file connection_solution.py)
    #          - initialize the Connection with the username and password received as parameters
    #          - initialize the db variable to be the "airline_db" database
    #          - check if the pilot's identification number exists in the table airline_db.Pilot
    #          - if the identification number does NOT exist, use the appropriate function from
    #                   Connection to insert*** the pilot as a new tuple in the Pilot table;
    #          - otherwise, use the appropriate function from Connection to update*** the existing
    #                   tuple with the current values for this Pilot.
    #          *** Note: always insert/update all the Pilot's attributes.
    # Parameters: self
    #             user: the MySQL username that has permission to access the database
    #             pwd: the password for the user
    # Return: True if the data successfully affected one row in the Pilot table (insert or update);
    #         False, otherwise
    # Grading: function header (4 points); update (4 points); insert (4 points); return (4 points)
    def save(self, user, pwd):
        connection = Connection(user=user, pwd=pwd, db="airline_db")
        pilot_exists_query = "SELECT * FROM Pilot WHERE identification = %s"
        result = connection.run_select(pilot_exists_query, (self.__id,))

        if len(result) == 0:
            insert_query = "INSERT INTO Pilot (identification, pilot_name, salary, gratification, airline, country) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (self.__id, self.__name, self.__salary, self.__bonus, self.__airline, self.__country)
            affected_rows = connection.run_change(insert_query, values)
        else:
            update_query = "UPDATE Pilot SET pilot_name=%s, salary=%s, gratification=%s, airline=%s, country=%s WHERE identification=%s"
            values = (self.__name, self.__salary, self.__bonus, self.__airline, self.__country, self.__id)
            affected_rows = connection.run_change(update_query, values)

        return affected_rows == 1


    # TODO 3. Create the function remove()
    # Process: - creates a Connection object (the class we created in file connection_solution.py)
    #          - initialize the Connection with the username and password received as parameters
    #          - use the appropriate function from Connection to delete the pilot based on the pilot's
    #                   identification number
    # Parameters: self
    #             user: the MySQL username that has permission to access the database
    #             pwd: the password for the user
    # Return: True if the data successfully affected one row in the Pilot table (insert or update);
    #         False, otherwise
    # Grading: function header (4 points); processing (4 points); return (4 points)
    def remove(self, user, pwd):
        connection = Connection(user=user, pwd=pwd, db="airline_db")
        delete_query = "DELETE FROM Pilot WHERE identification = %s"
        affected_rows = connection.run_change(delete_query, (self.__id,))
        return affected_rows == 1

    # TODO 4. Create the function load()
    # Process: - create a Connection object (the class we created in file connection_solution.py)
    #          - initialize the Connection with the username and password received as parameters
    #          - use the appropriate function from Connection to find an existing pilot based on
    #               the pilot's identification number provided as a parameter
    #          - if the identification number exists in the Pilot table, set the attributes of the
    #               pilot object to be the values recovered from the database
    # Parameters: self
    #             id: integer value that represents the an existing pilot's identification number
    #             user: the MySQL username that has permission to access the database
    #             pwd: the password for the user
    # Return: True if there is an existing Pilot in the table with the provided id and the values
    #               were successfully loaded into the pilot object
    #         False if identification number was not found in the Pilot table
    # Grading: function header (4 points); processing (4 points); return (4 points)
    def load(self, id, user, pwd):
        connection = Connection(user=user, pwd=pwd, db="airline_db")
        pilot_exists_query = "SELECT * FROM Pilot WHERE identification = %s"
        result = connection.run_select(pilot_exists_query, (id,))

        if len(result) == 0:
            return False
        else:
            self.__id, self.__name, self.__salary, self.__bonus, self.__airline, self.__country = result[0]
            return True
