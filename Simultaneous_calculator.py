while True:
    try:
        first_variable = float(input("First Variable: "))
        second_variable = float(input("Second variable: "))
        equal_to = float(input("Equal value: "))
        break
        
    except ValueError:
        print("Enter numbers only!")
        
        
while True:
    try:
        first_variable_B = float(input("First Variable_B: "))
        second_variable_B = float(input("Second variable_B: "))
        equal_to_B = float(input("Equal value_B: "))
        break
        
    except ValueError:
        print("Enter numbers only!!")
        
print(" ")

equation_1= str(first_variable) + "x " + str(second_variable) + "y" + " = " + str(equal_to)
print("EQU1 = " + equation_1)

print(" ")

equation_2 = str(first_variable_B) + "x " + str(second_variable_B) + "y" + " = " + str(equal_to_B) 
print("EQU2 = " + equation_2)

while True:
    print(" ")

    continue_prompt = input("Do you want to continue?(yes/no): ")

    clean_continue_prompt = continue_prompt.strip().lower()

    if clean_continue_prompt == "yes":
        try:
            D = (first_variable * second_variable_B) - (second_variable * first_variable_B)
            

    

            Dx = (equal_to * second_variable_B) -(second_variable * equal_to_B)
    

            Dy = (first_variable * equal_to_B) -(equal_to * first_variable_B)
    
            x = Dx / D
            y = Dy / D
    



            print("Solution:")
            print("x = " + str(x))
            print("y = " + str(y))
            break
        except ZeroDivisionError:
            print("No unique solution exists (lines are parallel).")                    
       
    elif clean_continue_prompt == "no":
        print("Ended")
        break
        
    else:
        print("choose again")
    
