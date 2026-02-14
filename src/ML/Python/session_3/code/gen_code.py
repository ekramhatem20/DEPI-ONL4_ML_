import random
def Generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ""
    for _ in range (length):
        password += random.choice(characters)
    return f"Generate_password: {password} "
Generate_password(8)