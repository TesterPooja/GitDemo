# if else condition code

greeting = "Good Morning"

if greeting == "Morning":
    print("condition matches")
else:
    print("Condition do not match")
print("done")


a = 4

if a > 2:
    print("a is greater")
else:
    print("a is lesser")
print("done")


# for in loop

obj = [2, 3, 5, 7, 9]     # for loop for list

for i in obj:
    print(i)

for i in obj:
    print(i+2)

# sum of first 5 natural numbers

summation = 0
for i in range(1, 6):               # for loop for range, it will print till n-1 from 0
    summation = summation + i

print(summation)

print("***************  increment by index other than default 1, 3rd argument  *****************")
for k in range(1, 10, 2):
    print(k)

print("***************  when first index in range is not given, default is 0  *****************")
for k in range(10):
    print(k)



print("##################   WHILE LOOP   #####################")

it = 4                     # basic example

while it > 1:
    print(it)
    it = it - 1

print("while loop execution is done")

a = 4                       # do not want to print particular observation

while a > 1:
    if a != 3:
        print(a)

    a = a - 1

print("while loop execution is done")


b = 10                  # break statement example

while b > 1:
    if b == 3:
        break
    print(b)

    b = b - 1

print("while loop execution is done")


c = 10         # continue statement example

while c > 1:
    if c == 9:
        c = c - 1
        continue
    if c == 3:
        break
    print(c)

    c = c - 1

print("while loop execution is done")




