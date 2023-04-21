import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

#service account credentials
cred = credentials.Certificate("C:\\Users\\singh\\Downloads\\f.auth.json")

#initializing the app
firebase_admin.initialize_app(cred)

cred = credentials.Certificate("C:\\Users\\singh\\Downloads\\f.auth.json")

#creating the user
email = input('Please enter your email address : ')
password = input("Please enter your password : ")
user = auth.create_user(email = "singhalmilan92@gmail.com", password = "Mi@03122004", phone_number = "+91 9680222741")
print("User created successfully : {0}",format(user.uid))

#get the user
email = 'singhalmilan92@gmail.com'
phone = "9680222741"
user = auth.get_user_by_email(email)
by_phone = auth.get_user_by_phone_number(phone)
print("User id is : {0} ",format(user.uid))
print("User id is : {0} ",format(by_phone.uid))

#list all the users
page = auth.list_users()
while page:
    for user in page.users:
        print("User : " + user.uid)
        
# get next page
    page = page.get_next_page()

#create user by id
email = input('Please enter your email address : ')
password = input("Please enter your password : ")
id = input("Please enter the id : ")
user = auth.create_user(uid = id, email = email, password = password)
print("Successfully created new user : {0} ".format(user.uid))

#creating password reset link
email = input("Please enter your email address : ")
link = auth.generate_password_reset_link(email, action_code_settings=None)
print(link)

#creating email verification link
email = input("Please enter your email address : ")
link = auth.generate_email_verification_link(email, action_code_settings=None)
print(link)
