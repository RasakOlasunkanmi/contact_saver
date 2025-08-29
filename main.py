import csv
from pathlib import Path
from helper import file_ops

workspace = Path("workspace_file") 
workspace.mkdir(exist_ok= True)
csv_file = workspace / "contacts.csv"

participants_dict = {}

def user_string_input(description):
    while True:
        try:
            participant = input(f"Enter your {description}: ")
            if participant == "":
                raise ValueError(f"You must enter your {description}")
            if participant.isdigit():
                raise ValueError("You must enter aplhabet")
            break
        except ValueError as e:
            print("Error:", e)
    return participant

while True:
    # Collecting user name
    paticipant_name = user_string_input("name")

    # collecting user age
    while True:
        try:
            paticipant_age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid input\nYou must enter a number")

    # Collecting participant number
    while True:
        try:
            participant_phone_number = input("Enter your phone number: ")
            if not participant_phone_number.isdigit():
                raise ValueError("invalid input\nYou must enter a number")
            if len(participant_phone_number) != 11:
                raise ValueError("Incomplete number")
            if not participant_phone_number.startswith("0"):
                raise ValueError("Phone number must start with zero")
            participant_number = int(participant_phone_number)
            break
        except ValueError as e:
            print("Error:", e)

    # collecting paticipant track 
    participant_track = user_string_input("track")

    participants_dict.update({
        "Name": paticipant_name,
        "Age": paticipant_age,
        "Phone number": participant_number,
        "Track": participant_track
    })

    # saving file to csv file
    file_ops.save_participant(csv_file, participants_dict)

    while True:
        exit = input("\nDid want to add more paticipants (yes/no): ").lower()
        if exit == "yes":
            print("Participants details have been saved successfully")
            break
        if exit == 'no':
            break
        else:
            print("Invalid input\nYou must input \"yes or no\"")
    if exit == 'yes':
        continue
    elif exit == 'no':
        break
      
# loading data from csv file
file_ops.load_participants(csv_file)
