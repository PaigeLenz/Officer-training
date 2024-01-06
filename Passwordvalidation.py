def user_password(password):
    if len(password) < 8:
        return False
    return True

password = input("Please enter your password:")
is_valid = user_password(password)

if is_valid:
    print("Valid Password.")
else:
    print("Please enter a password longer than 8 characters.")