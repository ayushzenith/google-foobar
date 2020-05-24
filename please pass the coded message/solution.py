def solution(l):
    l.sort(reverse = True)
    if sum(l) % 3 == 0:
        return int("".join(map(str,l)))
    else:
        imslow = False
        for i in l:
            if i%3 == 0:
                imslow = True
        if imslow == False:
            return 0
        temp = l[:]
        while 3 in temp: temp.remove(3)
        while 6 in temp: temp.remove(6)
        while 9 in temp: temp.remove(9)
        sum1 = sum(temp)
        x = int(sum1/3) * 3
        z = sum1 - x
        zz = z+3
        zzz = zz+3
        if z in temp and z <= sum1:
            l.remove(z)
            return int("".join(map(str,l)))
        elif zz in temp and zz <= sum1:
            l.remove(zz)
            return int("".join(map(str,l)))
        elif zzz in temp and zzz <= sum1:
            l.remove(zzz)
            return int("".join(map(str,l)))
        elif sum1 in temp:
            l.remove(sum1)
            return int("".join(map(str,l)))
        else:
            testing = False
            for i in range(len(temp)):
                if testing:
                    break
                for j in range(len(temp)): 
                    if(i != j):
                        if(temp[i]+temp[j]==z or temp[i]+temp[j]==zz or temp[i]+temp[j]==zzz):
                            testing = True
                            l.remove(temp[i])
                            l.remove(temp[j])
                            break
            if testing:
                return int("".join(map(str,l)))    
            else:
                for i in temp:
                    l.remove(i)
                return int("".join(map(str,l)))
