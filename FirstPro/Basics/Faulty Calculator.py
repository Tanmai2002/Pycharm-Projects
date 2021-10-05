cal = input("Enter then values to be calculated :\n")
# Plz avoid spacing
val = []
ans = 0
if cal.__contains__("*"):
    val = cal.split("*")
    ans = float(val[0]) * float(val[1])
    if cal.__contains__("45*3") and len(cal) == 4:
        ans = 555

if cal.__contains__("/"):
    val = cal.split("/")
    ans = float(val[0]) / float(val[1])
    if cal.__contains__("56/6") and len(cal) == 4:
        ans = 4

if cal.__contains__("+"):
    val = cal.split("+")
    ans = float(val[0]) + float(val[1])
    if cal.__contains__("56+9") and len(cal) == 4:
        ans = 77

if cal.__contains__("-"):
    val = cal.split("-")
    ans = float(val[0]) - float(val[1])

print(ans)
