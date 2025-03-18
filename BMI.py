weight_kg = float (input("Enter your weight in kg"))
height_m = float (input("Enter your height in meter"))
BMI = (weight_kg)/(height_m**2)
print("Your BMI is" + str("{:.3f}".format(BMI)))

#Function definition
def bmi(w,h):
    return (w)/(h**2)

#main is to use the function defined above.
def main ():
    your_w = float (input('Enter your weight in lbs'))
    your_h = float (input('Enter your height in meters'))
    your_w = your_w/2.205

    your_bmi = float(bmi(your_w,your_h))
    print ('Your BMI is'+ '{:.3f}'.format(your_bmi))

main ()


