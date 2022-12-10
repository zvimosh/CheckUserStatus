
"""Defines a list of users, each user is a dictionary with keys 'name','admin' and 'active'"""
multi_users = [
    {'admin': True, 'active': True, 'name': 'Kevin'},
    {'admin': True, 'active': False, 'name': 'Bob'},
    {'admin': False, 'active': True, 'name': 'John'},
    {'admin': False, 'active': False, 'name': 'Jane'}
]

def find_value_by_key(key, value, list_of_dicts):
    """Return True if value is found in list_of_dicts, False otherwise"""

    #print(f"key: {key}, value: {value}, list_of_dicts: {list_of_dicts}")
    if not any(_dict[key] == value for _dict in list_of_dicts if key in _dict):
        return False
    else:
        return True
def get_user_name():
    """Get user name from user input"""

    user = ""
    while not user:
        user = input(str("Enter user name: "))
        if user == "q" or user == "Q":
            print("Goodbye")
            break
        elif not user:
            print("Invalid input\ntry again, or enter 'q' or 'Q' to quit")
            user = input(str("Enter user name: "))
        elif find_value_by_key('name', user, multi_users) == False:
            print(f"Invalid user name: {user}")
        else:
            return user


def get_user_status(user_name):
    """Get user status from user input"""
    print ("-----------------")
    for user in multi_users:
        if user['name'] == user_name:
            if user['admin'] == True and user['active'] == True:
                print(f"ACTIVE - (ADMIN) {user['name']}")
            elif user['admin'] != True and user['active'] == True:
                print(f"ACTIVE {user['name']}")
            elif user['admin'] != True and user['active'] != True:
                print(f"{user['name']}")

if __name__ == "__main__":
    #get_user_name()
    get_user_status(get_user_name())




 


