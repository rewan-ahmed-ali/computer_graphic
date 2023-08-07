
from graphics import *
def main():
    win = GraphWin("sheet2",500,500)
    win.setBackground("#EBDDE2")
    #country 
    txt=Text(Point(250,41),"write a country")
    txt.setFill("#7E354D")
    txt.setSize(15)
    txt.draw(win)
    #entry
    text_ent=Entry(Point(250,91),10)
    text_ent.setFill("pink")
    text_ent.draw(win)
    win.getMouse()

    entry1=text_ent.getText()
    print(entry1)

    text=Text(Point(242,131),entry1)
    text.setFill("#7E354D")
    text.setFace("courier")
    text.draw(win)

    if (entry1=="egypt" or entry1=="Egypt" or entry1=="EGYPT"):
        
        rec1=Rectangle(Point(128,151),Point(378,191))
        rec1.setFill("red")
        rec1.setOutline("red")
        rec1.draw(win)

        rec2=Rectangle(Point(128,191),Point(378,231))
        rec2.setFill("white")
        rec2.setOutline("white")
        rec2.draw(win)


        rec3=Rectangle(Point(128,229),Point(378,274))
        rec3.setFill("black")
        rec3.setOutline("black")
        rec3.draw(win)

        img=Image(Point(247,209),"egypt.png")
        img.getPixel(5,2)
        img.draw(win)
        
        
        for r in range(6):
            time.sleep(2)
            rec1.move(5,15)
            rec2.move(5,15)
            rec3.move(5,15)
            img.move(5,15)
        for o in range(6):
            time.sleep(2)
            rec1.move(-5,-15)
            rec2.move(-5,-15)
            rec3.move(-5,-15)
            img.move(-5,-15)    
    elif entry1=="iraq" or entry1=="Iraq" or entry1=="IRAQ":
        rec11=Rectangle(Point(128,151),Point(378,191))
        rec11.setFill("red")
        rec11.setOutline("red")
        rec11.draw(win)

        rec22=Rectangle(Point(128,191),Point(378,231))
        rec22.setFill("white")
        rec22.setOutline("white")
        rec22.draw(win)


        rec33=Rectangle(Point(128,229),Point(378,274))
        rec33.setFill("black")
        rec33.setOutline("black")
        rec33.draw(win)

        txt2 =Text(Point(253,211),"ﷲ اكبر")
        txt2.setFill("green")
        txt2.setSize(15)
        txt2.draw(win)
        for r in range(6):
            time.sleep(2)
            rec11.move(5,15)
            rec22.move(5,15)
            rec33.move(5,15)
            txt2.move(5,15)
        for o in range(6):
            time.sleep(2)
            rec11.move(-5,-15)
            rec22.move(-5,-15)
            rec33.move(-5,-15)
            txt2.move(-5,-15)

    elif entry1=="Syria" or entry1=="syria" or entry1=="SYRIA":
        rec111=Rectangle(Point(128,151),Point(378,191))
        rec111.setFill("red")
        rec111.setOutline("red")
        rec111.draw(win)

        rec222=Rectangle(Point(128,191),Point(378,231))
        rec222.setFill("white")
        rec222.setOutline("white")
        rec222.draw(win)


        rec333=Rectangle(Point(128,229),Point(378,274))
        rec333.setFill("black")
        rec333.setOutline("black")
        rec333.draw(win)
        pol=Polygon(Point(302,197),Point(308,208),Point(320,208),Point(310,215),Point(314,225),Point(305,217),Point(297,225),
        Point(300,213),Point(289,207),Point(300,207))
        pol.setFill("green")
        pol.setOutline("green")
        pol.draw(win)

        pol2=Polygon(Point(203,199),Point(209,210),Point(219,210),Point(209,217),Point(213,227),Point(204,219),Point(198,227),
        Point(199,215),Point(190,209),Point(201,209))
        pol2.setFill("green")
        pol2.setOutline("green")
        pol2.draw(win)

        for r in range(6):
            time.sleep(2)
            rec111.move(5,15)
            rec222.move(5,15)
            rec333.move(5,15)
            pol.move(5,15)
            pol2.move(5,15)
        for o in range(6):
            time.sleep(2)
            rec111.move(-5,-15)
            rec222.move(-5,-15)
            rec333.move(-5,-15)
            pol.move(-5,-15)
            pol2.move(-5,-15)
    else:
        ttt=Text(Point(250,250),"write syria or iraq or egypt")
        ttt.draw(win)
        print("write syria or iraq or egypt")        
    
    win.getMouse()
    win.close()
main()  

