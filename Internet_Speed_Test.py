from tkinter import *
import speedtest

def starttest():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down= str(round(sp.download()/(10**6),3)) + "Mbps"
    up= str(round(sp.upload()/(10**6),3)) + "Mbps"
    lad_down.config(text=down)
    lad_up.config(text=up)
    
sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="#1b1613")

lad= Label(sp,text="Internet Speed Test",font=("Time New Roman",25,"bold"), bg="#1b1613", fg="Yellow")
lad.place(x=60,y=40,height=50,width=380)

lad= Label(sp,text="Downloading speed",font=("Time New Roman",25,"bold"), bg="#1b1613", fg="White")
lad.place(x=60,y=130,height=50,width=380)

lad_down= Label(sp,text="00",font=("Time New Roman",25,"bold"), bg="White", fg="Black")
lad_down.place(x=60,y=200,height=50,width=380)

lad= Label(sp,text="Uploading speed",font=("Time New Roman",25,"bold"), bg="#1b1613", fg="White")
lad.place(x=60,y=290,height=50,width=380)

lad_up= Label(sp,text="00",font=("Time New Roman",25,"bold"), bg="White", fg="Black")
lad_up.place(x=60,y=360,height=50,width=380)

button=Button(sp,text="Start Speed Test",font=("Time New Roman",25,"bold"),relief=RAISED,bg="#808080",command=starttest)
button.place(x=60,y=460,height=50,width=380)



sp.mainloop()

