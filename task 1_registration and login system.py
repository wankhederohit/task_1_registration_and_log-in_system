import csv
import re
valid_email = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
valid_password= re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,}$')

def check_password(password):
    if len(password) < 16 and len(password) > 5 and re.fullmatch(valid_password, password):
        return True
    else:
        return False

def check_email(email):
    if re.fullmatch(valid_email, email):
        return True
    else:
        return False

def register():
    email = input('please enter your email: ')
    if check_email(email):
        password = input('please enter your password: ')
        if check_password(password):
            write_to_file(email,password)
            print('User Registered Sucessfully')
        else:
            print('Invalid password,please try again')

    else:
        print('Invalid email-id,please try again')

def login():
    email = input('please enter email-id:')
    if check_email(email):
        password = input('please enter your password: ')
        if check_password(password):
            if check_email(email):
                print('User Logged In Sucessfully')
            else:
                print('user not found')
                register()
        else:
            print('Invalid password,please try again')
    else:
        print('Invalid email-id,please try again')

def forgot_password():
    email = input('please enter email-id:')
    if check_email(email):
        if search_password(email):
            print('here is your password')
        else:
            print('user not found')
    else:
        print('invalid user name')

def search_password(email):
    with open('new_file.csv','r') as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if row[0] == email:
                print(row[1])
                return True
        return False


def write_to_file(email,password, mode='a',newline=''):
    with open('new_file.csv','a') as data_file:
        writer = csv.writer(data_file)
        writer.writerow([email,password])


def main():
    while True:
        print(''' Please select an option 
                1. Register
                2. Login
                3. Forget Password
                ''')

        user_choice = int(input('enter your choice: '))
        if user_choice == 1:
            register()
        elif user_choice ==2:
            login()
        elif user_choice ==3:
            forgot_password()

        else:
            print('invalid option')
            break


main()

