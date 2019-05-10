import random
import another
import overlap
import numpy as np
import Stability
import Image
import StiffnessM

from scipy.stats import truncnorm

class rectangle:

    unstabledata=0
    stabledata=0
    sumreactionsupport=0
    false=True
    supportinfo = {}
    support = []
    numelement = {}
    elementmore = []
    needmore = []
    choosen = 0
    elementatnode = {}
    elementnotneed = []
    elementtable = [(0,1),(2,4)]
    supporttable = []
    numsupport = 0
    elementnotchoosen = []
    type = 0
    def __init__(self, numgridx, numgridy,time):


        # user interface : type of support and location

        if numgridx <= 0:
            self.gridx = 1
            print("must greater than 0 ok1")
        if numgridx > 0:
            self.gridx = numgridx
            print("ok2")
        if numgridy <= 0:
            self.numgridy = 1
            print("ok3")
        if numgridy > 0:
            self.gridy = numgridy
            print("ok4")

        while self.numsupport < 2 :
            numstrsupport = input("number of support: ")
            self.numsupport = int(numstrsupport)
        if self.numsupport >= 2:
            print("ok number of support", self.numsupport)

            for i in range(self.numsupport):
                while self.type != 1 or self.type != 2:
                    type2 = input("Which type of support Pinned[1],Roller[2]: ")
                    self.type = int(type2)
                    print(self.type)
                    if self.type == 1 or self.type == 2:
                        self.supportinfo.setdefault("type", []).append(self.type)

                        xstr = input("location in directrion x: ")
                        ystr = input("location in direction y: ")
                        x = int(xstr)
                        y = int(ystr)
                        if self.type == 2:
                            constraint = input("which is constrained displacement (xr or xl or y): ")
                            self.supportinfo.setdefault("constrained", []).append(constraint)
                            self.sumreactionsupport=self.sumreactionsupport+1
                        elif self.type == 1:
                            axis=input("which is axis of support(xr or xl or y): ")
                            self.supportinfo.setdefault("constrained", []).append(axis)
                            self.sumreactionsupport=self.sumreactionsupport+2
                        if x >= 0 and y >= 0:
                            print("ok,the location is: ", x, ",", y)
                            # self.supporttable.append([x,y])
                            self.support.append((x, y))

                            break
        print(self.gridx, "numner of gridx")
        print(self.gridy, "number of gridy")

        for r in range(time):
            nodetable=[]
            elementtable=[]
            sum=0
            indexsupport=[]
            jj2=[]
            for i in range(self.gridx):
                for j in range(self.gridy):
                    randnum = random.randint(0,1)
                    if randnum == 1:

                        if (i, j) in self.support:
                            print("support location already")
                        else:
                            node = (i, j)
                            nodetable.append(node)

            print(nodetable, " node selected")

            self.support.sort()
            allnode = nodetable + self.support
            allnode.sort()
            print(allnode, "allnode")
            numallnode = len(allnode)

            for i in reversed(range(numallnode)):
                sum =sum + i

            print(sum, "summ")
            upper=sum
            lower=len(self.support)-1
            mean=2*numallnode-self.sumreactionsupport-0.5
            print(mean, "meannnnnnnn1111")
            if mean<=lower:
                mean=lower
            if mean==upper and mean ==lower:
                element=mean
            if mean>=lower and mean<upper:
                sd=1.5
                element=truncnorm((lower - mean) / sd, (upper - mean) / sd, loc=mean, scale=sd)
                element=element.rvs(1)
                element=round(element[-1])
                element=int(element)
            print(mean, "meannnnnnnn")
            print(element,"element after random")

            for j in self.support:
                indexsupport.append(allnode.index(j))
            print(indexsupport, "indexsupport")

            false = True
            while (false):
                numelement=0
                jj = indexsupport
                found=0
                elementtable=[]
                print(jj,"self jj")
                checker=True
                while (checker):
                    if len(jj)==0 :
                        print("done")
                        checker=False
                    for a in jj:
                        x=a+1
                        for j in range(x, len(allnode)):
                            randnum=random.randint(0,1)
                            if randnum==1 and (a,j) not in elementtable:
                                elementtable.append((a,j))
                                jj2.append(j)
                                numelement = len(elementtable)
                                if numelement == element:
                                    jj2=[]
                                    break
                        else:
                            continue
                        break
                    print(element,"and",numelement)
                    print(allnode,"all fucking node")
                    print(self.sumreactionsupport,"summreaction")
                    print(sum,"summm")
                    print(mean,"meannn")
                    jj = jj2
                    jj = list(set(jj))
                    jj2 = []
                    print(jj,"self.jj")

                for i in indexsupport:
                    for k in elementtable:
                        if i in k:
                            found=found+1
                            break

                if found==len(self.support) and numelement==element :
                    false=False
                else :
                    false=True

            print(elementtable, "first elementtable")

            elementtable.sort()
            print(elementtable,"before check overlap")
            elementtable=overlap.overlap2(allnode,elementtable,self.support)
            print(elementtable,"after overlap checking , final elementtable")
            allnode, elementtable=another.changeelement(allnode,elementtable)
            for i in nodetable:
                if i not in allnode:
                    nodetable.remove(i)
            l = Stability.determinancycheck(elementtable, nodetable, self.support, self.supportinfo, self.sumreactionsupport)
            if l == "unstable":
                self.unstabledata=self.unstabledata+1
            else:
                self.stabledata=self.stabledata+1
            Image.drawimage(numgridx,numgridy,allnode,elementtable,self.support,self.supportinfo,l,r)
        print(self.stabledata,"stable data")
        print(self.unstabledata,"unstable data")













if __name__ == '__main__':

    a = rectangle(3, 2,time=10)


