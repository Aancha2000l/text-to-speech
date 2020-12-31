from tkinter import *
from gtts import gTTS
from playsound import playsound
from PIL import ImageTk, Image  # PIL -> Pillow
import os



################### Initializing Window####################

root = Tk()
root.geometry('350x300')
root.resizable(0, 0)
root.config(bg='white')
root.title('TEXT-TO-SPEECH')

# Adding a background image

same = True
n = 0.9

background_image = Image.open("background.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize(
    (newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(150, 150, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)



# heading
Label(root, text='TEXT_TO_SPEECH', font='arial 20 bold', bg='white smoke').pack()


# label
Label(root, text='Enter Text', font='arial 15 bold', bg='White').place(x=20, y=60)


# text variable
Msg = StringVar()


# Entry
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)


# Defining functions

def text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Audio.mp3')
    playsound('Audio.mp3')
    os.remove('Audio.mp3')

def exit():
    root.destroy()

def reset():
    Msg.set("")

# Button

Button(root, text = "PLAY >", font='arial 15 bold', command = text_to_speech, bg = 'cyan').place(x=25, y=140)
Button(root, text='EXIT', font='arial 15 bold', command=exit, bg='OrangeRed1').place(x=130, y=140)
Button(root, text='RESET', font='arial 15 bold', command=reset, bg='lime').place(x=215, y=140)


# infinite loop to run program
root.mainloop()
