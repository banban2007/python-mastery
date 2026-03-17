def signup(username,password):
    message = username + "account is ready !"
    return message

username = input("Enter account name: ")
password = input("Enter account password: ")
print(signup(username,password))
print(signup(username))  # TypeError: signup() missing 1 required positional argument: 'password'