import cv2
import numpy
def drawimage(gridx,gridy,nodetable,elementtable,support,supportinfo,l,r):

    j=0
    scaleX=200/(gridx-1)
    scaleX=round(scaleX)
    scaleY=200/(gridy-1)
    scaleY=round(scaleY)
    scaleX=int(scaleX)
    scaleY=int(scaleY)
    print(scaleX,scaleY,"scaleX and y")
    img = numpy.ones((220, 220), numpy.uint8) * 255

    for x,y in elementtable:
        x1=nodetable[x][0]*scaleX
        y1=nodetable[x][1]*scaleY
        x2=nodetable[y][0]*scaleX
        y2=nodetable[y][1]*scaleY
        pointx1=x1+10
        pointy1=200-y1+5
        pointx2=x2+10
        pointy2=200-y2+5
        cv2.line(img,(pointx1,pointy1),(pointx2,pointy2),0,1)

    for i in nodetable:
        x1 = i[0] * scaleX
        y1 = i[1] * scaleY
        pointx1 = x1 + 10
        pointy1 = 200 - y1 + 5
        cv2.rectangle(img, (pointx1 + 1, pointy1 + 1), (pointx1 - 1, pointy1 - 1), 0, -1)
        print(pointx1,"and",pointy1)
        if i in support:
            if supportinfo["type"][j]==2:
                if supportinfo["constrained"][j]=="y":

                    cv2.circle(img,(pointx1,pointy1+5),4,0,-1)
                    print(pointx1,pointy1+5)

                else:
                    if supportinfo["constrained"][j]=="xr" :

                        cv2.circle(img,(pointx1-5,pointy1),4,0,-1)
                    else:
                        cv2.circle(img,(pointx1+5,pointy1),4,0,-1)


            else:
                if supportinfo["constrained"][j]=="xl":

                    pt1=(pointx1+1,pointy1)
                    pt2=(pointx1+10,pointy1-10)
                    pt3=(pointx1+10,pointy1+10)
                    print(pt2,"asdasd")
                    print(pt3,"asdsads")
                elif supportinfo["constrained"][j]=="xr":

                    pt1 = (pointx1-1, pointy1)
                    pt2 = (pointx1 - 10, pointy1 - 10)
                    pt3 = (pointx1 -10, pointy1 + 10)

                else:
                    print("axis Y")
                    pt1=(pointx1,pointy1+2)
                    pt2=(pointx1+5,pointy1+10)
                    pt3=(pointx1-5,pointy1+10)
                    print(pt2, "asdasd")
                    print(pt3, "asdsads")

                triangle_cnt = numpy.array([pt1, pt2, pt3])
                cv2.drawContours(img, [triangle_cnt], 0, 0, -1)

            j = j + 1

    print(img)
    ret,thresh_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    print(thresh_img.shape)
    if l == "unstable":

        cv2.imwrite("Training/unstable/"+str(r)+".bmp", thresh_img)
    else:
        cv2.imwrite("Training/stable/"+str(r)+".bmp", thresh_img)

    cv2.waitKey(0)











if __name__ == '__main__':
    gridx=3
    gridy=2
    element = ((0,1),(0,2))
    node = ((0, 0), (2, 0), (2,1))
    support=[(1,0),(2,0),(2,1)]
    supportinfo={}
    supportinfo.setdefault("type",[]).append(1)
    supportinfo.setdefault("constrained",[]).append("xr")
    supportinfo.setdefault("type",[]).append(2)
    supportinfo.setdefault("constrained",[]).append("y")
    supportinfo.setdefault("type",[]).append(2)
    supportinfo.setdefault("constrained",[]).append("xl")

    drawimage(gridx,gridy,node,element,support,supportinfo)

    #ผิดตรง 0,0


