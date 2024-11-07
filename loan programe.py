hincome=float(input())
wincome=float(input())
hage=int(input())
wage=int(input())
if(hincome<=1,00,000):
    if(wincome<=50,000):
        if(hage<=30):
            if(wage<=25):
                print("loan approved")
            else:
                print("loan decelared due to wife age")
        else:
            print("loan decelared due to husband age")
    else:
        print("loan decelared due to wife income")
else:
    print("loan decelared due to husband income")
