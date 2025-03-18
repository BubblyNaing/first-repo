#global variables
miles = 20
feet = 20
inches = 100

def distance_convertor(miles,yards,feet):
    return miles*5280*12 + yards*36 + feet * 12
    

def main ():
    miles = float (input('Enter the miles'))