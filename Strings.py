str = " RahulShettyAcademy.com "
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[1])
print(str[0:5])

print(str + str1)       # concatenation of strings

print(str3 in str)      # substring check

var = (str.split("."))    # split string, after splitting list is created
print(var)
print(var[0])

print("*************  loop execution after converting string into list ***************")

for i in var:
    if i != "":
        print(i)

print("all values done")

print("*************  loop execution after converting string into list ***************")

print(str.strip())       # trim string
print(str.lstrip())
print(str.rstrip())
