from tkinter import *
root=Tk()
root.config(bg='black')
root.title("Calculator")
#root.geometry("300x400")
root.maxsize(300,400)
root.minsize(300,400)
canvas=Canvas(root,width=400,height=500,background='black')
canvas.pack()
canvas.create_rectangle(20,65,280,20,fill='grey')
status='OFF'
contentL1=[]
contentL=[]
def ON():
    global status
    if status=='OFF':
        status='ON'
        canvas.create_rectangle(20,65,280,20,fill='lightgreen')
        content='                                0'
        calc_screen=Label(root,text=content,bg='lightgreen',fg='black',font=('Times',22))
        calc_screen.place(relx=0.9,rely=0.06,anchor=NE)
        contentL.clear()
        contentL1.clear()
    elif status=='ON':
        status='OFF'
        canvas.create_rectangle(20,65,280,20,fill='grey')
        calc_screen=Label(root,text='                                  ',bg='grey',font=('Times',22))
        calc_screen.place(relx=0.9,rely=0.06,anchor=NE)
text=Label(root,text='PYTHON CALCULATOR',bg='black',fg='grey',font=('Times',8,'bold'))
text.place(relx=0.29,rely=0.90)
def one(event):
    screen(1)
def two(event):
    screen(2)
def three(event):
    screen(3)
def four(event):
    screen(4)
def five(event):
    screen(5)
def six(event):
    screen(6)
def seven(event):
    screen(7)
def eight(event):
    screen(8)
def nine(event):
    screen(9)
def zero(event):
    screen(0)
def plus(event):
    screen('+')
def minus(event):
    screen('-')
def divide(event):
    screen('/')
def multiply(event):
    screen('x')
def equals(event):
    screen('=')
def power(event):
    screen('pwr')
def dot(event):
    screen('.')
def PWRON(event):
    ON()
def clear(event):
    screen('C')
def back(event):
    screen('<-')
root.bind('1',one)
root.bind('2',two)
root.bind('3',three)
root.bind('4',four)
root.bind('5',five)
root.bind('6',six)
root.bind('7',seven)
root.bind('8',eight)
root.bind('9',nine)
root.bind('0',zero)
root.bind('+',plus)
root.bind('-',minus)
root.bind('/',divide)
root.bind('x',multiply)
root.bind('<Return>',equals)
root.bind('^',power)
root.bind('.',dot)
root.bind('f',PWRON)
root.bind('C',clear)
root.bind('<BackSpace>',back)

def screen(b):
    if status=='ON':
        if b==1:
            contentL.append('1')
            contentL1.append('1')
        elif b==2:
            contentL.append('2')
            contentL1.append('2')
        elif b==3:
            contentL.append('3')
            contentL1.append('3')
        elif b==4:
            contentL.append('4')
            contentL1.append('4')
        elif b==5:
            contentL.append('5')
            contentL1.append('5')
        elif b==6:
            contentL.append('6')
            contentL1.append('6')
        elif b==7:
            contentL.append('7')
            contentL1.append('7')
        elif b==8:
            contentL.append('8')
            contentL1.append('8')
        elif b==9:
            contentL.append('9')
            contentL1.append('9')
        elif b==0:
            contentL.append('0')
            contentL1.append('0')
        elif b=='.':
            contentL.append('.')
            contentL1.append('.')
        elif b=='x':
            contentL.append('*')
            contentL1.append('*') 
        elif b=='+':
            contentL.append(' + ')
            contentL1.append(' + ')
        elif b=='/':
            contentL.append('/')
            contentL1.append('/')
        elif b=='-':
            contentL.append(' - ') 
            contentL1.append(' - ')
        elif b=='<-':
            contentL.pop() 
            contentL1.pop() 
            calc_screen=Label(root,text='                                  ',bg='lightgreen',font=('Times',22))
            calc_screen.place(relx=0.9,rely=0.06,anchor=NE)
        elif b== 'C':
            contentL.clear()
        elif b=='=':
            print(contentL)
            if len(contentL)==0:
                contentL.append('NO VALUE')
            else:
                result=''
                for i in contentL:
                    result=result+i
                try:
                    ans=eval(result)
                    if type(ans)==float and ans%1!=0:
                        ans='{0:.15f}'.format(ans)
                except:
                    ans='MATH ERROR'
                print(ans)
                contentL.clear()
                calc_screen=Label(root,text='                                  ',bg='lightgreen',font=('Times',22))
                calc_screen.place(relx=0.9,rely=0.06,anchor=NE)
                contentL.append(str(ans))
            if contentL1==contentL:
                contentL.clear()
                contentL.append('INVALID')
            else:
                pass
        
        elif b=='pwr':
            contentL.append('**')
            contentL1.append('**')

        else:
            contentL.clear()
            contentL.append('ERROR')
        content=' '
        if len(contentL)==0:
            content='                                0'
        else:
            for i in contentL:
                content=content+i
        if len(content)>=19 and content!='                                0':
            content=content[-1:-19:-1]
            content=content[::-1]
        print(content)
        calc_screen=Label(root,text=content,bg='lightgreen',fg='black',font=('Times',22))
        calc_screen.place(relx=0.9,rely=0.06,anchor=NE)
    else:
        pass
    
#calc_screen=Label(root,text='1',font=('Times',22))
#calc_screen.place(relx=0.55,rely=0.06,anchor=NW)
button_1=Button(root,text='1',padx=16,pady=12,bg='black',fg='white',command=lambda:screen(1))
button_2=Button(root,text='2',padx=16,pady=12,bg='black',fg='white',command=lambda:screen(2))
button_3=Button(root,text='3',padx=16,pady=12,bg='black',fg='white',command=lambda:screen(3))
button_4=Button(root,text='4',padx=16,pady=12,bg='black',fg='white',command=lambda:screen(4))
button_5=Button(root,text='5',padx=16,pady=12,bg='black',fg='white',command=lambda:screen(5))
button_6=Button(root,text='6',padx=16,pady=12,bg='black',fg='white',command=lambda:screen(6))
button_7=Button(root,text='7',padx=16,pady=12,bg='black',fg='white',command=lambda:screen(7))
button_8=Button(root,text='8',padx=16,pady=12,bg='black',fg='white',command=lambda:screen(8))
button_9=Button(root,text='9',padx=16,pady=12,bg='black',fg='white',command=lambda:screen(9))
button_0=Button(root,text='0',padx=43,pady=12,bg='black',fg='white',command=lambda:screen(0))
button_mul=Button(root,text='x',padx=16,pady=12,bg='black',fg='white',command=lambda:screen('x'))
button_div=Button(root,text='/',padx=16,pady=12,bg='black',fg='white',command=lambda:screen('/'))
button_add=Button(root,text='+',padx=14.49,pady=12,bg='black',fg='white',command=lambda:screen('+'))
button_sub=Button(root,text='-',padx=16,pady=12,bg='black',fg='white',command=lambda:screen('-'))
button_eql=Button(root,text='=',padx=16,pady=40,bg='black',fg='white',command=lambda:screen('='))
button_bck=Button(root,text='<-',padx=13.7,pady=12,bg='black',fg='white',command=lambda:screen('<-'))
button_clr=Button(root,text='CLEAR',padx=55,pady=12,bg='black',fg='white',command=lambda:screen('C'))
button_dec=Button(root,text='.',padx=17.4,pady=12,bg='black',fg='white',command=lambda:screen('.'))
button_pwr=Button(root,text='PWR',padx=7.4,pady=12,bg='black',fg='white',command=lambda:screen('pwr'))
button_on=Button(root,text='ON/OFF',padx=24,pady=12,bg='black',fg='white',command=lambda:ON())
button_1.place(relx=0.06,rely=0.2)
button_2.place(relx=0.24,rely=0.2)
button_3.place(relx=0.42,rely=0.2)
button_4.place(relx=0.06,rely=0.34)
button_5.place(relx=0.24,rely=0.34)
button_6.place(relx=0.42,rely=0.34)
button_7.place(relx=0.06,rely=0.48)
button_8.place(relx=0.24,rely=0.48)
button_9.place(relx=0.42,rely=0.48)
button_0.place(relx=0.06,rely=0.62)
button_mul.place(relx=0.60,rely=0.2)
button_div.place(relx=0.60,rely=0.34)
button_add.place(relx=0.60,rely=0.48)
button_sub.place(relx=0.60,rely=0.62)
button_eql.place(relx=0.775,rely=0.48)
button_bck.place(relx=0.775,rely=0.2)
button_clr.place(relx=0.06,rely=0.76)
button_dec.place(relx=0.42,rely=0.62)
button_pwr.place(relx=0.775,rely=0.34)
button_on.place(relx=0.60,rely=0.76)
root.mainloop()
