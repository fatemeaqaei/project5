def ches(n, m):
    list1 = []
    sw = False
    for i in range(n):
        for j in range(m):
            if j % 2 == 0:
                if not sw:
                    list1.append("*")
                else : 
                    list1.append("#")
            else:
                if not sw:
                    list1.append("#")
                else:
                    list1.append("*")
        print("".join(list1))
        sw = not sw
        list1 = []


n = int(input("enter the number of rows: "))
m = int(input("enter the number of  colomns: "))
ches(n, m)