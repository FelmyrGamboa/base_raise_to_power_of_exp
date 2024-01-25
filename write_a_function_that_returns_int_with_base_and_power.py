# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

# Expected output

# Case 1:

# base = 2
# exponent = 5

# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

# Case 2:

# base = 5
# exponent = 4

# 5 raises to the power of 4 is: 625 
# i.e. (5 *5 * 5 *5 = 625)

#Create a function called exponent(base,exp) that returns an int value of base raises to the power of exp
def exponent(base,exp):
    result = base**exp
    return result

#Create a variable for the given bases and exponents
base_1 = 2
base_2 = 5

exp_1 = 5
exp_2 = 4

#Call out the function and get the result
result_1 = exponent(base_1,exp_1)
result_2 = exponent(base_2,exp_2)

#Create a variable to display the long method of computation
long_result_1 = f"{base_1} *" * (exp_1 - 1)  + f"{base_1}"
long_result_2 = f"{base_2} *" * (exp_2 - 1) + f"{base_2}"

#Display the result with the long example

#Case 1
print("Case 1: \nbase =", base_1 ," \nexponent =", exp_1)
print(base_1, "raise to the power of", exp_1, ":", result_1)
print("i.e.", f"({long_result_1} = {result_1})")

#Case 2
print("\nCase 2:\nbase =", base_2 ," \nexponent =", exp_2)
print(base_2, "raise to the power of", exp_2, ":", result_2)
print("i.e.", f"({long_result_2} = {result_2})")