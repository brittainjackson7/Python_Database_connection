from pilot import Pilot

def main():
    # Replace these with your MySQL credentials
    user = "root"
    pwd = "password"

    # Create a new pilot
    new_pilot = Pilot(id=1, name="John Doe", salary=90000, bonus=5000, airline="Airways Inc", country="USA")
    print("New pilot created:", new_pilot)

    # Save the pilot to the database
    success = new_pilot.save(user, pwd)
    if success:
        print("Pilot saved successfully")
    else:
        print("Error saving the pilot")

    # Load the pilot from the database
    loaded_pilot = Pilot()
    success = loaded_pilot.load(new_pilot.get_id(), user, pwd)
    if success:
        print("Pilot loaded successfully:", loaded_pilot)
    else:
        print("Error loading the pilot")

    # Update the pilot's information
    loaded_pilot.set_name("Jane Doe")
    loaded_pilot.set_country("UK")
    success = loaded_pilot.save(user, pwd)
    if success:
        print("Pilot updated successfully")
    else:
        print("Error updating the pilot")


if __name__ == "__main__":
    main()