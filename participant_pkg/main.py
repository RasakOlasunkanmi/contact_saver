from modules import get_data


get_data.display_menu()
while True:
      choice = input("Please enter the option number: ").strip()
      get_data.take_option_action(choice)


