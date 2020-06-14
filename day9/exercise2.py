# Exercise is: Suppose below list as input is passing in function and get ouput in a list
# Ouput should be in strings for numbers & floats which are being used in input list

# input -> [True, False, [1,2,3], 1, 2.0, 3]
# output -> ['1', '2', '3'] # Output should be a list in string for numbers & floats used in input list above

# Normal Way:
def string_list(lis):
    output_list = []
    for i in lis:
        if (type(i) == int or type(i) == float):
            app_i = str(i)
            output_list.append(app_i)
    return output_list

input = [True, False, [1,2,3], 1, 2, 3]
print(string_list(input))


# Using LC:
input = [True, False, [1,2,3], 1, 2, 3]
output = [str(i) for i in input if (type(i) == int or type(i) == float)]
print(output)

# Using LC: Making a func for this
input = [True, False, [1,2,3], 1, 2, 3]
def lc_func(lis):
    return [str(i) for i in input if (type(i) == int or type(i) == float)]

print(lc_func(input))