
def overlap2(nodetable,elementtable,support):
    p=0


    ppp=[]
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
                print("yes1")

                l.append(i)
                l.append(j)
            elif yi==yj:
                print("yes2")
                y.append(i)
                y.append(j)
            else:
                slope = (yj - yi) / (xj - xi)
                xy.setdefault((slope),[]).append((i,j))
                print(slope,"slope")
                print("yes3")


        m=list(xy.values())
        print(m,"mmmm")
        if len(m)!=0:
            for i in range(len(m)):
                print(len(m[i]),"len miii")
                if(len(m[i])>=2):
                    for j in range(len(m[i])):
                        lxy.append(m[i][j][0])
                        lxy.append(m[i][j][1])

        l=list(set(l))
        l.sort()
        print(l,"lll")
        revisedelement(l,elementtable,ppp,support,nodetable)
        y=list(set(y))
        y.sort()
        print(y,"y")
        revisedelement(y,elementtable,ppp,support,nodetable)
        #print(b,"this is b")
        lxy=list(set(lxy))
        lxy.sort()
        print(lxy,"lxy")
        c,pp=revisedelement(lxy,elementtable,ppp,support,nodetable)
    print(c,"sadklsa;kd;lsakdls;akdl;sakdl;sakdl;sakdla;s'")
    ppp=ppp+pp
    ppp=list(set(ppp))
    print(ppp,"askdlsa;kdsal;dksal;kds;lakdl;askdl;sakdl;sakdl;aksd;as'")
    return c,pp


def revisedelement(l,elementtable,ppp,support,nodetable):
        o=[]
        print(l,"this is l mtherfuckerrr")
        revisedelementtable=elementtable
        pp=ppp

        z=[]
        s=[]

        p=[]
        if len(l)>2 :


            print(l)


            for j in l:

                for k in range(len(elementtable)):
                    if elementtable[k][0]<=j<=elementtable[k][1] and elementtable[k][0] in l and elementtable[k][1] in l:
                        p.append(j)

            p=list(set(p))
            p.sort()
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
            print(o, "d")
            for i in range(0,len(o)-1):
                print(o[i], "oi")
                print(i,"i")
                revisedelementtable.append((o[i],o[i+1]))


            s=list(set(s))
            print(s,"ssss")
            for k in range(len(s)):
                revisedelementtable.remove(s[k])
            for number in p:
                found = False
                for tup in revisedelementtable:
                    if number in tup:
                        found = True
                if found == False:
                    pp.append(number)
        pp = list(set(pp))

        revisedelementtable=list(set(revisedelementtable))
        revisedelementtable.sort()

        print(revisedelementtable,"final elementtable")
        return revisedelementtable,pp











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

