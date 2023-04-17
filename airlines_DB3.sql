drop database if exists airline_db;
create database if not exists airline_db;
use airline_db;

create table Pilot (
    identification int primary key not null,
    pilot_name varchar(100) not null,
    salary decimal(10 , 2 ),
    gratification decimal(10 , 2 ),
    airline varchar(30),
    country varchar(15)
);

create table Airport(acronym varchar(3) primary key not null,
                    airport_name varchar(100) not null,
                    city varchar(50),
                    country varchar(15));

create table Flight(flight_number varchar(6) primary key not null,
                    departure_airport varchar(3) not null,
                    destination_airport varchar(3) not null,
                    departure_time time,
                    foreign key (departure_airport) references Airport(acronym) on delete cascade,
                    foreign key (destination_airport) references Airport(acronym) on delete cascade);

create table Stopover(flight_number varchar(6) not null,
                    flight_date date not null,
                    pilot_id int not null,
                    aircraft varchar(30),
                    primary key(flight_number, flight_date),
                    foreign key (flight_number) references Flight(flight_number) on delete cascade,
                    foreign key (pilot_id) references Pilot(identification) on delete cascade);

-- DML STARTS HERE --
insert into Pilot values
            (279, "Steven Grant Rogers", 30000.00, 500.00, "American Airlines", "USA"),
            (627, "Wanda Maximoff", 30000.00, 500.00, "American Airlines", "USA"),
            (947, "Natasha Romanoff", 25000.00, 800.00, "United", "USA"),
            (463, "Anthony Edward Stark", 20000.00, 800.00, "United", "USA"),
            (839, "Robert Bruce Banner", 35000.00, 500.00, "American Airlines", "USA"),
            (628, "Carol Susan Jane Danvers", 30000.00, 500.00, "Air France", "France"),
            (832, "Clinton Francis Barton", 20000.00, 800.00, "Air Canada", "Canada"),
            (602, "Stephen Vincent Strange", 25000.00, 800.00, "Air Canada", "Canada"),
            (633, "Victor Shade", 28000.00, 600.00, "Air France", "France"),
            (382, "Jessica Jones", 35000.00, 700.00, "Japan Airlines", "Japan");

insert into Airport values
            ("LAS", "Harry Reid International Airport", "Las Vegas", "USA"),
            ("PHX", "Phoenix Sky Harbor Airport", "Phoenix", "USA"),
            ("DFW", "Dallas Fort Worth Airport", "Dallas", "USA"),
            ("IAH", "George Bush Intercontinental Airport", "Houston", "USA"),
            ("LAX", "Los Angeles International Airport", "Los Angeles", "USA"),
            ("GRU", "Guarulhos International Airport", "Guarulhos", "Brazil"),
            ("BSB", "Presidente Juscelino Kubitschek International Airport", "Brasilia", "Brazil"),
            ("MAO", "Eduardo Gomes International Airport", "Manaus", "Brazil"),
            ("CDG", "Aéroport Paris-Charles de Gaulle", "Paris", "France"),
            ("LYS", "Aéroport Lyon Saint-Exupéry", "Lyon", "France"),
            ("MRS", "Marseille Provence Airport", "Marselha", "France");

insert into Flight values
            ("RG230", "LAX", "PHX", "23:05"),
            ("PR231", "IAH", "LAS", "12:15"),
            ("TG331", "DFW", "LAX", "17:22"),
            ("AV431", "PHX", "GRU", "02:10"),
            ("KI356", "IAH", "MAO", "23:55"),
            ("OD468", "BSB", "LAX", "11:45"),
            ("PS324", "PHX", "GRU", "22:19"),
            ("OO677", "GRU", "DFW", "18:52"),
            ("TW873", "GRU", "LYS", "18:52"),
            ("IE832", "LYS", "MRS", "04:40"),
            ("JD646", "CDG", "LYS", "05:00"),
            ("MD342", "CDG", "BSB", "08:34"),
            ("UJ658", "LAS", "IAH", "08:34"),
            ("GF774", "LAS", "DFW", "08:34");

insert into Stopover values
            ("RG230", "2022-12-30", 279, "Boeing 747"),
            ("RG230", "2022-09-24", 628, "Boeing 747"),
            ("PR231", "2022-08-15", 279, "Airbus A380"),
            ("PR231", "2022-01-12", 947, "Airbus A380"),
            ("TG331", "2022-02-05", 947, "Boeing 747"),
            ("TG331", "2022-01-12", 627, "Airbus A380"),
            ("AV431", "2022-12-04", 463, "Embraer 195"),
            ("AV431", "2022-10-30", 839, "Airbus A380"),
            ("KI356", "2022-09-07", 463, "Embraer 195"),
            ("KI356", "2022-08-13", 463, "Embraer 175"),
            ("OD468", "2022-03-13", 839, "Airbus A330"),
            ("OD468", "2022-04-01", 839, "Airbus A330"),
            ("OD468", "2022-04-02", 839, "Airbus A330"),
            ("PS324", "2022-03-15", 627, "Airbus A320"),
            ("PS324", "2022-03-18", 627, "Embraer 195"),
            ("OO677", "2022-02-09", 832, "Embraer 195"),
            ("OO677", "2022-02-01", 832, "Boeing 797"),
            ("TW873", "2022-12-11", 602, "Boeing 797"),
            ("TW873", "2022-11-17", 633, "Boeing 797"),
            ("IE832", "2022-05-17", 633, "Embraer 195"),
            ("IE832", "2022-08-16", 602, "Embraer 175"),
            ("JD646", "2022-09-27", 602, "Embraer 175"),
            ("JD646", "2022-09-29", 832, "Airbus A320"),
            ("MD342", "2022-09-29", 382, "Airbus A320"),
            ("MD342", "2022-10-31", 382, "Airbus A330"),
            ("UJ658", "2022-03-30", 633, "Boeing 797"),
            ("UJ658", "2022-02-25", 279, "Boeing 797"),
            ("GF774", "2022-01-22", 602, "Boeing 747"),
            ("GF774", "2022-01-12", 633, "Boeing 747");

-- DML QUERIES START HERE --

-- a. Find the flight number and the destination country for all the flights to France or Brazil along with the departure’s date and time.

SELECT Flight.flight_number, Airport.country, Stopover.flight_date, Flight.departure_time
FROM Flight
JOIN Airport ON Flight.destination_airport = Airport.acronym
JOIN Stopover ON Flight.flight_number = Stopover.flight_number
WHERE Airport.country IN ('France', 'Brazil');

-- b. Find the name and airline of all the pilots who work for the same airline as Wanda Maximoff.

SELECT pilot_name, airline
FROM Pilot
WHERE airline = (
SELECT airline
FROM Pilot
WHERE pilot_name = 'Wanda Maximoff'
);

-- c. Find the airline companies of pilots who fly to France.

SELECT DISTINCT Pilot.airline
FROM Pilot
JOIN Stopover ON Pilot.identification = Stopover.pilot_id
JOIN Flight ON Stopover.flight_number = Flight.flight_number
JOIN Airport ON Flight.destination_airport = Airport.acronym
WHERE Airport.country = 'France';

-- d. Find the destination (airport name, city and country) for all the flight operated by American Airlines.

SELECT Airport.airport_name, Airport.city, Airport.country
FROM Airport
JOIN Flight ON Airport.acronym = Flight.destination_airport
JOIN Stopover ON Flight.flight_number = Stopover.flight_number
JOIN Pilot ON Stopover.pilot_id = Pilot.identification
WHERE Pilot.airline = 'American Airlines';

-- e. Find the name of the destination airports of flights that have more than two stopovers.

SELECT Airport.airport_name
FROM Airport
WHERE Airport.acronym IN (
SELECT Flight.destination_airport
FROM Flight
JOIN Stopover ON Flight.flight_number = Stopover.flight_number
GROUP BY Flight.destination_airport
HAVING COUNT(*) > 2
);

-- f. Find the names of the departure and destination airports for all the flights scheduled to 2022-01-12.

SELECT A1.airport_name AS departure_airport_name, A2.airport_name AS destination_airport_name
FROM Stopover
JOIN Flight ON Stopover.flight_number = Flight.flight_number
JOIN Airport A1 ON Flight.departure_airport = A1.acronym
JOIN Airport A2 ON Flight.destination_airport = A2.acronym
WHERE Stopover.flight_date = '2022-01-12';

-- g. Find the destination airports (name, city) for all the flights operated by United in Embraer aircrafts.

SELECT Airport.airport_name, Airport.city
FROM Airport
JOIN Flight ON Airport.acronym = Flight.destination_airport
JOIN Stopover ON Flight.flight_number = Stopover.flight_number
JOIN Pilot ON Stopover.pilot_id = Pilot.identification
WHERE Pilot.airline = 'United' AND Stopover.aircraft LIKE 'Embraer%';

-- h. Find the flight number and time for all the domestic flights for all countries.

SELECT Flight.flight_number, Flight.departure_time
FROM Flight
JOIN Airport A1 ON Flight.departure_airport = A1.acronym
JOIN Airport A2 ON Flight.destination_airport = A2.acronym
WHERE A1.country = A2.country;

-- i. Find the name of all the airports where American Airlines operates.

SELECT DISTINCT Airport.airport_name
FROM Airport
JOIN Flight ON (Airport.acronym = Flight.departure_airport OR Airport.acronym = Flight.destination_airport)
JOIN Stopover ON Flight.flight_number = Stopover.flight_number
JOIN Pilot ON Stopover.pilot_id = Pilot.identification
WHERE Pilot.airline = 'American Airlines';

-- j. Find the total income (salary + gratification) for pilots that have the lowest gratification.

SELECT pilot_name, (salary + gratification) as total_income
FROM Pilot
WHERE gratification = (
SELECT MIN(gratification)
FROM Pilot
);

-- k. Find the name of the pilots who flights Boeing aircrafts to their own country.

SELECT Pilot.pilot_name
FROM Pilot
JOIN Stopover ON Pilot.identification = Stopover.pilot_id
JOIN Flight ON Stopover.flight_number = Flight.flight_number
JOIN Airport ON Flight.destination_airport = Airport.acronym
WHERE Stopover.aircraft LIKE 'Boeing%' AND Pilot.country = Airport.country;

-- l. Find the flight number for all international flights that depart from the company’s country (from the company’s country to a different country).

SELECT Flight.flight_number
FROM Flight
JOIN Airport A1 ON Flight.departure_airport = A1.acronym
JOIN Airport A2 ON Flight.destination_airport = A2.acronym
JOIN Stopover ON Flight.flight_number = Stopover.flight_number
JOIN Pilot ON Stopover.pilot_id = Pilot.identification
WHERE A1.country = Pilot.country AND A1.country != A2.country;