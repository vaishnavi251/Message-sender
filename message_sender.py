
import requests
import json
from tkinter import *
from tkinter import messagebox


def send_sms(phoneno,message):
    url='https://www.fast2sms.com/dev/bulkV2'
    parameters={
        'authorization':'gEF1jLy2fe8xVN7kCLn6ScGbW9F7R61vDiw0N9RRfLLFdf4mtVdCuhD9YI78',
        'sender_id':'TXTIND',
        'message':message,
        'language':'english',
        'route':'v3',
        'numbers':phoneno
       
    }    

    response=requests.get(url,params=parameters)
    dic=response.json()
    print(dic)

#send_sms("9970097511","Helloo dear Vaish")

def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    r = send_sms(num, msg)
    if r:
        messagebox.showinfo("Send Success", "Successfully sent")
    else:
        messagebox.showerror("Error", "Details Missing!!")


# Creating GUI
root = Tk()
root.title("Message Sender ")
root.geometry("400x550")
root.configure(bg='lavender')
#img=PhotoImage(file='Message.jpeg')
#Label(root,image=img).pack()
#root.configure('lightBlue')
font = ("Helvetica", 22, "bold")
#LabelWhite=Label(root,text="\n",bg="black",width=100,height=1)
#LabelWhite.pack()
Label0=Label(root,text="Recipient's Number",font=("helvetica",15,"bold"),bg='#2764bf',fg='#d8e9f4',width='150')
Label0.pack()
textNumber = Entry(root, font=("helvetica",18),bg='#fff')
textNumber.pack(fill=X)
Label0=Label(root,text="Message",font=("helvetica",15,"bold"),bg='#2764bf',fg='#d8e9f4',width='150')
Label0.pack()
textMsg = Text(root)
textMsg.pack(fill=X)
sendBtn = Button(root, text="SEND SMS", command=btn_click,activebackground="LightSkyBlue",bg='#2764bf',bd=10,font=('Arial',12),fg='white',relief='groove')
sendBtn.pack()
root.mainloop()