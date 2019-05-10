#หาเฉพาะตัวที่ unstable เพราะ stable groupller มันไม่ชัวร์ ต้องใช้ cholesky แทน

import StiffnessM

def determinancycheck(element,node,support,supportinfo,supportreact):

        #print(numelement)
    allnode=node+support
    allnode.sort()
    print(allnode,"all")
    numelement=len(element)
    numallnode=len(allnode)
    numunknow=supportreact+numelement
    print("start check determinancy")
    print()
    print(numunknow,"unknow")
    if 2*numallnode>numunknow:
        l="unstable"
    else:
        print("check parallel and concurrent")
        print(allnode,"allnode")
        l=StiffnessM.stiffnessmatrix(element, allnode, support, supportinfo)
        #check parallel and concurrent
    return l



if __name__ == '__main__':
    node = [(1,1)]
    element = ((0, 1), (0,2), (1,2))
    support = [(0, 0), (2,0)]

    supportinfo={}
    supportinfo.setdefault("type", []).append(2)
    supportinfo.setdefault("constrained", []).append("y")
    supportinfo.setdefault("type", []).append(2)
    supportinfo.setdefault("constrained", []).append("y")

    sumreact=3
    #print(support)
    a=determinancycheck(element,node,support,supportinfo,sumreact)
    print(a,"aaaaa")
