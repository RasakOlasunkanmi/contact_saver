# import csv
# from pathlib import Path

# workspace = Path("workspace_files")
# workspace.mkdir(exist_ok=True)
# csv_file = workspace / "contacts.csv"

# contacts = [
#     ["Name", "Age", "Phone number", "Track"],  # Header row
#     ["Precious", 20, "09123456789", "Python"],
#     ["Favour", 22, "08012345678", "JavaScript"],
#     ["Ore", 21, "08165432876", "Python"],
#     ["Susan", 23, "09087654335", "Data Science"]
# ]

# # Write data to CSV file
# with open(csv_file, "w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerows(contacts)  # Write all rows at once

def save_participant(path: Path, participant_dict: dict):
    """
    Save a participant's details into a CSV file.
    If the file does not exist, create it with a header.
    """
    try:
        file_exists = path.exists()
        with path.open(csv_file, "a", newline="", encoding="utf-8") as f:
            fieldnames = ["Name", "Age", "Phone", "Track"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            # Write header only if file is new
            if not file_exists:
                writer.writeheader()

            writer.writerow(participant_dict)

    except Exception as e:
        raise IOError(f"Error saving participant: {e}")


def load_participants(path: Path):
    """
    Load all participants from the CSV file.
    Returns a list of dictionaries.
    """
    participants = []
    try:
        if path.exists():
            with path.open(csv_file, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    participants.append(row)
    except Exception as e:
        raise IOError(f"Error loading participants: {e}")

    return participants


def display_participants(path: Path):
    """
    Load and display participants in a nicely formatted table.
    """
    participants = load_participants(path)

    if not participants:
        print("\nNo participants found.")
        return

    print("\n=== Participants List ===")
    print(f"{'Name':<15}{'Age':<5}{'Phone':<15}{'Track'}")
    print("-" * 50)

    for p in participants:
        print(f"{p['Name']:<15}{p['Age']:<5}{p['Phone']:<15}{p['Track']}")






# from pathlib import Path

# csv_file = Path("workspace/contacts.csv")

# # Load all participants from the CSV
# participants = load_participants(csv_file)
# # Display them in a table with header
# display_participants(csv_file)
# # Show summary count
# print(f"\nWorkshop registration complete! {len(participants)} participants saved.")
# print("\nReading CSV file:")

# with open(csv_file, "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
    
#     # for row_number, row in enumerate(reader):
#     #     if row_number == 0:  # Header row
#     #         # print(f"{'\t\t|'.join(row)}")
# for c in contacts:

#             print(f"{c['Name']:<15}{c['Age']:<5}{c['Phone']:<15}{c['Track']}")
#             print("-" * 70)
#             name, age, phone, track = contacts
#             # print("\n=== Participants List ===")
#             print(f"{name:<20}{age:<15}{phone:<25}{track}")
        
# import csv
# from pathlib import Path

# workspace = Path("workspace_files")
# workspace.mkdir(exist_ok=True)
# csv_file = workspace / "contacts.csv"

# contacts = [
#     ["Name", "Age", "Phone number", "Track"],  # Header row
#     ["Precious", 20, "09123456789", "Python"],
#     ["Favour", 22, "08012345678", "JavaScript"],
#     ["Ore", 21, "08165432876", "Python"],
#     ["Susan", 23, "09087654335", "Data Science"]
# ]

# with open(csv_file, "r", encoding="utf-8") as f:
#     reader = csv.reader(f)

#     # Read header row
#     header = next(reader)  
#     print(f"{header[0]:<20}{header[1]:<10}{header[2]:<20}{header[3]}")
#     print("-" * 70)

#     # Loop through remaining rows
#     for row in reader:
#         name, age, phone, track = row
#         print(f"{name:<20}{age:<10}{phone:<20}{track}")





import csv
from pathlib import Path

workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)
csv_file = workspace / "contacts.csv"

# Sample contacts data
contacts = [
    ["Name", "Age", "Phone number", "Track"],  # Header row
    ["Precious", 20, "09123456789", "Python"],
    ["Favour", 22, "08012345678", "JavaScript"],
    ["Ore", 21, "08165432876", "Python"],
    ["Susan", 23, "09087654335", "Data Science"]
]

# Write contacts to file first (if file is empty or missing)
if not csv_file.exists():
    try:
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(contacts)
    except Exception as e:
        print("Error writing to CSV:", e)

# Read with error handling
try:
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        try:
            header = next(reader)  # read header row
            print(f"{header[0]:<20}{header[1]:<10}{header[2]:<20}{header[3]}")
            print("-" * 70)
        except StopIteration:
            print("CSV file is empty.")
        else:
            for row_number, row in enumerate(reader, start=2):
                try:
                    name, age, phone, track = row
                    print(f"{name:<20}{age:<10}{phone:<20}{track}")
                except ValueError:
                    print(f"Skipping malformed row {row_number}: {row}")

except FileNotFoundError:
    print("Error: CSV file not found.")
except Exception as e:
    print("Unexpected error:", e)
