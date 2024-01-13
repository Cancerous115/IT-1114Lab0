# Program Name: Lab1.py
# Course: IT1114/Section 01
# Student Name: Garrett Cook
# Assignment Number: Lab1
# Due Date: 05/26/2024
# Purpose: Write a Python program that will calculate the amount and cost of purchasing flooring.
# Calculate the total square feet, flooring cost, tax (7%) and total amount due.


length = input("Room Length:")
length = float(length)
width = input("Room Width:")
width = float(width)
CostSq = input("Cost per Sq.Foot:")
CostSq = float(CostSq)

# Flooring would be the CostSq * total SqFt = "length * width")
# So we made a new variable for total SqFt.
SqFt = length*width
print("Square feet:", SqFt)
# We made another variable for flooring
Floor = SqFt * CostSq
print("Flooring:", Floor)

# Tax is 7%, so we just multiply total flooring by 0.07
Tax = Floor * 0.07
print("Tax:", Tax)
# Finally we make a variable for Total that's just us adding the tax with the flooring cost.
Total = Tax + Floor
print("Total:", Total)