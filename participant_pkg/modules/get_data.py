from modules import file_ops

'''
This class is to display and get data from users
'''

def display_menu():
    print("\n=== Participant Contact Saver ===")
    print("1. Add new Participant Contact")
    print("2. Edit Participant Contact")
    print("3. Delete Participant Contact")
    print("4. View All Contacts")
    print("5. Exit")
   

def add_participant():
    print("Adding new participant...")
    full_name = input("Please enter the Participant Full Name: ")
    phone = collect_participant_phone_number()
    age = collect_participant_age()
    track = input("Please enter the Participant Track: ")
    data = {
      'Full Name' : full_name,
      'Phone' : phone,
      'Age' : age,
      'Track' : track
      
    }
    
    file_ops.save_participant('participants.csv', data)
    exit()

def edit_participant():
    print("Editing participant...")

def delete_participant():
    print("Deleting participant...")
    
def show_all_participants():
    print("\n📋 All Participants\n" + "-"*80)
    data = file_ops.load_participants("participants.csv")
    
    if not data:
        print("No participants found.")
        return

    # Print header
    print(f"{'S/N':<5}{'Full Name':<25}{'Phone':<15}{'Age':<15}{'Track'}")
    print("-"*80)

    # Print each participant
    for idx, row in enumerate(data, start=1):
        print(f"{idx:<5}{row['Full Name']:<25}{row['Phone']:<15}{row['Age']:<15}{row['Track']}")

    
    another_use = input('\nDo you want to see the menu again y/n? :').lower()
    if another_use == "y":
      display_menu()
    else:
      print("Thank you for using the contact saver app. Goodbye!")
      exit()

def exit_app():
    print("Thank you for using contact saver app. Goodbye!")
    exit()
    
def take_option_action(choice):
    actions = {
        "1": add_participant,
        "2": edit_participant,
        "3": delete_participant,
        "4": show_all_participants,
        "5": exit_app,
    }
    
    action = actions.get(choice)
    if action:
        action()
    else:
        print("❌ Invalid option, please try again.")
        
        
def collect_participant_phone_number():
    while True:
        # Ask for the user's phone number
        phone_number = input("Please enter the Participant Phone Number: ")

        # Clean up the input by removing any spaces or dashes
        phone_number = phone_number.replace(" ", "").replace("-", "")

        # Check if the phone number starts with '0' or '+234' and has exactly 11 digits
        if phone_number.startswith('0') and len(phone_number) == 11 and phone_number[1:].isdigit():
            return phone_number
        elif phone_number.startswith('+234') and len(phone_number) == 13 and phone_number[4:].isdigit():
            return phone_number
        else:
            print("Invalid phone number. Please enter a valid Nigerian phone number.")
            
def collect_participant_age():
  while True:
    age_input = input("Please enter the Participant Age: ").strip()
    if age_input.isdigit():
        age = int(age_input)
        if 18 <= age <= 70:
           return age
        else:
            print("Age must be between 18 and 70.")
    else:
        print("Invalid input. Please enter a number.")
