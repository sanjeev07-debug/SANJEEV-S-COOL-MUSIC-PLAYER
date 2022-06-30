import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title('Sanjeev\'s Music Player!')
canvas.geometry("600x600")
canvas.config(bg = 'black')
rootpath = "C:\\Users\sanju\Desktop\music\songs"
pattern = "*.mp3" #used regex
mixer.init()

# # to add images for the buttons
# prev_image = tk.PhotoImage(file = "prev.png")
# stop_image = tk.PhotoImage(file = "stop.png")
# play_image = tk.PhotoImage(file = "play.png")
# pause_image = tk.PhotoImage(file = "play.png")
# next_image = tk.PhotoImage(file = "next.png")
#when the user want to play the song it will show the song
def select():
    label.config(text = listbox.get("anchor"))
    # to select the song i will call mixer
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    #to play the song 
    mixer.music.play()
def stop():

    mixer.music.stop()
    listbox.select_clear("active")

def nxt():
    next_song = listbox.curselection() #inorder to select the next song first we need specify the current song
    next_song = next_song[0] + 1 #index of 0 + 1
    next_sng = listbox.get(next_song)
    label.config(text = next_sng)
    #again i used the same
     
    mixer.music.load(rootpath + "\\" + next_sng)
    #to play the song 
    mixer.music.play()

    #to move the cursor
    listbox.music.play()
    
    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def prev():
    next_song = listbox.curselection() #inorder to select the next song first we need specify the current song
    next_song = next_song[0] - 1 #for prev i decreased the value 
    next_sng = listbox.get(next_song)
    label.config(text = next_sng)
    #again i used the same
     
    mixer.music.load(rootpath + "\\" + next_sng)
    #to play the song 
    mixer.music.play()

    #to move the cursor
    listbox.music.play()
    
    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

listbox = tk.Listbox(canvas,fg = "cyan", bg = "black" , width = 200 ,font  = ('poppins',14)) #you can use any font
listbox.pack(padx = 20,pady = 20) # by doing matplotlib module i got to know about colours x-axis and y-axis

label = tk.Label(canvas,text = "", bg = "black", fg = "yellow",font = ("poppins",15))
label.pack(pady = 15)
#inorder to insert items in our music box
#you can also insert some txt
# listbox.insert(0,"vibez-zayn")
# listbox.insert(1,"better-zayn")
# listbox.insert(2,"tightrope-zayn")

#for controlling the music file
top = tk.Frame(canvas, bg = "black")
top.pack(padx = 10,pady = 5,anchor = "center")

prevbutton = tk.Button(canvas , text = "Prev",command = prev)
prevbutton.pack(pady = 15,in_ = top,side = "left")

stopbutton = tk.Button(canvas,text = "stop",command = stop)
stopbutton.pack(pady = 15,in_= top,side = "left")


playbutton = tk.Button(canvas,text = "play",command= select)
playbutton.pack(pady = 15,in_= top,side = "left")

nextbutton = tk.Button(canvas,text = "next",command = nxt)
nextbutton.pack(pady = 15,in_= top,side = "left")
#for adding songs i am writing a for loop
for root, dirs, files in os.walk(rootpath):
    for i in fnmatch.filter(files, pattern):
        listbox.insert('end',i)

canvas.mainloop()