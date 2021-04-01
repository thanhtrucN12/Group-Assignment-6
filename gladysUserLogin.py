import io
"""
Student: Nhi Tran
Module: gladysUserLogin
Description: This module checks if the usernameis a valid emailaddress or not and logs the user in.
"""
def login(email_address):
    while"@"notinemail_address:
        email_address =input("User login is not anemail address. ")
        if"."notinemail_address:
            email_address =input("User login is notan email address. ")
        if"com"notinemail_address:
            email_address =input("User login is notan email address. ")
        returnemail_address

login(input("Username: "))
password =input("Password: ")

