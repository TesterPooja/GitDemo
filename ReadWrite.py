'''
file = open('test.txt')
print(file.read())      # to read all content of the file

print(file.read(2))     # read no. of characters by passing parameter
print(file.read(5))

print(file.readline())   # read single line at a time


line = file.readline()      # print all lines in file
while line != "":
    print(line)
    line = file.readline()
print("all lines printed")


for i in file.readlines():     # read all lines using readlines method which convert line into list
    print(i)
print("all lines printed")

file.close() '''

print("***************************  WRITE INTO FILE  ***************************")

with open('test.txt', 'r') as reader:
    content = reader.readlines()     # content is variable to store data from file, output is list
    reversed(content)                # output is reversed list ["elephant", "dog" etc.]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
print("writing completed")

with open('test.txt', 'r') as reader:     # to check if content is reversed after writing
    file = reader.readlines()
    for i in file:
        if i != "":
            print(i)
print("reversed list is produced")



