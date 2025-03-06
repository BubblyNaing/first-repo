#---COUNTERTOP AREA CALCULATOR----
# This program calculates the area of a broken countertop, give
# /!\ 
# TODO: 
side_countertop = input("Enter the length of the side of the countertop")
side_countertop = float(side_countertop)
area_square = (side_countertop**2)  #Area of the square
area_broken_triangle = ((side_countertop/2)**2)/2
area_countertop = area_square - area_broken_triangle
print (area_countertop)
