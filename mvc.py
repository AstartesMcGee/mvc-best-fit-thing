#best fit thing made for MVC 2026-27
import numpy as np #deadahh purpose built for ts
import tkinter as tk
from tkinter import filedialog

np.set_printoptions(precision=5, suppress=True) #sets the final displayed value
root = tk.Tk()
root.withdraw()

#------------------------------------------------------------------------------------------
#leftover debug stuff
# highest = 3

# x = np.array([0, 3, 9, 6, 12])
# y = np.array([1, 4, 2, 7, 12])

#------------------------------------------------------------------------------------------
#its a choice
print("File upload (F) or manual input (M)?")

while True:
    choice = input("F or M: ").strip().upper()

    if choice in ("F", "M"):
        break

    print("Invalid input! Please enter F or M.")

#------------------------------------------------------------------------------------------
#file upload option

if choice == "F":
    
    filename = filedialog.askopenfilename(
        title="Select your data file",
        filetypes=[("Text files", "*.txt")]
    )

    if filename:
        data = np.loadtxt(filename)

        x = data[:, 0]
        y = data[:, 1]

        print("File loaded successfully!")
    else:
        print("No file selected.")

    root.destroy()

    while True: #literally just copy pasted from below
        try:
            highest = int(input("Highest degree in your best fit polynomial: "))

            if highest >= 0:
                break
            print("Degree must be nonnegative!")

        except ValueError:
            print("Not a valid answer! Try again!")

#------------------------------------------------------------------------------------------
#inputs along with some input checking logic

if choice == "M":
    while True:
        while True:
            try:
                highest = int(input("What typa best fit function (linear, quadratic, cubic, etc.): "))

                if highest >= 0:
                    break
                print("Degree must be nonnegative!")

            except ValueError:
                print("Not a valid answer! Try again!")

        proceed = False

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
                print("Number of x-values does not match number of y-values")
            else:
                proceed = True

        if np.unique(x).size < highest + 1:
            print("Not enough distinct x-values for this polynomial degree!")
            continue
        break

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
coefficients = np.flipud(inverse_coeff_arr @ result_arr)

sum_arr = np.zeros(((x.size), 1), dtype=float)

print(coefficients)

def vert_squared(i):
    fy = coefficients[0]*(x[i]**0) + coefficients[1]*(x[i]**1) + coefficients[2]*(x[i]**2) + coefficients[3]*(x[i]**3) - y[i]

    fy = fy**2
    return fy

for i in range(x.size):
    sum_arr[i] = vert_squared(i)

total_answer=sum_arr.sum()

#------------------------------------------------------------------------------------------
#matrix multiplication
#weirdly enough, flipping it again in the end makes the print statement logic easier


print(f"The minimum sum of least squares is {total_answer}.")

for terms in range(highest + 1):
    print(f"a_{terms} = {coefficients[terms]}")
