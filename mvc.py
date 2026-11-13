#best fit thing made for MVC 2026-27
import numpy as np #deadahh purpose built for ts
np.set_printoptions(precision=5, suppress=True) #sets the final displayed value

#------------------------------------------------------------------------------------------
#leftover debug stuff
# highest = 3

# x = np.array([0, 3, 9, 6, 12])
# y = np.array([1, 4, 2, 7, 12])

#------------------------------------------------------------------------------------------
#inputs along with some input checking logic
proceed = False

while True:
    try:
        highest = int(input("What typa best fit function (linear, quadratic, cubic, etc.): "))
        break
    except ValueError:
        print("Not a valid answer! Try again!")

while proceed == False:
    while True:
        try:
            x = np.array(list(map(float, input("Only x-values (space-separated): ").split())))
            break
        except ValueError:
            print("Invalid input! Try again!")

    while True:
        try:
            y = np.array(list(map(float, input("Only y-values (space-separated): ").split())))
            break
        except ValueError:
            print("Invalid input! Try again!")

    if y.size != x.size:
        proceed = False
        print("Number of x-values does not match number of y-values")
    else:
        proceed = True

#------------------------------------------------------------------------------------------
#calculating the left matrix
coeff_arr = np.zeros((highest + 1, highest + 1), float)

def summation_power(array, i, j):
    array = array**(i+j)
    total = array.sum()
    return total

for i in range(highest + 1):
    for j in range(highest + 1):
        coeff_arr[i, j] = summation_power(x, i, j)

#flipping it both ways since I use numpy index coordinates which start with (0, 0) in the top left when we consider the first term to be on the bottom right 
coeff_arr = np.flipud(coeff_arr)
coeff_arr = np.fliplr(coeff_arr)

#pretty self explanatory ngl
inverse_coeff_arr = np.linalg.inv(coeff_arr)

#------------------------------------------------------------------------------------------
#calculating the right matrix
result_arr = np.zeros((highest + 1, 1), dtype = float)

def x_summation_power(array_x, array_y, i):
    result_arr = (array_x**i)*(array_y)
    result_int = result_arr.sum()
    return result_int

for i in range(highest + 1):
    result_arr[i, 0] = x_summation_power(x, y, i)

#see above note
result_arr = np.flipud(result_arr)

#------------------------------------------------------------------------------------------
#matrix multiplication
#weirdly enough, flipping it again in the end makes the print statement logic easier
coefficients = np.flipud(inverse_coeff_arr @ result_arr)

for terms in range(highest + 1):
    print(f"a_{terms} = {coefficients[terms]}")