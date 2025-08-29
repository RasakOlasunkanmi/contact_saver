from pathlib import Path
import csv


def save_participant(path, participant_dict):
    """
    Save a participant's details in a csv file.
    If the file does not exsit, create it with a header.
    """
    file_exit = path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames= participant_dict.keys())
        if not file_exit:
            writer.writeheader()
        writer.writerow(participant_dict)

def load_participants(path):
    """
    Load and display all participants in a nicely formatted table
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)

            try:
                header = next(reader)   # read header row
                print(f"{header[0]:<20}{header[1]:<20}{header[2]:<20}{header[3]:<20}")
                print("-"*70)
            except StopIteration:
                print("csv file is empty.")
            else:
                for row_number, row in enumerate(reader, start=2):
                    try:
                        name, age, phone, track = row
                        print(f"{name:<20}{age:<20}{phone:<20}{track:<20}")
                    except ValueError:
                        print(f"Skipping malformed row {row_number}")
    except FileNotFoundError:
        print("Error: csv file not found.")
    except Exception as e:
        print("Unexpected error:", e)
