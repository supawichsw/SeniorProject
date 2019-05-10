import cholesky
def stiffnessmatrix(element,node,support,supportinfo):
    #หา existnode

    constrained=[]
    unconstrained=[]
    a=[]
    n=[]
    equation2 = {}
    numsupportforce=0

    degreefreedom = len(node) * 2
    g = (len(node) - len(support)) * 2
    z = len(node)
    L = [[0] * 2 for i in range(z)]
    k=0
    print(len(node),"len all node")
    for i in range(len(node)):
        if node[i] not in support:
            L[i][0] = k * 2
            L[i][1] = k * 2 + 1
            k = k + 1
    for x in range(len(support)):
        if supportinfo["type"][x] == 2:
            numsupportforce = numsupportforce + 1
            if supportinfo["constrained"][x] == "xr" or supportinfo["constrained"][x]=="xl":
                constrained.append((x, 0))
                unconstrained.append((x, 1))
            elif supportinfo["constrained"][x] == "y":
                unconstrained.append((x, 0))
                constrained.append((x, 1))
        elif supportinfo["type"][x] == 1:
            numsupportforce=numsupportforce+2
            constrained.append((x, 0))
            constrained.append((x, 1))
    for z, b in unconstrained:
        y = node.index(support[z])
        L[y][b] = g
        g = g + 1
    for j, r in constrained:
        y = node.index(support[j])
        L[y][r] = g
        g = g + 1

    print(L,"L")

    for x in range(degreefreedom):
        for i in range(degreefreedom):
            equation2.setdefault((x,i),[]).append(0)

    print(equation2,"equation2")
    for q in range(len(element)):
        print(q,"q")
        Nearendnode=element[q][0]
        Farendnode=element[q][1]

        Nx=L[Nearendnode][0]
        Ny=L[Nearendnode][1]
        Fx=L[Farendnode][0]
        Fy=L[Farendnode][1]

        X = node[Farendnode][0] - node[Nearendnode][0]
        Y = node[Farendnode][1] - node[Nearendnode][1]
        Magnitude = ((X * X) + (Y * Y)) ** 0.5
        lambdaX= X/Magnitude
        lambdaY=Y/Magnitude
        print(Fx,"Fx")
        print(Fy,"Fy")
        print(Nx,"Nx")
        print(Ny,"Ny")
        print(lambdaX,"lamdaX value")
        print(lambdaY,"lambdaY value" )
        print(Magnitude,"Magnitude value")
        equation2[(Nx,Nx)][-1]=equation2[(Nx,Nx)][-1]+(lambdaX**2)/Magnitude
        equation2[(Ny,Nx)][-1]=equation2[(Ny,Nx)][-1]+(lambdaX*lambdaY)/Magnitude
        equation2[(Fx,Nx)][-1]=equation2[(Fx,Nx)][-1]-(lambdaX**2)/Magnitude
        equation2[(Fy,Nx)][-1]=equation2[(Fy,Nx)][-1]-(lambdaX*lambdaY)/Magnitude
        equation2[(Nx,Ny)][-1]=equation2[(Nx,Ny)][-1]+(lambdaX*lambdaY)/Magnitude
        equation2[(Ny,Ny)][-1]=equation2[(Ny,Ny)][-1]+(lambdaY**2)/Magnitude
        equation2[(Fx,Ny)][-1]=equation2[(Fx,Ny)][-1]-(lambdaX*lambdaY)/Magnitude
        equation2[(Fy,Ny)][-1]=equation2[(Fy,Ny)][-1]-(lambdaY**2)/Magnitude
        equation2[(Nx,Fx)][-1]=equation2[(Nx,Fx)][-1]-(lambdaX**2)/Magnitude
        equation2[(Ny,Fx)][-1]=equation2[(Ny,Fx)][-1]-(lambdaX*lambdaY)/Magnitude
        equation2[(Fx,Fx)][-1]=equation2[(Fx,Fx)][-1]+(lambdaX**2)/Magnitude
        equation2[(Fy,Fx)][-1]=equation2[(Fy,Fx)][-1]+(lambdaX*lambdaY)/Magnitude
        equation2[(Nx,Fy)][-1]=equation2[(Nx,Fy)][-1]-(lambdaX*lambdaY)/Magnitude
        equation2[(Ny,Fy)][-1]=equation2[(Ny,Fy)][-1]-(lambdaY**2)/Magnitude
        equation2[(Fx,Fy)][-1]=equation2[(Fx,Fy)][-1]+(lambdaX*lambdaY)/Magnitude
        equation2[(Fy,Fy)][-1]=equation2[(Fy,Fy)][-1]+(lambdaY**2)/Magnitude

        #ตัดให้เหลือ K11 อิงจา่ก จำนวน reactionatsupport

    i=len(node)*2-numsupportforce

    for row in range(i):
        s=[]
        for column in range(i):
            s.append(equation2[row,column][-1])
        a.append(s)


    print(a,"a")
    result=cholesky.cholesky(a)
    return result


if __name__ == '__main__':
    #test hibbler554
    #element = ((0,1),(0,2))
    #allnode = ((0, 0),(3,0),(3,4))
    #support=((3,0),(3,4))
    #supportinfo={}
    #supportinfo.setdefault("type",[]).append(1)
    #supportinfo.setdefault("type",[]).append(1)

    #test hibbler558
    #allnode=((0,0),(0,3),(4,0),(4,3))
    #element=((0,3),(1,3),(2,3))
    #support=((0,0),(0,3),(4,0))
    #supportinfo = {}
    #supportinfo.setdefault("type",[]).append(1)
    #supportinfo.setdefault("type",[]).append(1)
    #supportinfo.setdefault("type",[]).append(1)

    #test hibbler pg.577
    #allnode=((0,0),(0,10),(10,0),(10,10))
    #element=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
    #support=((10,0),(10,10))
    #supportinfo={}
    #supportinfo.setdefault("type",[]).append(2)
    #supportinfo.setdefault("type",[]).append(1)
    #supportinfo.setdefault("constrained",[]).append("x")
    #supportinfo.setdefault("constrained",[]).append(0)
    #a=stiffnessmatrix(element,allnode,support,supportinfo)


    #allnode=[(0,0),(0,3),(3,0),(3,3)]
    #element=[(0,1),(0,2),(1,3),(2,3)]
    #support=[(0,0),(3,0)]
    #supportinfo={}
    #supportinfo.setdefault("type",[]).append(1)
    #supportinfo.setdefault("type",[]).append(2)
    #supportinfo.setdefault("constrained",[]).append(0)
    #supportinfo.setdefault("constrained",[]).append("y")
    #a=stiffnessmatrix(element,allnode,support,supportinfo)

    allnode=[(0,0),(1,1),(2,0)]
    element=[(0,1),(0,2)]
    support=[(0,0),(2,0)]
    supportinfo={}
    supportinfo.setdefault("type",[]).append(1)
    supportinfo.setdefault("type",[]).append(2)
    supportinfo.setdefault("constrained",[]).append("y")
    supportinfo.setdefault("constrained", []).append("y")
    a = stiffnessmatrix(element, allnode, support, supportinfo)


























