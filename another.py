
def changeelement(node,element):
    pp = []
    for i in range(len(node)):
        print(i, "i")
        for j in element:
            if i in j:
                break
        else:
            pp.append(i)
    removednode=[]
    zw=[]
    element2=[]
    for x, y in element:
        print(node[x])
        z = node[x]
        w = node[y]
        zw.append((z,w))
    print(zw,"zw")
    for j in pp:
        removednode.append(node[j])
    for  i in  removednode:
        node.remove(i)
    for z,w in zw:
        index1=node.index(z)
        index2=node.index(w)
        element2.append((index1,index2))
    print(node,"new node")
    print(element2,"new element")
    return node,element2


if __name__ == '__main__':
    allnode = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
    node= [ (0, 1), (1, 0), (2, 0), (2, 1)]
    support =[(0,0),(1,1)]
    element = [(0, 1), (0, 3), (0, 4), (0, 5), (1, 4), (3, 4), (4, 5)]
    pp = [2]
    allnode,element=changeelement(allnode,element)
    print(allnode,"askdlsa;kdlsa;kd;aslkd;lsa'")
    for i in node:
        if i not in allnode:
            print(i,"iiiiiii")
            node.remove(i)
    print(node,"nodeejaokdfjsa;fjaskd;fja")