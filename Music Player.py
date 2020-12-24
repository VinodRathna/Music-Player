def unmutemusic():
    global currentvol
    root.unmutebutton.grid_remove()
    root.mutebutton.grid()
    mixer.music.set_volume(currentvol)

def mutemusic():
    global currentvol
    root.mutebutton.grid_remove()
    root.unmutebutton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)

def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text='Playing...')

def stop():
    mixer.music.stop()
    AudioStatusLabel.configure(text='Stopped...')

def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100

def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100

def pause():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatusLabel.configure(text='Paused...')

def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    root.mutebutton.grid()
    mixer.music.set_volume(0.4)
    ProgressbarVolume['value'] = 40
    ProgressbarVolumeLabel['text'] = '40%'
    mixer.music.play()
    AudioStatusLabel.configure(text='Playing...')


def musicurl():
    dd = filedialog.askopenfilename()
    audiotrack.set(dd)

def createwidhtes():
    global AudioStatusLabel,ProgressbarVolumeLabel,ProgressbarVolume,ProgressbarLabel
    #########################################----Labels----######################Label
    TrackLabel = Label(root,text='Select Song : ',background='turquoise1',font=('arial',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)

    AudioStatusLabel = Label(root,text='',background='turquoise1',font=('arial',15,'italic bold'),width=20)
    AudioStatusLabel.grid(row=2,column=1)


    ########################################################################Entry
    TrackLabelEntry = Entry(root,font=('arial',16,'italic bold'),width=35,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)
    ##################################################################Buttons
    BrowseButton = Button(root,text='Search Song',bg='deeppink',font=('arial',13,'italic bold'),width=20,bd=5,activebackground='purple4',command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)

    PlayButton = Button(root,text='Play',bg='green2',font=('arial',13,'italic bold'),width=20,bd=5,activebackground='purple4',command=playmusic)
    PlayButton.grid(row=1,column=0,padx=20,pady=20)

    root.PauseButton = Button(root,text='Pause',bg='yellow',font=('arial',13,'italic bold'),width=20,bd=5,activebackground='purple4',command=pause)
    root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

    root.ResumeButton = Button(root,text='Resume',bg='yellow',font=('arial',13,'italic bold'),width=20,bd=5,activebackground='purple4',command=resumemusic)
    root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
    root.ResumeButton.grid_remove()

    root.mutebutton = Button(root,text='Mute',bg='yellow',activebackground='purple4',bd=5,command=mutemusic,width=10)
    root.mutebutton.grid(row=6,column=3)

    root.unmutebutton = Button(root,text='Unmute',bg='yellow',activebackground='purple4',bd=5,command=unmutemusic,width=10)
    root.unmutebutton.grid(row=6,column=3)
    root.unmutebutton.grid_remove()

    VolumeUpButton = Button(root,text='Volume Up',bg='blue',font=('arial',13,'italic bold'),width=20,bd=5,activebackground='purple4',command=volumeup)
    VolumeUpButton.grid(row=1,column=2,padx=20,pady=20)

    StopButton = Button(root,text='Stop',bg='red',font=('arial',13,'italic bold'),width=20,bd=5,activebackground='purple4',command=stop)
    StopButton.grid(row=2,column=0,padx=20,pady=20)

    VolumeDownButton = Button(root,text='Volume Down',bg='blue',font=('arial',13,'italic bold'),width=20,bd=5,activebackground='purple4',command=volumedown)
    VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)
    #----------------------------------------------------------------Volume Progress Bar
    ProgressbarLabel = Label(root,text='',bg='red')
    ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    ProgressbarLabel.grid_remove()

    ProgressbarVolume = Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',
                                    value=0,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5,)


    ProgressbarVolumeLabel = Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)

################################################################################################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
root = Tk()
root.geometry('1100x500')
root.title('VR Music Player')
root.resizable(False,False)
root.configure(bg='turquoise1')
###########################################################Global Variables
audiotrack = StringVar()
currentvol = StringVar()
#################################3
createwidhtes()
mixer.init()
root.mainloop()
