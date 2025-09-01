import csv
import os
from pathlib import Path



"""
  First check if the file does not exsit, create it with a header.
  after that subsequently check if the participant details already exist in the csv file,
  if not then save the participant's details in the csv file.
"""
def save_participant(path, participant_dict):
    workspace = Path("data")
    workspace.mkdir(exist_ok=True)

    # Ensure file exists, if not create with headers
    file_exists = os.path.isfile(path)
    fieldnames = ["Full Name", "Phone", "Age", "Track"]

    if not file_exists:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

    with open(path, mode="r+", newline="", encoding="utf-8") as f:
        contacts = list(csv.DictReader(f))

        # Check if name or phone already exists
        for row in contacts:
            if row["Full Name"] == participant_dict["Full Name"] or row["Phone"] == participant_dict["Phone"]:
                print("Record already exists:", row)
                return

        # Append new record
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(participant_dict)
        print("Record added successfully!")    
        
# save_participant('participants.csv',{
#   'Full Name' : 'peter okonmah',
#   'Phone' : "07036947783",
#   "Age" : 18,
#   "Track" : "Engineer"
# })

"""
Load and display all participants in a nicely formatted table
"""
def load_participants(path):
  if not os.path.isfile(path):
    return []
  
  with open(path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    return list(reader)
  
# data = load_participants("participants.csv")
# print(data)
  