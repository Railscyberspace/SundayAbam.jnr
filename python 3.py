import random
import string

letters = string.ascii_lowercase
# Create an empty dictionary
employee_data = {}

while True:
    # prompt employee for first name, last name and email
    first_name = input('First name : ')
    last_name = input('Last name: ')
    email = input('Email: ')
# Generate password by appending first 2 letters of first name and last 2 letters of last with random string of length 5
    initials = f"{first_name[0:2]}{last_name[-2:]}"
    password = f"{initials}{(''.join(random.choice(letters) for i in range(5)))}"
    print(f"Password: {password}")
    # Ask if employee is satisfied with the generated password
    is_satisfied = input('Do you like the generates password,if yes enter yes if no,enter No supply your password')
      

    if password_satified == "Yes":
        employee_details = {
            "First name": first_name,
            "Last name": last_name,
            "Email": email,
            "Password": password
        }
        print(f"employee{employee_details}")
        break
    else:
        print("Kindly enter desired password below")
        desired_password = input('Desired_password: ')
        print(f"Desired password:{desired_password}")

    if len(desired_password) >= 7:
        employee_details = {
            "First name": first_name,
            "Last name": last_name,
            "Email": email,
            "Password": desired_password
            }
        print(f"employee{employee_details}")
    else:
        print("Password must be more than 7 characters")
        desired_password = input('Desired_password: ')
        print("Password is good")
        employee_details = {
            "First name": first_name,
            "Last name": last_name,
            "Email": email,
            "Password": desired_password
        }
        print(f"employee {employee_details}")
else:
    repeat = input(f"Do you still have another user:[yes/no] ")

     if  (new_user =="no"):
         return False

         for item container:
             print(item)

else:

       return True
       
       return details


     }
   
    
        
        




