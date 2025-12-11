email = "Amit_ml@gmail.edu"
at = email.count("@")
dot = email.count(".")
if at != 1 or dot != 1:
    print("Invalid email")
print(email[0:(email.index("@")):1])
print(email[(email.index("@")):(email.index(".")):1])
