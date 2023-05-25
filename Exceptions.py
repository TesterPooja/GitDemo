# exception means we want to explicitly fail the test if condition is not matched
# we can fail test by using below 2 methods

ItemsInCart = 0

if ItemsInCart != 2:        # using exception method
    # raise Exception("products cart count not matched")
    pass  # pass statement does nothing,it just passes the condition since we have commented line for exception method

assert (ItemsInCart == 0)      # using assertion method

print("***************  TRY CATCH MECHANISM  *****************")

try:
    with open('test.txt', 'r') as reader:
        reader.read()
        print("printing as there is NO ERROR in try block")
except:
    print("printing this as there is ERROR in try block")


try:             # to know which error python has thrown
    with open('filelog.txt', 'r') as reader:
        reader.read()
        print("NO ERROR")

except Exception as e:     # store error msg in variable e
    print(e)

finally:             # this block is to execute such steps irrespective of test pass or fail
    print("cleaning records")



