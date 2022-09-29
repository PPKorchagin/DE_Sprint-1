input_str = 3

if input_str > 2000 or input_str < 0:
    exit(1)

elements = []

while input_str > 1000:
    elements.append("M")
    input_str -= 1000

hundreds = int(input_str / 100)

if hundreds == 9:
    elements.extend(["C", "M"])
elif hundreds >= 5:
    elements.append("D")
    elements.extend(["C"] * (hundreds - 5))
elif hundreds == 4:
    elements.extend(["C", "D"])
else:
    elements.extend(["C"] * hundreds)

input_str -= hundreds * 100

tens = int(input_str / 10)
if tens == 9:
    elements.extend(["X", "C"])
elif tens >= 5:
    elements.append("L")
    elements.extend(["X"] * (tens - 5))
elif tens == 4:
    elements.extend(["X", "L"])
else:
    elements.extend(["X"] * tens)

input_str -= tens * 10

if input_str == 9:
    elements.extend(["I", "X"])
elif input_str >= 5:
    elements.append("V")
    elements.extend(["I"] * (input_str - 5))
elif input_str == 4:
    elements.extend(["I","V"])
else:
    elements.extend(["I"] * input_str)



print(''.join(elements))
