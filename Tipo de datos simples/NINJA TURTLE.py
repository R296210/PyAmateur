import turtle
#clcoding.com
t=turtle.Turtle ()
s=turtle.Screen ()
s.bgcolor('#262626')
t.pencolor('#7C909C')
t.speed  (800)
col=('#ED7864','#6E544F','#592F2F','#6E382E')
for n in range (5): #NUMERO DE ELIPCES 
        for x in range (16):
            t.speed( x+10 )
            for i in range (2):
                t.pensize (2)
                t.circle(80+n*20,90)
                t.lt(90)
        t.lt(45)
t.pencolor(col[n%4])
s.exitonclick()
