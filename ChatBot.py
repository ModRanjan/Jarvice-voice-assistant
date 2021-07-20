from tkinter import *
from PIL import Image, ImageTk
from Database_Module import *
import Assistant_Details_Module
from Output_Module import output
from Time_Module import get_time, get_date
from Database_Module import new_assistant_name, get_answers_from_memory
from Weather_Module import weather
from WebBrowser_Module import open_facebook, open_google, close_browser
from Internet_Module import check_inernet_connection, check_on_wikipedia
from News_Module import get_news
from Play_Music_module import play_music
from WindowsOperation_Module import restart, shutdown, logoff_or_signoff, hibernate
import speech_recognition as sr
import pyttsx3
import time
from Welcome_Module import greet

# creat object of class tk()
root = Tk()

# set output-Window size 
canvas_width = 888
canvas_height = 730
root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(888, 720)
root.maxsize(888, 730)
# set title 
root.title("voice Assistant")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening...")               # for testing purpose
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        # print("Recognizing...")             # for testing purpose
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:-{query}")        # for testing purpose
    except Exception:
        # print("Say that again please!")     # for testing purpose
        return "None"
    return query


def change_name_t():
    txt_output.configure(state="normal")
    temp = input_txt.get()
    txt_output.insert(END, "\n\nYou : "+input_txt.get())
    if temp == Assistant_Details_Module.name:
        r = 'Can not change.I think you are happy with my old name'
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+r)
        txt_output.configure(state="disabled")
        output('Can not change.I think you are happy with my old name')
        input_txt.delete(0, END)
    else:
        new_assistant_name(temp)
        Assistant_Details_Module.name = temp
        a = 'now you can call me '+temp
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+a)
        txt_output.configure(state="disabled")
        output('now you can call me '+temp)
        input_txt.delete(0, END)
    send = Button(input_frame, image=photo_1, bg="skyblue", relief=RIDGE, command=Send).grid(
        row=4, column=1, padx=5, pady=3, sticky='e', ipadx=2, ipady=2)
    send = Button(input_frame, image=photo_2, bg="skyblue", relief=RIDGE, command=Mic).grid(
        row=4, column=1, padx=5, pady=3, sticky='w', ipadx=2, ipady=2)
    txt_output.see(END)


def change_name_m():
    # e.delete(0,END)
    txt_output.configure(state="normal")
    temp = takeCommand()
    txt_output.insert(END, "\n\nYou : "+temp)
    if temp == Assistant_Details_Module.name:
        r = 'Can not change.I think you are happy with my old name'
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+r)
        txt_output.configure(state="disabled")
        output('Can not change.I think you are happy with my old name')
        input_txt.delete(0, END)
    else:
        new_assistant_name(temp)
        Assistant_Details_Module.name = temp
        a = 'now you can call me '+temp
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+" : "+a)
        txt_output.configure(state="disabled")
        output('now you can call me '+temp)
        input_txt.delete(0, END)
    send = Button(input_frame, image=photo_2, bg="skyblue", relief=RIDGE, command=Mic).grid(
        row=4, column=1, padx=5, pady=3, sticky='w', ipadx=2, ipady=2)
    send = Button(input_frame, image=photo_1, bg="skyblue", relief=RIDGE, command=Send).grid(
        row=4, column=1, padx=5, pady=3, sticky='e', ipadx=2, ipady=2)
    txt_output.see(END)


def teach_me_t():
    txt_output.configure(state="normal")
    temp = input_txt.get()
    txt_output.insert(END, "\n\nYou : "+temp)
    print(temp)
    if 'it means' in temp:
        temp = temp.replace('it means', '')
        temp = temp.strip()
        value = get_answers_from_memory(temp)
        if value == '':
            o = ('Can not help with this one')
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+" : "+o)
            txt_output.configure(state="disabled")
            output(o)
            input_txt.delete(0, END)
        else:
            insert_question_and_answer(query, value)
            o = 'Thanks I will remember this for next time'
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+" : "+o)
            txt_output.configure(state="disabled")
            output(o)
            input_txt.delete(0, END)
    else:
        o = 'Can not help with this one'
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+" : "+o)
        txt_output.configure(state="disabled")
        output(o)
        input_txt.delete(0, END)
    send = Button(input_frame, image=photo_1, bg="skyblue", relief=RIDGE, command=Send).grid(
        row=4, column=1, padx=5, pady=3, sticky='e', ipadx=2, ipady=2)
    txt_output.see(END)


def teach_me_m():
    txt_output.configure(state="normal")
    temp = takeCommand()
    txt_output.insert(END, "\n\nYou : "+temp)
    print(temp)
    if 'it means' in temp:
        temp = temp.replace('it means', '')
        temp = temp.strip()
        value = get_answers_from_memory(temp)
        if value == '':
            o = ('Can not help with this one')
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+" : "+o)
            txt_output.configure(state="disabled")
            output(o)
            input_txt.delete(0, END)
        else:
            insert_question_and_answer(query, value)
            o = 'Thanks I will remember this for next time'
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+" : "+o)
            txt_output.configure(state="disabled")
            output(o)
            input_txt.delete(0, END)

    else:
        o = 'Can not help with this one'
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+" : "+o)
        txt_output.configure(state="disabled")
        output(o)
        input_txt.delete(0, END)
    send = Button(input_frame, image=photo_2, bg="skyblue", relief=RIDGE, command=Mic).grid(
        row=4, column=1, padx=5, pady=3, sticky='w', ipadx=2, ipady=2)
    send = Button(input_frame, image=photo_1, bg="skyblue", relief=RIDGE, command=Send).grid(
        row=4, column=1, padx=5, pady=3, sticky='e', ipadx=2, ipady=2)
    txt_output.see(END)


def Send():
    txt_output.configure(state="normal")
    global query
    query = input_txt.get()
    answer = get_answers_from_memory(input_txt.get())
    txt_output.insert(END, "\n\nYou : "+input_txt.get())
    input_txt.delete(0, END)
    if answer == 'change name':
        output('Okay! What do you want to call me ')
        a = 'Okay! What do you want to call me '
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+" : "+a)
        txt_output.configure(state="disabled")
        send = Button(input_frame, image=photo_1, bg="skyblue", relief=RIDGE, command=change_name_t).grid(
            row=4, column=1, padx=5, pady=3, sticky='e', ipadx=2, ipady=2)
        send = Button(input_frame, image=photo_2, bg="skyblue", relief=RIDGE, command=change_name_m).grid(
            row=4, column=1, padx=5, pady=3, sticky='w', ipadx=2, ipady=2)

    elif answer == 'get time details':
        output('Time is-' + get_time())
        o = ('Time is-' + get_time())
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'check internet connection':
        if check_inernet_connection():
            output('Internet is connected')
            o = ('Internet is connected')
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
            txt_output.configure(state="disabled")
        else:
            output('Internet is not connected')
            o = ('Internet is not connected')
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
            txt_output.configure(state="disabled")

    elif answer == 'tell date':
        o = get_date()
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'on speak':
        o = turn_on_speech()
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'off speak':
        o = turn_off_speech()
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'open facebook':
        open_facebook()
        o = 'Opening facebook'
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'open google':
        open_google()
        o = 'Opening google'
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'close browser':
        close_browser()
        o = 'Closing browser'
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'get news':
        o = get_news()
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'play music':
        o = play_music()
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == '' and 'wikipedia' in query:
        if check_inernet_connection():
            answer = check_on_wikipedia(query)
            if answer != '':
                o = answer
                output(o)
                txt_output.insert(
                    END, "\n"+Assistant_Details_Module.name+":"+o)
                txt_output.configure(state="disabled")
        else:
            o = 'Internet is not connected'
            output(o)
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
            txt_output.configure(state="disabled")

    elif answer == 'weather details':
        if check_inernet_connection():
            a = weather()
            o = (a+'\n This ia all about todays weather')
            output(o)
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
            txt_output.configure(state="disabled")
        else:
            o = 'Check Internet connection First !'
            output(o)
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
            txt_output.configure(state="disabled")

    elif answer == 'exit':
        o = ('Exiting ! Thank you')
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")
        time.sleep(3)
        exit()

    elif answer == 'restart':
        o = ('Restarting. Please Wait !')
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")
        time.sleep(3)
        restart()

    elif answer == 'shutdown':
        o = ('Shutting down. Please Wait !')
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")
        time.sleep(3)
        shutdown()

    elif answer == 'hibernate':
        o = ('Hibernating. Please Wait !')
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")
        time.sleep(3)
        hibernate()

    elif answer == 'logoff':
        o = ('logging off. Please Wait !')
        output(o)
        time.sleep(3)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")
        logoff_or_signoff()

    else:
        output('I do not know. Can you tell me what it means')
        a = 'I do not know. Can you tell me what it means'
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+a)
        txt_output.configure(state="disabled")

        send = Button(input_frame, image=photo_1, bg="skyblue", relief=RIDGE, command=teach_me_t).grid(
            row=4, column=1, padx=5, pady=3, sticky='e', ipadx=2, ipady=2)
        send = Button(input_frame, image=photo_2, bg="skyblue", relief=RIDGE, command=teach_me_m).grid(
            row=4, column=1, padx=5, pady=3, sticky='w', ipadx=2, ipady=2)
    txt_output.see(END)


def Mic():
    txt_output.configure(state="normal")
    global query
    query = takeCommand()
    answer = get_answers_from_memory(query)
    txt_output.insert(END, "\n\nYou : "+query)
    input_txt.delete(0, END)
    if answer == 'change name':
        output('Okay! What do you want to call me ')
        a = 'Okay! What do you want to call me '
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+" : "+a)
        txt_output.configure(state="disabled")
        send = Button(input_frame, image=photo_2, bg="skyblue", relief=RIDGE, command=change_name_m).grid(
            row=4, column=1, padx=5, pady=3, sticky='w', ipadx=2, ipady=2)
        send = Button(input_frame, image=photo_1, bg="skyblue", relief=RIDGE, command=change_name_t).grid(
            row=4, column=1, padx=5, pady=3, sticky='e', ipadx=2, ipady=2)

    elif answer == 'get time details':
        output('Time is-' + get_time())
        o = ('Time is-' + get_time())
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'check internet connection':
        if check_inernet_connection():
            output('Internet is connected')
            o = ('Internet is connected')
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
            txt_output.configure(state="disabled")
        else:
            output('Internet is not connected')
            o = ('Internet is not connected')
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
            txt_output.configure(state="disabled")

    elif answer == 'tell date':
        o = get_date()
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'on speak':
        o = turn_on_speech()
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'off speak':
        o = turn_off_speech()
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'open facebook':
        open_facebook()
        o = 'Opening facebook'
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'open google':
        open_google()
        o = 'Opening google'
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'close browser':
        close_browser()
        o = 'Closing browser'
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'get news':
        o = get_news()
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == 'play music':
        o = play_music()
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")

    elif answer == '' and 'wikipedia' in query:
        if check_inernet_connection():
            answer = check_on_wikipedia(query)
            if answer != '':
                o = answer
                output(o)
                txt_output.insert(
                    END, "\n"+Assistant_Details_Module.name+":"+o)
                txt_output.configure(state="disabled")
        else:
            o = 'Internet is not connected'
            output(o)
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
            txt_output.configure(state="disabled")

    elif answer == 'weather details':
        if check_inernet_connection():
            a = weather()
            o = (a+'\n This ia all about todays weather')
            output(o)
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
            txt_output.configure(state="disabled")
        else:
            o = 'Check Internet connection First !'
            output(o)
            txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
            txt_output.configure(state="disabled")

    elif answer == 'exit':
        o = ('Exiting ! Thank you')
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")
        time.sleep(3)
        exit()

    elif answer == 'restart':
        o = ('Restarting. Please Wait !')
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")
        time.sleep(3)
        restart()

    elif answer == 'shutdown':
        o = ('Shutting down. Please Wait !')
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")
        time.sleep(3)
        shutdown()

    elif answer == 'hibernate':
        o = ('Hibernating. Please Wait !')
        output(o)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")
        time.sleep(3)
        hibernate()

    elif answer == 'logoff':
        o = ('logging off. Please Wait !')
        output(o)
        time.sleep(3)
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+":"+o)
        txt_output.configure(state="disabled")
        logoff_or_signoff()

    else:
        output('I do not know. Can you tell me what it means')
        a = 'I do not know. Can you tell me what it means'
        txt_output.insert(END, "\n"+Assistant_Details_Module.name+" : "+a)
        txt_output.configure(state="disabled")
        send = Button(input_frame, image=photo_2, bg="skyblue", relief=RIDGE, command=teach_me_m).grid(
            row=4, column=1, padx=5, pady=3, sticky='w', ipadx=2, ipady=2)
        send = Button(input_frame, image=photo_1, bg="skyblue", relief=RIDGE, command=teach_me_t).grid(
            row=4, column=1, padx=5, pady=3, sticky='e', ipadx=2, ipady=2)

    txt_output.see(END)


# creat Frames
left_frame = Frame(root, bg="black", borderwidth=7, relief=SUNKEN)
left_frame.grid(row=0, column=0, rowspan=4, padx=1, pady=0)

top_frame = Frame(root, bg="grey", borderwidth=4, relief=SUNKEN).grid(
    row=0, column=1, columnspan=4)

img_frame = Frame(root, relief=SUNKEN).grid(
    row=1, column=1, padx=0, columnspan=4)

output_frame = Frame(root, relief=SUNKEN).grid(
    row=9, column=1, padx=0, columnspan=4)

input_frame = Frame(root, borderwidth=4, relief=SUNKEN).grid(
    row=5, column=1, padx=0, columnspan=4)

# creating labels
label_0 = Label(left_frame, text="Here is something you can try",
                fg="black", padx=1, pady=10, font="monospace 12 bold")
label_0.grid(row=0, column=0, pady=0)

questions = get_questions_and_answers()
b = 2
for i in range(0, len(questions)):
    label_a = Label(left_frame, text=questions[i][0], padx=10, pady=6,
                    font="monospace 12 ", fg='white', bg='black').grid(row=b, column=0)
    b = b+1

label_1 = Label(top_frame, text="Welcome To Voice Assistant", bg="skyblue", fg="white", padx=179,
                pady=10, font="Helvetica 15 bold underline", justify='left', borderwidth=5, relief=RIDGE)
label_1.grid(row=0, column=1)

photo_0 = ImageTk.PhotoImage(Image.open("bgimage.jpg"))

img_label = Label(img_frame, image=photo_0, bg="skyblue",
                  padx=150, pady=0, borderwidth=5, relief=RIDGE)
img_label.grid(row=1, column=1)

txt_output = Text(output_frame, relief=RIDGE, bg="black",
                  fg="white", width=70, height=9, font="Helvetica 12 bold")
txt_output.configure(state="normal")
o = greet()
output(o)
txt_output.insert(END, "\n"+Assistant_Details_Module.name+" : "+o)
txt_output.configure(state="disabled")
txt_output.grid(row=3, column=1)

input_txt = Entry(input_frame, borderwidth=7,
                  font="Helvetica 12 bold", relief=RIDGE, width=55)
input_txt.grid(row=4, column=1)

# Button Creation
photo_1 = ImageTk.PhotoImage(Image.open("button.jpg"))
Button_InputText = Button(input_frame, image=photo_1, bg="skyblue", relief=RIDGE, command=Send).grid(
    row=4, column=1, padx=5, sticky='e', ipadx=2, ipady=2)

photo_2 = ImageTk.PhotoImage(Image.open("mic.jpg"))
Button_InputMic = Button(input_frame, image=photo_2, bg="skyblue", relief=RIDGE, command=Mic).grid(
    row=4, column=1, padx=5, sticky='w', ipadx=2, ipady=2)


root.mainloop()
# C:\Users\modra\Desktop\Personal_Assistant with gui\bgimage.jpg
