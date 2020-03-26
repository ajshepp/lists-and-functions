print()
print("==========================================="); print("  Start program: Lists & Functions Combos "); print("===========================================")
print(); print()

print("Multiply specific index from a list:")
n = [1, 2, 3]
n[1] = n[2] * 5 # n[1] indicates where value will populate
                # n[2] represents value from array that will get multiplied

print(n)


print(); print(); print("////next example////")


print("Multiply variable by some value:")
number = 5
def multiply_var(x): # Pass variable to a function and return var x value
    return x * 3

print(multiply_var(number))


print(); print(); print("////next example////")


print("Add two variables together:")
a = 2
b = 3

def add_function(a, b): # Pass variables to a function and return value + value
    return a + b

print(add_function(a,b))


print(); print(); print("////next example////")


print("A function that returns the sum of a list:")
n = [15, 30, 45, 50]

def sum_list(a): # pass a list to a function to sum all elements
    result = 0
    for e in a:
        result += e
    return result

print(sum_list(n))




print(); print("=================================="); print()




print("How to write a string:")
n = "hello"
def string_function(s): # write string function and concatenate with another string
    return s + "_world"

print(string_function(n))


print(); print(); print("////next example////")


n = ["Michael", " Lieberman"]
def join_strings(a):
    result = ""
    for e in a:
        result += e
    return result

print(join_strings(n))




print(); print("=================================="); print()




print("Pass a list to a function:")
def list_function(x): # pass a list to a function
    return x

n = [5, 7, 9]
print(list_function(n))


print(); print(); print("////next example////")


print("Pass list to a function and return a specific element:")
def new_list_function(x): # pass a list to a function and return a specific element
    return x[1]

n = [11, 13, 15]
print(new_list_function(n))


print(); print(); print("////next example////")


print("Print elements from a list one by one:")
n = [8, 10, 12]

def one_by_one(x): # define a function, write for loop to print each element one by one
    for i in range(0, len(x)):
        print(x[i])

print(one_by_one(n))




print(); print("=================================="); print()




print("Multiply each element in a list by one value and return list:")
n = [20, 40, 60]

n2 = [i * 2 for i in n] # multiply each element in a list by a value

print(n2)


print(); print(); print("////next example////")


print("Multiply one element in a list by one value and return list:")
n = [12, 14, 16]

def double_value_in_list(x): # define a function, write for loop that returns one doubled element
    for i in range(3): 
        x[i] = x[i] * 2
        return x

print(double_value_in_list(n))




print(); print("=================================="); print()




print("Generate numbers in an empty list:")
a = []
for i in range(3): # fill an empty list with numbers using for loop+range and .append
    a.append(i)

print(a)


print(); print(); print("////next example////")


print("Add a value to the array:")
n = [1, 3, 5]
n.append(4) # append (add) number to the end of a list

print(n)




print(); print("=================================="); print(" Diff Methods for adding/removing") 
print("       values from an array:"); print("=================================="); print()




print(".pop() removes a value from specified index:")
n = [1, 2, 3]
n.pop(1) # returns (removes) value from specified index

print(n)


print(); print(); print("////next example////")


print(".remove() removes first matching value from list:")
n = [2, 4, 2, 4, 4, 2, 4, 6]
n.remove(4) # removes first maching vale from a list

print(n)


print(); print(); print("////next example////")


print("Join two lists together:")
a1 = [1, 3, 3, 3]
a2 = [2, 2, 4, 4, 4, 4]

def join_lists(x,y): # a fucntion to concatenate two separate lists into one array
    return [x] + [y] # w/ or w/out brackets produces different results

print(join_lists(a1, a2))


print(); print(); print("////next example////")


print("Flatten function concatenates sublists into a single list:")
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
    results = []
    for e in lists:
        for n in e:
            results.append(n)
    return results

print(flatten(n))




print(); print(); print("===================="); print("   End of program"); print("====================")