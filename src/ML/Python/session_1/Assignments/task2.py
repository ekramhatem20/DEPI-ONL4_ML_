message = "mocleW EPGTQ"
split_message = message.split()
first_word = split_message[0][::-1]
second_word = split_message[1].replace("E","") 
print(f"{first_word} {second_word}")