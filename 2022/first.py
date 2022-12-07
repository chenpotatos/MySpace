from manim import *
import math

class creates(Scene):
    def jumpin(self,dot2,x_goto=0,y_goto=0):
        lis=[]
        fangda=100000000
        x=0
        y=y_goto+2
        x1=0.18/fangda**0.5
        x2=-0.004/fangda
        y1=0
        y2=-0.1/fangda
        
        while 1:
            y1+=y2
            x+=x1
            y+=y1
            x1+=x2
            #x+=x1
            lis.append([x,y])
            if y<y_goto and y1<0 :
                y1=-y1*0.7
                if y1+y2<0:
                    break
        while x1>0:
            x1+=x2
            x+=x1
            lis.append([x,y_goto])

        lis=np.asarray(lis)
        last=lis[-1,0]
        
        t=ValueTracker(0)
        dot2.set_opacity(0)
        self.add(dot2)

        def run(dot2):
            place=int((len(lis)-1)*t.get_value())
            dot2.move_to(np.array([lis[place,0]-last+x_goto,lis[place,1],0]))
        dot2.add_updater(run)

        def fadein(x):
            tt=t.get_value()
            x.set_opacity(1-(1-tt)**(1/0.25))#2*tt-tt**2 2*tt**0.5/(tt+1)
            return x
        dot2.add_updater(fadein)
        self.play(t.animate.set_value(1),run_time=4,rate_func=linear)
        dot2.remove_updater(run)
        dot2.remove_updater(fadein)

#xxyy=point.centre
    def createangle3(self,x=2,y=1,xx=0,yy=0):
        point1=[x,y,0]
        point3=[distance(point1,[0,0,0]),0,0]
        self.angle=VMobject().set_points_as_corners([point1,[0,0,0],point3])
        self.angle.shift(xx*RIGHT+yy*UP)
        self.play(Create(self.angle))
    def letter(self,x=2,y=1,xx=0,yy=0,letter=Text('A'),buff=0.4):
        point1=[x,y,0]
        point3=[distance(point1,[0,0,0]),0,0]
        nextto(point1,[0,0],point3,letter,buff)
        letter.shift(xx*RIGHT+yy*UP)
        self.play(Write(letter))

    def drawarc3(self,line,radian=PI,time=1):
        path = VMobject()
        pointt1=line.get_start()
        self.pointt2=line.get_end()
        path.set_points_as_corners([self.pointt2,self.pointt2])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([line.get_end()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path)
        
        self.play(Rotating(line, radians=radian, about_point=pointt1, run_time=time,rate_func=smooth))
        self.remove(path)
        path.remove_updater(update_path)

    def daoji(self,a,place=[5,-3,0]):
        anu=Annulus(0.4,0.7,1,0,BLUE).move_to(place).scale(0.7)
        lis=[RED,ORANGE,YELLOW,GREEN,BLUE]
        tex=Text(str(a)).move_to(place).scale(0.7)
        self.play(FadeIn(anu,tex))
        #self.wait()
        for i in range(a):
            texx=Text(str(a-i-1)).move_to(place).scale(0.7)
            self.play(anu.animate.set_color(lis[i%5]),Transform(tex,texx))
        self.play(FadeOut(anu,tex))


        
    

def nextto(a,b,c,obj,buff=1):
    d=math.atan2(a[1]-b[1],a[0]-b[0])
    f=math.atan2(c[1]-b[1],c[0]-b[0])
    g=(d+f)/2+PI
    place=[b[0]+math.cos(g)*buff,b[1]+math.sin(g)*buff,0]
    obj.move_to(place)
    return place

def distance(a,b):
    c=np.asarray(b)-a
    return (c[0]**2+c[1]**2)**0.5

def copy(listt):
    return [i for i in listt]

def intersec_arc_angle(angle,lenth,point):
    point1=copy(point)
    point1[0]+=lenth
    point2=copy(point)
    point2[0]+=lenth*np.cos(angle)
    point2[1]+=lenth*np.sin(angle)
    return np.array([point1,point2])

def getangle(x,y):
    return math.atan2(y,x)


class m1(creates):
    def construct(self):

        #设参数
        x=6
        y=4
        xx=-3
        yy=-2
        do=True
        letter=Text('O')
        buff=0.4

        pointt1=np.array([xx,yy,0])
        pointt2=RIGHT*3-UP*2.5
        radian=PI
        time=1
        t0=Text('<Samuelhzx>').scale(1.5).set_color('#006fff')
        self.jumpin(t0)

        t1=Text('二等分角的作法：')
        t2=Tex('(1)在OA、OB上分别截取OD、OE，使OD=OE',tex_template=TexTemplateLibrary.ctex).scale(0.5)
        t3=Tex('(2)分别以点D、E为圆心，以大于',r'$\frac{1}{2} $','DE的同一长度为半径作弧，'
            ,tex_template=TexTemplateLibrary.ctex).scale(0.5)
        t32=Tex('两弧交于',r'$\angle$','AOB内的一点C'
            ,tex_template=TexTemplateLibrary.ctex).scale(0.5)
        t4=Tex('(3)作射线OC',tex_template=TexTemplateLibrary.ctex).scale(0.5)
        t5=Tex('OC就是所求作的角的平分线',tex_template=TexTemplateLibrary.ctex)

        g=Group(t1,t2,t3,t32,t4,t5).arrange(DL).to_corner(UL)
        #g.to_corner(UL)
        t1.to_edge()
        t2.to_edge()
        t3.to_edge()
        t32.to_edge()
        t4.to_edge()
        t5.to_edge()
        #self.add(g)
        self.wait()
        self.play(FadeOut(t0))

#angle,big_arc
        self.createangle3(x=x,y=y,xx=xx,yy=yy)
        reddot=Dot([xx,yy,0],color=RED)
        self.play(Create(reddot))
        self.letter(x=x,y=y,xx=xx,yy=yy,letter=letter)
        point1=[x,y,0]
        point3=[distance(point1,[0,0,0]),0,0]
        aa=Text('A').next_to(point1,UP).shift([xx,yy,0])
        bb=Text('B').next_to(point3,UP).shift([xx,yy,0])
        self.play(Write(aa),Write(bb))
        self.play(Write(t1))
        self.play(Write(t2))
        self.daoji(4)



        line=Line(start=pointt1,end=pointt2)
        self.play(Create(line))
        self.drawarc3(line,radian=1)

        arc=ArcBetweenPoints(
            start=self.pointt2,
            end=line.get_end(),
            angle=1,
        )
        self.add(arc)
        

#crossings

        angle=getangle(x,y)
        lenth=distance(pointt1,pointt2)
        points=intersec_arc_angle(angle,lenth,pointt1)
        dot1=Dot(points[0],color='#006fff')
        dot2=Dot(points[1],color='#006fff')
        self.play(Create(dot1),Write(dot2))
        self.play(Uncreate(line),FadeOut(arc))
        d=Text('D').next_to(dot2,UP)
        self.play(Write(d))
        ee=Text('E').next_to(dot1,UP)
        self.play(Write(ee))
#small_arcs
        self.play(Write(t3))
        self.daoji(4)



        def p2(a):
            return points[a]+RIGHT*2.5-UP*0.5
        line1=Line(start=points[0],end=p2(0))
        self.play(Create(line1))
        self.drawarc3(line1,PI*0.5)

        arc2=ArcBetweenPoints(
            start=self.pointt2,
            end=line1.get_end(),
            angle=PI*0.5,
        )
        self.add(arc2)


        #self.youhua(line1,PI*0.5)
        pointdis=points[1]-points[0]
        self.play(line1.animate.shift(pointdis))
        self.drawarc3(line1,-PI*0.7)

        arc3=ArcBetweenPoints(
            start=self.pointt2,
            end=line1.get_end(),
            angle=-PI*0.7,
        )
        self.add(arc3)
#作点c
        self.play(Write(t32))
        self.daoji(4)



        a=distance(points[1],points[0])
        b=distance(points[0],p2(0))
        gamma=math.acos((2*b**2-a**2)/(2*b**2))
        gamma=(PI-gamma)/2
        gamma=math.atan2(pointdis[1],pointdis[0])-gamma
        dot3=Dot(points[0],color='#15ff00').shift([b*np.cos(gamma),b*np.sin(gamma),0])
        self.play(Uncreate(line1))
        self.play(Create(dot3))
        c=Text('C').next_to(dot3,UP)
        self.play(Write(c))
#射线
        self.play(Write(t4))
        self.daoji(4)



        yanchang=dot3.get_center()-[xx,yy,0]
        yanchang*=1.1
        yanchang+=[xx,yy,0]
        line2=Line(start=[xx,yy,0],end=yanchang)
        self.play(Create(line2))
        self.play(FadeOut(arc2,arc3,d,ee,dot1,dot2))
        self.play(Write(t5))
        self.play(Indicate(t5))
        self.wait()
        self.play(FadeOut(line2,dot3,self.angle,g,letter,aa,bb,c,reddot))
        ttt=Text('<\Samuelhzx>').scale(1.5).set_color('#006fff')
        self.jumpin(ttt)
        self.wait()
        self.play(FadeOut(ttt))
        text=Text('text')
        self.add(text)