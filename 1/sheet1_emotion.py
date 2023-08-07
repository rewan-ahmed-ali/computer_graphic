#rewan ahmed ali -->cs
from graphics import *
def main():
    win = GraphWin("rewan ahmed ",500,500)
    win.setBackground("pink")
    #الشكل
    cir=Circle(Point(250,250),100)
    cir.setFill("yellow")
    cir.setOutline(color_rgb(199,169,16))
    cir.draw(win)
    #العين الاولي
    eye1=Circle(Point(290,230),20)
    eye1.setFill("white")
    eye1.draw(win)
    eye11=Circle(Point(289,229),10)
    eye11.setFill("black")
    eye11.draw(win)
    #العين اللي ع يمين
    eye2=Circle(Point(210,230),20)
    eye2.setFill("white")
    eye2.draw(win)
    eye22=Circle(Point(210,229),10)
    eye22.setFill("black")
    eye22.draw(win)
    #الفم
    cirmouse=Circle(Point(252,289),25)
    cirmouse.setFill("black")
    cirmouse.draw(win)
    #اللسان

    irmouse=Circle(Point(255,299),15)
    irmouse.setFill("red")
    irmouse.setOutline("red")
    irmouse.draw(win)

    cirmouseba=Circle(Point(250,280),25)
    cirmouseba.setFill("yellow")
    cirmouseba.setOutline("yellow")
    cirmouseba.draw(win)
    #يتحرك للاخر يمين

    for r in range(10):
        time.sleep(1)
        cir.move(14,0)
        eye1.move(14,0)
        eye11.move(14,0)
        eye2.move(14,0)
        eye22.move(14,0)
        cirmouse.move(14,0)
        irmouse.move(14,0)
        cirmouseba.move(14,0)
        #يتحرك للاخر شمال

    for p in range(20):
        time.sleep(1)
        cir.move(-14,0)
        eye1.move(-14,0)
        eye11.move(-14,0)
        eye2.move(-14,0)
        eye22.move(-14,0)
        cirmouse.move(-14,0)
        irmouse.move(-14,0)
        cirmouseba.move(-14,0)
    #يرجع للنص
    
    for o in range(10):
        time.sleep(1)
        cir.move(14,0)
        eye1.move(14,0)
        eye11.move(14,0)
        eye2.move(14,0)
        eye22.move(14,0)
        cirmouse.move(14,0)
        irmouse.move(14,0)
        cirmouseba.move(14,0)
    win.getMouse()
    win.close()
main()  