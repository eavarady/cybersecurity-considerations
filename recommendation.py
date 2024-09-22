from Cybersecurity_Dataset import categories, tool_data
def welcome():
    print("______________________________________\n")
    print("\nWelcome to Cybersecurity Considerations!\n")
    print("What kind of software are you looking for?\nAvailable categories are the following:\n")
    print("______________________________________\n")
    for i in categories:
        print(i + "\n")
    print("______________________________________\n")
    return input("Pick a category:\n").lower()
def search(category):
    print("______________________________________\n")
    if category not in categories:
        print("Wrong input! Restarting the program!\n")
        print("______________________________________\n")
        return welcome()
    print("SEARCH RESULTS:\n")
    for i in tool_data:
        if i[0] == category:
            print(f"Name: {i[1]}\nPrice per yearly license: ${i[2]}\nRating: {i[3]} out of 5\nVendor: {i[4]}\n")
    print("______________________________________\n")

if __name__ == '__main__':
    user_choice = "y"
    while user_choice == "y":
        user_input = welcome()
        search(user_input)
        user_choice = input("Thank you for using Cybersecurity Considerations! Would you like to search somenthing else? Enter y/n: \n").lower()
    print("Goodbye!\n")
    print("______________________________________\n")