import sys

if len(sys.argv) != 2:
    print("need one argument")
    exit(1)

def is_palindrome(val):
    str = val.replace(" ", "")

    return str == str[::-1]


if is_palindrome(sys.argv[1]):
    print(f"{sys.argv[1]} is palindrome")
else:
    print("try another word")
