previous_string = ""
while True:
    str1 = input("Please enter a random string: ")

    if str1 == previous_string:
        break

    print(str1)
    previous_string = str1