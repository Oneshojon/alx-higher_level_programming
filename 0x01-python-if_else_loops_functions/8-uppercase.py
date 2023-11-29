def uppercase(str):
    for i in str:
        int_value = ord(i)
        if int_value >= 97 and int_value <= 122:
            int_value -= 32
        print("{:c}".format(int_value), end="")
    print()
