previous_string = ""
combined = ""
while True:
    str1 = input("Please enter a random string: ")

    if str1 == previous_string:
        break

    combined += str1 + " "
    print(combined[:-1])
    previous_string = str1

#Did it all by myself excluding the [:-1] couldnt find any way to make it break after repeated words
#so i used chat GPT and this is the only solution i knew and understood.