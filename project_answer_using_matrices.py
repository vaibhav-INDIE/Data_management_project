list1 = ["matrices",["1", 0, 1, 0, 0, 0, 1], ["2", 1 ,0 ,1 ,1 ,0 ,0], ["3", 0,1,0,1,0,0],["4", 0,1,1,0,1,0],["5", 0,0,0,1,0,0], ["6", 1,0,0,0,0,0]]

s = str(input("Enter starting point "))
e = str(input("Enter ending point "))


# 0 steps

if int(s) != int(e) and list1[int(s)][int(e)] == 1:
    print(s,"-",e)

# 1 step

if int(s) != int(e) and list1[int(s)][int(e)] == 0:
    for i in range(1,6):
        if list1[i][int(s)] == 1 and list1[i][int(e)] == 1:
            print(s,"-",list1[i][0],"-",e)

if int(s) != int(e) and list1[int(s)][int(e)] == 1:
    for i in range(1,6):
        if list1[i][int(s)] == 1 and list1[i][int(e)] == 1:
            print(s,"-",list1[i][0],"-",e)



# 2 step

if int(s) != int(e) and list1[int(s)][int(e)] == 0:
    for i in range(1,6):
        if list1[i][int(s)] == 1:
            for j in range(1,6):
                if list1[j][int(e)] == 1 and list1[i][j] == 1 and s!=j :
                    print(s,"-",list1[i][0],"-",list1[j][0],"-",e)

# 3 step
if int(s) != int(e) and list1[int(s)][int(e)] == 0:
    for i in range(1,6):
        if list1[i][int(s)] == 1:
            for j in range(1,6):
                if list1[i][j] == 1:
                    for k in range(1,6):
                        if list1[j][k] == 1 and list1[k][int(e)] == 1 and s!=j and i!=k and j != int(e):
                            print(s,"-",list1[i][0],"-",list1[j][0],"-",list1[k][0],"-",e)

# 4 step

if int(s) != int(e) and list1[int(s)][int(e)] == 0:
    for i in range(1,6):
        if list1[i][int(s)] == 1:
            for j in range(1,6):
                if list1[i][j] == 1:
                    for k in range(1,6):
                        if list1[j][k] == 1:
                            for c in range(1,6):
                                if list1[c][k] == 1 and list1[c][int(e)] == 1 and int(s)!=j and i!=k and j != int(e) and i != int(e) and j!=c and i != c and k!=int(e):
                                    print(s,"-",list1[i][0],"-",list1[j][0],"-",list1[k][0],"-",list1[c][0],"-",e)



