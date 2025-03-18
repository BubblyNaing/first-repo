def compute_tuition_fee (nb_credits):
    if nb_credits>= 12:
        return 5000  #full tuition
    
    else:   #if you delete this line and the below return is not indented, it is exactly the same but not recommended to use
        return 600*nb_credits #part_time
    
def main():
    nb_credits =13
    fee, status = compute_tuition_fee(nb_credits)
    print(f"you have to pay ${fee}")
    print(f"and you are a {status} student")

main()