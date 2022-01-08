from tkinter import*
import random #IMPORTED FOR RANDOM NUMBER GENERATION
import sys
import re
import time #IMPORTED FOR TIME LABEL
import tkinter.messagebox #IMPORTED MESSAGEBOX FOR ABOUT BUTTON
root = Tk()  #window creation
root.title("Password Generator") #window title
root.configure(bg="orangered4") #bg=background color
root.geometry("1100x700") #geometry function for window widthxheight
fnamestring=StringVar() #stringvar() used to hold a string
lnamestring=StringVar()
dobstring=StringVar()
citystring=StringVar()
phonestring=StringVar()
specialstring=StringVar()
clstring=StringVar()

def generatemethod(): #method executed when generate button pressed
      fs=fnamestring.get() #get() to reterive value from variable ,textboxrelated
      ls=lnamestring.get()
      db=dobstring.get()
      cs=citystring.get()
      ps=phonestring.get()
      splstring=specialstring.get()
      value1=str(random.randint(7777,9999))
      global xv1,xv2,xv3,xv4,xv5,xv6 #declared global for later saving in file
      xv1=value1
      value2=str(random.randint(1010,9199)) #use of random.randint(from,till) for random integer generation
      xv2=value2
      value3=str(random.randint(3090,4900))
      xv3=value3
      value4=str(random.randint(5995,9999))
      xv4=value4
      value5=str(random.randint(6666,7077))
      xv5=value5
      value6=str(random.randint(8000,9999))
      xv6=value6

      global gp1,gp2,gp3,gp4,gp5,gp6 #declared global for later saving in file
      generatedpassword1=fs+str(xv6)+str(xv4)+str(db)
      gp1=generatedpassword1
      generatedpassword2=str(xv2)+ls+str(db)
      gp2=generatedpassword2
      generatedpassword3=str(xv1)+str(splstring)+cs
      gp3=generatedpassword3
      generatedpassword4=fs+str(xv3)+ls+str(xv2)
      gp4=generatedpassword4
      generatedpassword5=str(xv4)+str(splstring)+str(db)
      gp5=generatedpassword5
      generatedpassword6=ls+cs+str(db)+str(xv5)
      gp6=generatedpassword6

      #labels to display generated passwords
      #use of rows & column arangement grid(row,column)
      generated1=Label(root,text=generatedpassword1,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
      generated2=Label(root,text=generatedpassword2,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
      generated3=Label(root,text=generatedpassword3,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
      generated4=Label(root,text=generatedpassword4,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
      generated5=Label(root,text=generatedpassword5,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
      generated6=Label(root,text=generatedpassword6,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
      generated1.grid(row=20,column=0)#use of grid arrangement to place label,buttons etc
      generated2.grid(row=20,column=1)
      generated3.grid(row=21,column=0)
      generated4.grid(row=21,column=1)
      generated5.grid(row=22,column=0)
      generated6.grid(row=22,column=1)
      #labels to display generated pin passwords
      #label here is having color font, text=value text of label will have value1
      pin1=Label(root,text=value1,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
      pin2=Label(root,text=value2,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
      pin3=Label(root,text=value3,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
      pin4=Label(root,text=value4,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
      pin5=Label(root,text=value5,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
      pin6=Label(root,text=value6,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
       #use of rows & column arangement grid(row,column)
      pin1.grid(row=23,column=0)
      pin2.grid(row=23,column=1)
      pin3.grid(row=24,column=0)
      pin4.grid(row=24,column=1)
      pin5.grid(row=25,column=0)
      pin6.grid(row=25,column=1)
      save.grid(row=1,column=3)
      
def checkmethod(): #method executed when check is button pressed 
      strength=Label(root,text=" ",fg="dark orange",bg="orangered4",font=("Corbel Bold",18))
      strength.grid(row=10,column=1)
      curpass=clstring.get()#curpass is password entered tocheck,
      p= curpass
      regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')#used to check this string is in p or not
      if len(p)>=8 and len(p) <=18 and p.lower() != p and p.upper() !=p and p.isalnum()!=p and regex.search(p) !=None:
                              strength.config(text="S  T  R  O  N  G",fg="green",bg="white")
      else:
            strength.config(text="W     E      A      K",fg="red",bg="white")
            tkinter.messagebox.showinfo('N O T E','Password is weak please generate new one\n Password Should Be A Combination Of Capital Letters\n Small Letters\n Numbers\Special Characters\n Length of 6 or More')

def exittmethod(): #cannot use exit() call,is keyword
      root.destroy() #destroy method to close window kind of destructor
#labels to guide user
fname= Label(root,text="ENTER FIRST NAME:",fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
fname.grid(row=0,column=0)
#textbox is implemented using variable=Entry(textvariable=somevariable tohold value
tb1=Entry(root,textvariable=fnamestring,width=30)
tb1.grid(row=0,column=1)

lname= Label(root,text="ENTER LAST NAME:",fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
lname.grid(row=1,column=0)
tb2=Entry(root,textvariable=lnamestring,width=30)
tb2.grid(row=1,column=1)

dob=Label(root,text="ENTER DOB:",fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
tb3=Entry(root,textvariable=dobstring,width=30)
dob.grid(row=2,column=0)
tb3.grid(row=2,column=1)

city=Label(root,text="ENTER YOUR CITY/STATE:",fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
tb4=Entry(root,textvariable=citystring,width=30)
city.grid(row=3,column=0)
tb4.grid(row=3,column=1)

phone=Label(root,text="ENTER PHONE NUMBER:",fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
tb5=Entry(root,textvariable=phonestring,width=30)
phone.grid(row=4,column=0)
tb5.grid(row=4,column=1)

pl=Label(root,text="ENTER SPECIAL CHARACTERS:",fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
tb6=Entry(root,textvariable=specialstring,width=30)
pl.grid(row=5,column=0)
tb6.grid(row=5,column=1)

generate =Button(root,text="G E N E R A T E",command=generatemethod,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
generate.grid(row=6,column=1)

def SAVEmethod(): #exceutes to save passwords&pins in file on Cdrive
      file=open("D:\\generatedpassword.txt",'a')
      file.write(xv1+"\n")
      file.write(gp1+"\n")
      file.write(xv2+"\n")
      file.write(gp2+"\n")
      file.write(xv3+"\n")
      file.write(gp3+"\n")
      file.write(xv4+"\n")
      file.write(gp4+"\n")
      file.write(xv5+"\n")
      file.write(gp5+"\n")
      file.write(xv6+"\n")
      file.write(gp6+"\n")
      file.close()
      tkinter.messagebox.showinfo('S A V E D','Passwords Generated Are Stored On D:\Drive\n In a Text File')


save= Button(root,text=" S A V E",command=SAVEmethod,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))


exiit= Button(root,text="E X I T",command=exittmethod,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
exiit.grid(row=7,column=3)

cl=Label(root,text="ENTER YOUR CURRENT PASSWORD:",fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
cl.grid(row=7,column=1)
tb7=Entry(root,textvariable=clstring,width=30)
tb7.grid(row=8,column=1)

checkmethod =Button(text="C H E C K",command=checkmethod,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
checkmethod.grid(row=9,column=1)

def aboutmethod():#to display info implementation of msgbox
      tkinter.messagebox.showinfo('About','PythonProject :Password Generator\n SE2CMPN\n Made By\n Swapnil-Roll NO:03\nTusshar-Roll NO:15\n & Arvinda-Roll NO:19')
      
About=Button(root,text="A B O U T",command=aboutmethod,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
About.grid(row=3,column=3)

def helppmethod():
      tkinter.messagebox.showinfo('H E L P','You need to enter text in above textboxes\n Press Generate for generating password\n Password generated can be more than 18 Characters\n 4-DigitPin is also Generated\nYou can also Check Password Strength ')
      
helpp=Button(root,text="H E L P",command=helppmethod,fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
helpp.grid(row=3,column=4)

#here time.asctime() is function from time library
TIME =Label(root,text=time.asctime(),fg="dark orange",bg="orangered4",font=("Corbel Bold",16))
TIME.grid(row=5,column=3)
root.mainloop()#for looping this window


      
      
