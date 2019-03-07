#!/usr/bin/env python3
import tkinter as tk
import random
from tkinter import messagebox
import copy

n = 4
length = 50 

window = tk.Tk()
window.title("2048")
window.geometry("400x200")
window.configure(background='gray19')

#canvas in tkinter
canvas = tk.Canvas(window, width=201, height=201,bg="gray")
canvas.pack(side=tk.LEFT)

#generating two random positions to initially fill the tiles
p=random.sample(range(0, 16), 2)
lst=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
t=0

#initially filing the tiles at two positions with either 2 or 4 
for row in range(4):
	for col in range(4):
		if (t==p[0] or t==p[1]) :
			a = [2,4]
			random.shuffle(a)	
			lst[row][col]=a[0]	
		t=t+1


#generates 2 or 4 at every move on a random location.
def rando():
	flag=0
	for row in range(4):
		if flag==1:break
		for col in range(4):
			p=random.sample(range(0, 2), 1)
			if (p[0]==1 and lst[row][col]==0):
				a = [2,4]
				random.shuffle(a)
				lst[row][col]=a[0]
				flag=1
				break

def make():
    canvas.delete('all')
    row=0
    for i in range(n):
        y = i * length
        col=0
        for j in range(n):
            x = j * length	
            if (lst[row][col]==0):
                #for tiles which are unfilled
                canvas.create_rectangle(x+1, y+1, x+1+length, y+1+length,fill="gray9")
                canvas.create_text((x+1+25, y+1+25), text=" ")
            else:
                #coloring the tiles for different numbers
                if(lst[row][col]==2):
                    canvas.create_rectangle(x+1, y+1, x+1+length, y+1+length,fill="lightgreen")
                elif(lst[row][col]==4):
                    canvas.create_rectangle(x+1, y+1, x+1+length, y+1+length,fill="lightblue")
                elif(lst[row][col]==8):
                    canvas.create_rectangle(x+1, y+1, x+1+length, y+1+length,fill="yellow")
                elif(lst[row][col]==16):
                    canvas.create_rectangle(x+1, y+1, x+1+length, y+1+length,fill="lightcoral")
                elif(lst[row][col]==32):
                    canvas.create_rectangle(x+1, y+1, x+1+length, y+1+length,fill="purple")
                elif(lst[row][col]==64):
                    canvas.create_rectangle(x+1, y+1, x+1+length, y+1+length,fill="plum3")
                elif(lst[row][col]==128):
                    canvas.create_rectangle(x+1, y+1, x+1+length, y+1+length,fill="maroon1")
                elif(lst[row][col]==256):
                    canvas.create_rectangle(x+1, y+1, x+1+length, y+1+length,fill="tomato")
                elif(lst[row][col]==512):
                    canvas.create_rectangle(x+1, y+1, x+1+length, y+1+length,fill="azure")
                elif(lst[row][col]==1024):
                    canvas.create_rectangle(x+1, y+1, x+1+length, y+1+length,fill="tan2")
                else:
                    canvas.create_rectangle(x+1, y+1, x+1+length, y+1+length,fill="snow")
                
                canvas.create_text((x+1+25, y+1+25), text=lst[row][col])
            col=col+1
        row=row+1
		
		
		
		
def slide(t):
	stop=0 #stop variable to avoid double merging
	for ori in range(4):                                
		if t[ori]!=0: #for every number not 0.
			tar=ori     
			#iterates backwards till stop to find a non 0 number.                                 
			while(tar > stop):
				tar-=1
				if t[tar]!=0:
					if t[tar]!=t[ori]:
                        #if the non zero number is not equal to original number then increase position by 1.
						tar+=1
					break
			if ori!=tar:	              
				if t[ori]==t[tar]:stop=tar+1	#if a merging happens update stop
				t[tar]+=t[ori] #merge.
				t[ori]=0	 #set the original position to zero.
	return t
	
	
     
 
def check(lst):
	#check if any operation i.e. left, right, up, down is possible or not. 
	p=copy.deepcopy(lst)
	count=0
    
    #check if left move possible or not
	for row in range(4):
		t=p[row][:]
		slide(t)
		p[row][:]=t	
	if p==lst: count+=1

    #check if right move possible or not	
	for row in range(4):
		t=p[row][:]
		t=t[::-1]
		slide(t)
		p[row][:]=t[::-1]
	if p==lst: count+=1

    #check if up move possible or not		
	for col in range(4):
		t=[a[col] for a in p]
		slide(t)
		for row in range(4):
			p[row][col]=t[row]	
	if p==lst: count+=1	

    #check if down move possible or not	
	for col in range(4):
		t=[a[col] for a in p]
		t=t[::-1]
		slide(t)
		for row in range(4):
			p[row][col]=t[3-row]		
	if p==lst: count+=1
    
	for row in range(4):
		for col in range(4):
			if lst[row][col]==0:count=0	
	make()	

    #when none of the moves are possible				
	if count==4 :
		#if not operation is possible show this message.
		messagebox.showinfo('2048','Try Again : You LOSE!!!')	
		p=random.sample(range(0, 16), 2)
		t=0
        #restart the game
		for row in range(4):
			for col in range(4):
				if t==p[0] or t==p[1] :
					a = [2,4]
					random.shuffle(a)	
					lst[row][col]=a[0]	
				else:	lst[row][col]=0
				t=t+1			
	make()
	
	#congratulate the user if one of the index is 2048.
	flag=0
	for row in range(4):
		if flag==1:break
		for col in range(4):
			if lst[row][col]==2048:
				messagebox.showinfo('2048','Congratualations : You WON!!!')	
				p=random.sample(range(0, 16), 2)
				t=0
                #restart a new game
				for row in range(4):
					for col in range(4):
						if t==p[0] or t==p[1] :
							a = [2,4]
							random.shuffle(a)	
							lst[row][col]=a[0]	
						else:	lst[row][col]=0
						t=t+1					
				make()
				flag=1
				break
					
	
				

#function called when left direction button is pressed				
def left():
	for row in range(4):
		t=lst[row][:]
		slide(t) #passes rows to slide()
		lst[row][:]=t	
	rando()					
	check(lst)			
		
		
#function called when right direction button is pressed		
def right():
	for row in range(4):
		t=lst[row][:]
		t=t[::-1] #passes rows in reverse to slide()
		slide(t)
		lst[row][:]=t[::-1]
	rando()
	check(lst)
		

#function called when up direction button is pressed		
def up():
	for col in range(4):
		t=[a[col] for a in lst]
		slide(t) #passes columns to slide()
		for row in range(4):
			lst[row][col]=t[row]	
	rando()					
	check(lst)


#function called when down direction button is pressed	
def down():
	for col in range(4):
		t=[a[col] for a in lst]
		t=t[::-1]
		slide(t) #passes columns in reverse order to slide()
		for row in range(4):
			lst[row][col]=t[3-row]	
	rando()					
	check(lst)


#calling the function to start the game     
make()

#creating frame to put the direction buttons
f = tk.Frame(window, width=200, height=400,bg="gray19")
f.pack(side=tk.LEFT)

#creating four buttons for four directions
bl = tk.Button(f,text="◀",command=left,bg="bisque4").pack(padx="10", pady="10",side=tk.LEFT)
br = tk.Button(f,text="▶",command=right,bg="bisque4").pack(padx="10", pady="10",side=tk.RIGHT)
bu = tk.Button(f,text="▲",command=up,bg="bisque4").pack(padx="10", pady="10",side=tk.TOP)
bd = tk.Button(f,text="▼",command=down,bg="bisque4").pack(padx="10", pady="10",side=tk.BOTTOM)


window.mainloop()
