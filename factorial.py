def factorial(num):
    # Take a number and output the factorial of it.
    # Create some sort of deincrementer that consistenly takes -1 and multiplies it by the existing
    # Use while loop to go through a known number
    if num == 0:
        return 1
    newProduct = num
    i = num
    while i > 1:
        newProduct *= (i - 1)
        i -= 1
    return newProduct
