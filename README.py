import time
print ("Hello, Welcome to Zach's Project.")
print ("Today's date and time is,")
print (time.strftime("%H:%M:%S"))
username = 0
password = 0
while username != "zach" and password != "zach":

 username = input("Please enter your username.")
 password = input("Please enter your pasword.")


print ("Welcome to my project")
print ("Please select an option")
print ("1 Open a new python file")
option = int(input("..."))
if option == 1:
    
