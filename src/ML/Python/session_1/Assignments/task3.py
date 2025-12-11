message = "gnirtS PLIO"
split_message = message.split()
first_word = split_message[0][::-1]
second_word = split_message[1].replace("I""O","E""U")
print(f"{first_word} {second_word}")