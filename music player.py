from tkinter import *
import pygame as pg
import os

win = Tk()
win.title("Music")
win.geometry("650x400")
win.resizable(0,0)

pg.init()
pg.mixer.init()
#funcs_____________________________________________________
def plays():
    showname.config(state="normal")
    showname.delete("1.0","end")
    showname.insert("1.0",pl.get("active"))
    showname.config(state="disabled")
    pg.mixer.music.load(pl.get("active"))
    pg.mixer.music.play()
def stops():
    pg.mixer.music.load(pl.get("active"))
    pg.mixer.stop()
def puases():
    pg.mixer.music.pause()
def unpuases():
    pg.mixer.music.unpause()

    

#play list __________________________________________________
plframe = LabelFrame(win,text="Musics",bg="skyblue",fg="darkblue",bd=5,font=("Yasmen",12))
plframe.place(x = 0 , y = 90,width=640 , height=200)
scroly = Scrollbar(plframe,orient="vertical")
scroly.pack(fill=Y,side="right")
pl = Listbox(plframe,bg="#00FA9A",fg="#000000",font=("yasmen",8),selectmode="single",selectbackground="white",selectforeground="black",
             height=17,yscrollcommand = scroly.set)
scroly.config(command=pl.yview)
pl.pack(fill="both",padx=10,pady=5)



#song play___________________________________________________
tframe = LabelFrame(win,text="Song",bg="skyblue",fg="darkblue",bd=5,font=("Yasmen",12))
tframe.place(x = 0 , y = 10,width=640 , height=70)

showname = Text(tframe,fg="green",bg="yellow",height=1,width=50,state="disabled",cursor="hand2")
showname.grid(row=0,column=0,padx=5,pady=8)

#control panel____________________________________________________
cframe = LabelFrame(win , text="Panel",bg="skyblue",fg="darkblue",bd=5,font=("Yasmen",12),padx=15)
cframe.place(x = 0 , y = 300,width=640 , height=70)

btnplay = Button(cframe,text="Play",bg="yellow",fg="black",width=12,command=plays)
btnplay.grid(row=0,column=0,padx=10,pady=5)

btnstop = Button(cframe,text="Stop",bg="white",fg="black",width=12,command=stops)
btnstop.grid(row=0,column=1,padx=10,pady=5)

btnpause = Button(cframe,text="Pause",bg="white",fg="black",width=12,command=puases)
btnpause.grid(row=0,column=2,padx=10,pady=5)

btnunpause = Button(cframe,text="Unpause",bg="white",fg="black",width=12,command=unpuases)
btnunpause.grid(row=0,column=3,padx=10,pady=5)
#__________________________________________________________________________________

os.chdir("E:\mahdi\music\آهنگ")
songs = os.listdir()
for song in songs:
    if ".MP3" in song or ".mp3" in song or ".wav" in song:
        
        pl.insert("end",song)
        
        
win.mainloop()