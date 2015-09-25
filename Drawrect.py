
for i in range(int(input())) :
    xr = []
    yr = []
    a = input()
    x,y = a.split()
    x = int(x)
    y = int(y)
    xr.append(x)
    yr.append(y)

    b = input()
    x,y = b.split()
    x = int(x)
    y = int(y)
    xr.append(x)
    yr.append(y)

    c = input()
    x,y = c.split()
    x = int(x)
    y = int(y)
    xr.append(x)
    yr.append(y)

    xr.append(1) # x[3] 요소를 넣어둬야 값 변경이 가능해서 넣어둠
    yr.append(1) # y[3] 요소를 넣어둬야 값 변경이 가능해서 넣어둠

    if xr[0]^xr[1]==0:
        xr[3]=xr[2]
    elif xr[0]^xr[2]==0:
        xr[3]=xr[1]
    else : xr[3]=xr[0]

    if yr[0]^yr[1]==0:
        yr[3]=yr[2]
    elif yr[0]^yr[2]==0:
        yr[3]=yr[1]
    else : yr[3]=yr[0]

    xr[3]=str(xr[3])
    yr[3]=str(yr[3])
    result = xr[3] + ' ' +  yr[3]
    print(result)
