import time
while True:
 username=input("Enter your username:").lower()
 password=input("Enter your password:")
 if username=="shadow" and password=="@shadow123":
    time.sleep(2)
    print("Access Granted ✅")
    break

 else:
    if username=="shadow":
        time.sleep(2)
        print("Right Username ✅")    
    else:
        time.sleep(2)
        print("Wrong Username ❌") 

    if password=="@shadow123":
            time.sleep(2)
            print("Right Password ✅")    
    else:
            time.sleep(2)
            print("Wrong Password ❌")      
    print("Not Access Granted ❌")