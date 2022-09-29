string = "[{}({})]"

br = {
    "[": 0,
    "(": 0,
    "{": 0,
}

rbr = {
    "]": "[",
    "}": "{",
    ")": "("
}

inside = []


def die(*msg):
    print(*msg)
    exit()


for ch in string:
    #print(ch, inside)
    if ch in "[({":
        br[ch] += 1
        inside.append(ch)
    elif ch in "])}":
        if len(inside) == 0:
            die("False")
        elif inside[-1] == rbr[ch]:
            br[rbr[ch]] -= 1
            inside.pop()
        else:
            die(f"Error: need to close {inside[-1]}, but we have {ch}")
    else:
        die("False")

die(str(len(inside) == 0))
