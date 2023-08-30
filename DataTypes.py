# declaring list data type

values = [1, 2, "rahul", 4, 5]
print(values)
print(type(values))
print(values[2])
print(values[-1])      # print last value
print(values[1:3])     # print range

values[2] = "RAHUL"    # updating any value
print(values)

values.insert(3, "shetty")      # add value in the list
print(values)

values.append("End")      # add value at the end of the list (last value)
print(values)

# del values     # delete entire list

# del values[2]   # delete any value from the list
print(values)






# declaring tuple data type

val = (1, 2, "rahul", 4.5)
print(val)
print(val[1])







# declaring dictionary data type

dic = {"a": 2, 4: "bcd", "c": "Hello world"}
print(dic)
print(dic[4])
print(dic["c"])


# declaring empty dictionary first and then filling values into it later

dict = {}

dict["firstname"] = "Pooja"
dict["lastname"] = "Kale"
dict["vehiclenumber"] = 2035
dict[1] = 1

print(dict)

print(dict["lastname"])



