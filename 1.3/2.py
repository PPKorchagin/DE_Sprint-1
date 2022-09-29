import sys

if len(sys.argv) != 2:
    print("need one argument")
    exit(1)

orig_str = sys.argv[1]
str = orig_str.replace(" ","")

if str == str[::-1]:
    print(f"{orig_str} is palindrome")
else:
    print("try another word")
