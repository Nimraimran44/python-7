#1. Calculate age based on current year and birth year
current_year = 2024
birth_year = 2002
Age=current_year - birth_year
print("My age is ",Age)

 #2. Calculate area of a rectangle
length = 5
width = 3
area = length * width
print("The area of the rectangle is",area)

 #3. Calculate area of a circle
import math
radius = 4 
area = math.pi*(radius**2)
print("The area of the circle is" ,area)

 # 4. Calculate area of a cube (note a cube has 6 equal square faces)
side_length = 4
area = 6*(side_length **2)
print("The surface area of the cube is" ,area)
#5. Convert temperature from Fahrenheit to celsius and vice versa
def convert_temperature(temp, from_unit, to_unit):
    if from_unit =="F" and to_unit == "C":
        return(temp - 32) * 5/9
    elif from_unit == "C" and to_unit =="F":
        return(temp * 9/5) + 32
    else: 
        return "Invalid units"
fahrenheit = 100
celsius = convert_temperature(fahrenheit, "F" , "C")
print(f"{fahrenheit}F is equal to {celsius}C") 
celsius = 37.5
fahrenheit = convert_temperature(celsius, "C" , "F")
print(f"{celsius} C is equal to {fahrenheit} F")

 #6. Convert seconds to minutes and seconds 
total_seconds = 120
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds}seconds")

 #7. Calculate percentage
def calculate_percentage(part,whole):
    return(part/whole) * 100
part = 25
whole = 100
percentage = calculate_percentage(part,whole)
print(f"{part} is {percentage}% of {whole}")

 #8. BMI Calculator 
weight = 58
height = 1.52
bmi = weight / (height ** 2) 
print("Weight:" , weight, "kg")
print("Height:" , height, "m")
print("BMI:" , round(bmi,2))

 #9. Cylinder Volume Calculator
import math
radius = 5
height = 10 
volume = math.pi (radius ** 2) *height
print("Radius:" , radius)
print("Height:" , height)
print("Volume:" , round(volume, 2))