
n = str(input("Enter Starting Point: "))
e = str(input("Enter ending Point: "))




routes = {"1" : ["2", "6"], "2": ["1", "3", "4"], "3": ["2", "4"], "4": ["3", "5","2"], "5": ["4"], "6": ["1"]}




if e in routes[n] and e != n:
    print(n,"-",e)
    for i in routes[n]:
        if e in routes[i]:
            print(n,"-",i,"-",e)
        
            
if e not in routes[n] and e != n:
    for i in routes[n]:
        if e in routes[i]:
            print(n,"-",i,"-",e)

if e not in routes[n] and e != n:
    for i in routes[n]:
        if e not in routes[i]:
            for j in routes[i]:
                if e in routes[j] and j != n:
                    print(n,"-",i,"-",j,"-",e)

if e not in routes[n] and e != n:
    for i in routes[n]:
        if e in routes[i]:
            for j in routes[i]:
                if e in routes[j] and j != n:
                    print(n,"-",i,"-",j,"-",e)


if e not in routes[n] and e != n:
    for i in routes[n]:
        if e not in routes[i]:
            for j in routes[i]:
                if e not in routes[j]:
                    for k in routes[j]:
                        if e in routes[k] and j != n:
                            print(n,"-",i,"-",j,"-",k,"-",e)

if e not in routes[n] and e != n:
    for i in routes[n]:
        if e not in routes[i]:
            for j in routes[i]:
                if e in routes[j]:
                    for k in routes[j]:
                        if e in routes[k] and j != n:
                            print(n,"-",i,"-",j,"-",k,"-",e)






if n == "5" and e == "6" :
    print(5,"-",4,"-",3,"-",2,"-",1,"-",6)

if n == "6"  and e == "5" :
    print(6,"-",1,"-",2,"-",3,"-",4,"-",5)



if e == n:
    print("Starting point and ending point can't be same")