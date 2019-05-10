
def overlap2(nodetable,elementtable,support):
    p=0
    numnode=len(nodetable)
    nodetable=list(set(nodetable))
    nodetable.sort()

    for i in range(numnode):

        xy={}
        print(i,"i")
        lxy=[]
        y=[]
        l=[]
        xi=nodetable[i][0]
        yi=nodetable[i][1]
        p=p+1

        for j in range(p,numnode):
            print(j,"j")
            xj=nodetable[j][0]
            yj=nodetable[j][1]
            if xi==xj:
                print("equal in x axis")
                l.append(i)
                l.append(j)
            elif yi==yj:
                print("equal in y axis")
                y.append(i)
                y.append(j)
            else:
                slope = (yj - yi) / (xj - xi)
                xy.setdefault((slope),[]).append((i,j))



        #combined adjacent elements which have the same slope
        m=list(xy.values())
        if len(m)!=0:
            for i in range(len(m)):
                if(len(m[i])>=2):
                    for j in range(len(m[i])):
                        lxy.append(m[i][j][0])
                        lxy.append(m[i][j][1])

        l=list(set(l))
        l.sort()
        print(l,"l")
        revisedelement(l,elementtable,support,nodetable)
        y=list(set(y))
        y.sort()
        print(y,"y")
        revisedelement(y,elementtable,support,nodetable)
        lxy=list(set(lxy))
        lxy.sort()
        print(lxy,"lxy")
        c=revisedelement(lxy,elementtable,support,nodetable)
    return c


def revisedelement(l,elementtable,support,nodetable):
        o=[]
        revisedelementtable=elementtable
        s=[]
        p=[]
        if len(l)>2 :


            print(l)


            for j in l:
                for k in range(len(elementtable)):
                    if len(p)==2:
                        if elementtable[k][0] in l and elementtable[k][1] in l and elementtable[k][0]<=p[-1]:
                            p.append(elementtable[k][0])
                            p.append(elementtable[k][1])
                            p = list(set(p))
                            p.sort()
                        elif p[0]<=j<=p[-1]:
                            p.append(j)
                            p=list(set(p))
                            p.sort()
                    elif j == elementtable[k][0] and elementtable[k][1] in l:
                        p.append(j)
                        p.append(elementtable[k][1])
            print(p)
            for i in range(1,len(p)-1):
                 if nodetable[p[i]] in support:
                     o.append(p[i])
                     print(p[i],"this is  support location ,cannot be removed")
                 for j in range(len(elementtable)):
                    if elementtable[j][0] in p and elementtable[j][1] in p:
                        o.append(p[0])
                        o.append(p[-1])
                        s.append(elementtable[j])
                        print(elementtable[j], "this is in")

                    elif elementtable[j][0] != p[i] and elementtable[j][1]  == p[i]:
                        print(elementtable[j][1], "this is not in due to elementtable[j][1]")
                        o.append(elementtable[j][1])

                    elif elementtable[j][0] == p[i] and elementtable[j][1] != p[i]:
                        print(elementtable[j][0], "this is not in due to elementtable[j][0]")
                        o.append(elementtable[j][0])
            o=list(set(o))
            o.sort()
            for i in range(0,len(o)-1):

                revisedelementtable.append((o[i],o[i+1]))

            s=list(set(s))
            for k in range(len(s)):
                revisedelementtable.remove(s[k])

        revisedelementtable=list(set(revisedelementtable))
        revisedelementtable.sort()

        print(revisedelementtable,"final elementtable")
        return revisedelementtable











if __name__ == '__main__':
    #nodetable=[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
    #elementtable=[(0, 1), (0, 3), (0, 4), (0, 5), (1, 4), (3, 4), (4, 5)]
    support=[(0,1),(1,1)]
    #nodetable=[(0,0),(0,2),(1,1),(2,2)]
    #support=[(0,1)]
    #elementtable=[(0,3),(1,2)]
    #nodetable=[(0, 0), (0, 1), (0, 2), (1, 1), (1, 2)]
    #elementtable=[(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)]
    #nodetable=[(0,0),(1,0),(1,1),(1,2)]
    #elementtable=[(0,3)]
    #nodetable=((1,0),(1,2),(0,0),(1,1))
    #elementtable=[(0,1),(0,2),(1,3)]
    #nodetable=((0,1),(0,2),(0,3))
    #elementtable=[(0,1),(1,2)]
    nodetable=[(0,1),(0,2),(0,3),(1,1),(2,2),(3,1),(3,3),(4,1)]
    elementtable=[(0,1),(1,2),(0,5)]
    #nodetable=((0,1),(0,2),(0,3),(0,4),(1,0),(2,1),(3,1))
    #elementtable=[(0,1),(0,5),(0,6),(1,2),(1,3),(1,4),(2,5)]
    #nodetable=((0,1),(0,2),(0,3),(2,1),(3,1))
    #elementtable=[(0,1),(0,2),(0,3),(0,4),(1,2),(1,3)]
    #nodetable=((0,1),(0,2),(0,3),(0,4),(1,0),(2,1),(3,1))
    #elementtable=[(0,1),(1,2),(0,3),(0,5),(0,6),(1,4),(2,5),]
    #nodetable = ((0, 1), (0, 2), (0, 3),(0,4), (1, 0), (2, 0), (3, 0), (3, 3),(4,3),(4,4))
    #nodetable = ((0, 1), (0, 2), (0, 3),(1,1),(1,4),(2,2),(3,3))
    #elementtable=[(0,1),(1,2),(2,3),(3,4),(4,5)]
    #elementtable=[(0,1),(0,2),(0,3),(1,3),(4,5),(5,6),(6,7)]
    overlap2(nodetable,elementtable,support)

