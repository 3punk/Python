import time
import requests

delay01 = 3
delay02 = 4
delay03 = 6
delay04 = 2

print ("Hello!")
time.sleep(delay01)
print ("My name is Jarvis.")
time.sleep(delay01)
print ("May I help you?")
time.sleep(delay02)
print ("Me : Login Data")
time.sleep (delay02)
print ("Please wait for a moment...")
time.sleep (delay01)
name = input ("Username : ")
if name == 'Evan':
    pwd= input ("Welcome back, Evan. Please input the password : ")
    if pwd == 'codegeass':
        print ("Please wait for a moment...")
        time.sleep (delay03)
        print ("Confirming password")
        time.sleep (delay01)
        print ("Checking validation")
        time.sleep (delay01)
        print ("Wait for a moment...")
        time.sleep(delay02)
        print ("Accepted. Enjoy the journey at here," +name)
    else:
        print ("Is that you? Try to input the correct password..." )
else:
    print ("You look kinda sus...")
