import tkinter.messagebox
import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root=Tk()

mixer.init() #initializing the mixer  

root.geometry("400x400")
root.title("Muse")
root.iconbitmap(r"headphone.ico")

# menubar
menubar=Menu(root)
root.config(menu=menubar)

def aboutUs():
    tkinter.messagebox.showinfo("About Muse","This is a music player built in python.")

# to browse through the device to open a mp3 file
def browse():
    global filename
    filename=filedialog.askopenfilename()
    
subMenu=Menu(menubar)
menubar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Open",command=browse)
subMenu.add_command(label="Exit",command=root.destroy)

subMenu=Menu(menubar)
menubar.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label="About Us",command=aboutUs)

frame0=Frame(root)
frame0.pack(pady=10)

details=Label(frame0,text="Ready to make some noise?",bg="black",fg="white")
details.grid(row=0,column=0)

# length=Label(frame0,text="--:--",bg="black",fg="white")
# length.grid(row=0,column=1,padx=10)

def showDetails():
    details['text']="Playing "+os.path.basename(filename)
    # a=mixer.sound(filename)
    # totalLength=a.get_length()
    # mins,secs=divmod(totalLength,60)
    # print(round(mins),round(secs))
    
    # details['text']=str(round(mins))+":"+str(round(secs))

def playMusic():
    global paused
    if paused:# checks whether the paused variable is initialized or not
        paused=False
        mixer.music.unpause()
        statusBar['text']="Playing "+os.path.basename(filename)
    else:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusBar['text']="Playing "+os.path.basename(filename)
            showDetails()
        except:
            tkinter.messagebox.showerror("Error","Muse could not play the file! Try again.")
            print("Error")
    
paused=False       
def pauseMusic():
    global paused
    paused=True
    mixer.music.pause()
    statusBar['text']="Paused "+os.path.basename(filename)
    details['text']="Paused "+os.path.basename(filename)
    
def stopMusic():
    mixer.music.stop()
    statusBar['text']="Music stopped"
    details['text']="Ready to make some noise?"
    # length["text"]=""
    
def setVol(val):
    volume=int(val)/100
    mixer.music.set_volume(volume) # takes the value in the range 0 to 1

isMute=False
def muteMusic():
    global isMute
    if isMute:
        isMute=False
        mixer.music.set_volume(0.4)
        vol.configure(image=volImg)
        scale.set(40)
    else:
        isMute=True
        mixer.music.set_volume(0)
        vol.configure(image=muteImg)
        scale.set(0)

frame1=Frame(root)
frame1.pack(pady=10)

#play button    
playImg=PhotoImage(file="play.png")
play=Button(frame1,image=playImg,command=playMusic)
play.grid(row=0,column=0,padx=10)

#pause button
pauseImg=PhotoImage(file="pause.png")
pause=Button(frame1,image=pauseImg,command=pauseMusic)
pause.grid(row=0,column=1,padx=10)

#stop button
stopImg=PhotoImage(file="stop.png")
stop=Button(frame1,image=stopImg,command=stopMusic)
stop.grid(row=0,column=2,padx=10)

frame2=Frame(root)
frame2.pack(pady=10)

#rewind button
rewindImg=PhotoImage(file="rewind.png")
rewind=Button(frame2,image=rewindImg,command=playMusic)
rewind.grid(row=0,column=0)

#mute
muteImg=PhotoImage(file="mute.png")
volImg=PhotoImage(file="volume.png")
vol=Button(frame2,image=volImg,command=muteMusic)
vol.grid(row=0,column=1,padx=10)

#volume scale
scale=Scale(root,from_=0,to_=100,orient=HORIZONTAL,command=setVol)
scale.set(40)
mixer.music.set_volume(0.4)
scale.pack(pady=10)

# status bar
statusBar=Label(root,text="Welcome to Muse:)",relief="sunken",bg="olive",anchor=W)
statusBar.pack(side="bottom",fill=X)

root.mainloop()

