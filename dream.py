import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import pyautogui
from tkinter import filedialog
from os import path

#Global varialbe
vr = 3
playerlist = ['degea','shaw','cancelo','maguire','rubbendias','kimmich','kdb','bruno','rashford','cavani','bernardo']
stringname = ""
pathfile = open("enterhere.txt","r")
SAVE_PATH = pathfile.read()
pathfile.close()



#Global function
def takeScreenshot(win,mode,SAVE):


    # get the region of the canvas
    x, y = win.winfo_rootx(), win.winfo_rooty()
    w, h = win.winfo_width(), win.winfo_height()

    myScreenshot = pyautogui.screenshot('sesadas.png',region=(x,y,w,h))
    rmk = (0,150,335,599)
    rmkimg = myScreenshot.crop(rmk)
    if mode == 1:
        try:
            file_path = filedialog.asksaveasfilename(defaultextension='.png')
            rmkimg.save(file_path)
        except:
            pass
    elif mode ==2:
        rmkimg.save(SAVE)


#Frame
class mainscreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def gototrans():
            url = 'https://www.transfermarkt.com/'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)

        def bgmaker():
            global vr
            #backgroundh3 = ImageTk.PhotoImage(Image.open("C:\\Users\Administrator\Desktop\Project X. Dream Team XL\Opening Wallpaper\\neto.jpg"))
            if vr == 1:
                backgroundh1 = ImageTk.PhotoImage(Image.open("Opening Wallpaper/cavani_0.jpg"))
                a1.configure(image = backgroundh1)
                a1.image = backgroundh1
                vr = 2

            elif vr == 2:
                backgroundh2 = ImageTk.PhotoImage(Image.open("Opening Wallpaper/damos.jpg"))
                a1.configure(image = backgroundh2)
                a1.image = backgroundh2
                vr = 3
            elif vr == 3:
                backgroundh3 = ImageTk.PhotoImage(Image.open("Opening Wallpaper/neto.jpg"))
                a1.configure(image=backgroundh3)
                a1.image = backgroundh3
                vr = 4
            else:
                backgroundh4 = ImageTk.PhotoImage(Image.open("Opening Wallpaper/silva.jpg"))
                a1.configure(image = backgroundh4)
                a1.image = backgroundh4
                vr = 1
            a1.place(x=0, y=0, relwidth=1, relheight=1)

        #Set up background
        loadbg = Image.open("Opening Wallpaper/cavani_0.jpg")
        background = ImageTk.PhotoImage(loadbg)
        a1 = tk.Label(self, image=background)
        a1.image = background
        a1.place(x=0, y=0)

        #Main button
        buildbutton = tk.Button(self, text="BUILD NOW", font=("Courier", 20), fg="white", bg="green",command =lambda: controller.show_frame(MediatePage))
        buildbutton.place(x=0, y=220)

        librarybutton = tk.Button(self, text="LIBRARY", font=("Courier", 20), fg="white", bg="green", command = lambda :controller.show_frame(LibraryPage))
        librarybutton.place(x=0, y=280)

        webbutton = tk.Button(self, text="Market values &\nTransfer news", font=("Courier", 10), fg="white", bg="green",command=gototrans)
        webbutton.place(x=0, y=340)

        exitbutton = tk.Button(self, text="exit", font=("Courier", 20), fg="white", bg="green", command=self.quit)
        exitbutton.place(x=0, y=390)


    #Change Background
        changebutton = tk.Button(self, text = "change wallpaper", font=("Helvetica", 8), bg="SystemButtonFace", command = lambda: bgmaker())
        changebutton.place(x =320, y =550)

class SecondPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("Storage/bsbackground.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        #Command Button
        self.back_image = ImageTk.PhotoImage(file = "Storage/backbutton.jpg")
        self.saveas_image = ImageTk.PhotoImage(file = "Storage/saveasbutton.png")
        self.save_image = ImageTk.PhotoImage(file = r"Storage/savebutton.png")
        backbutton = tk.Button(self,image = self.back_image, command = lambda: controller.show_frame(mainscreen))
        backbutton.place(x =0 , y = 0)

        saveasbutton = tk.Button(self, image=self.saveas_image, command = lambda : takeScreenshot(parent,1,SAVE_PATH))
        saveasbutton.place(x=340,y=550)

        savebutton = tk.Button(self, image=self.save_image, command = lambda : takeScreenshot(parent,2,SAVE_PATH))
        savebutton.place(x=340,y =500)

        def choose_player(lab,mode):

            Choosing = tk.Toplevel()
            Choosing.title('Select one')
            Choosing.iconbitmap("iconbitmap/icon.ico")

            global frame2

            self.defaulfavt = ImageTk.PhotoImage(Image.open("Storage\playerchoose.png"))
            frame2 = tk.Label(Choosing, image=self.defaulfavt)
            frame2.grid(row=1, column=0)

            def switchavt(lab):

                try:
                    str1 = playerlistbox.get("anchor")
                    newlink = "Player/" + str1 + ".jpg"

                    self.pav = ImageTk.PhotoImage(Image.open(newlink))
                    frame2.config(image=self.pav)
                except:
                    pass
            frame1 = tk.LabelFrame(Choosing, text = " Player")
            scrollbar = tk.Scrollbar(frame1, orient= "vertical")

            playerlistbox = tk.Listbox(frame1, width=30,height =10, selectmode= "SINGLE" ,yscrollcommand=scrollbar.set)
            scrollbar.config(command=playerlistbox.yview)
            scrollbar.pack(side="right", fill="y")
            playerlistbox.pack(pady=15)
            frame1.grid(row=1,column = 1)
            playerlistbox.insert("end", "bernardo")
            playerlistbox.insert("end", "bruno")
            playerlistbox.insert("end", "cancelo")
            playerlistbox.insert("end", "cavani")
            playerlistbox.insert("end", "degea")
            playerlistbox.insert("end", "kdb")
            playerlistbox.insert("end", "kimmich")
            playerlistbox.insert("end", "maguire")
            playerlistbox.insert("end", "rashford")
            playerlistbox.insert("end", "rubbendias")
            playerlistbox.insert("end", "shaw")

            def setavt(mode):
                str2 = playerlistbox.get("anchor")
                index1 = "Storage/JPEG/" + str2 + "mini" + ".jpg"
                if mode == "cf":
                    self.avtcf = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtcf)
                    bcf.config(text = str2,font =("Arial",5),padx =14)
                elif mode == "am":
                    self.avtam = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtam)
                    bam.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "cm":
                    self.avtcm = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtcm)
                    bcm.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "dm":
                    self.avtdm = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtdm)
                    bdm.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "rw":
                    self.avtrw = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtrw)
                    brw.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "lw":
                    self.avtlw = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtlw)
                    blw.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "lcb":
                    self.avtlcb = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtlcb)
                    blcb.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "rcb":
                    self.avtrcb = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtrcb)
                    brcb.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "rb":
                    self.avtrb = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtrb)
                    brb.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "lb":
                    self.avtlb = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtlb)
                    blb.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "gk":
                    self.avtgk = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtgk)
                    bgk.config(text=str2, font=("Arial", 5), padx=14)

            frame3 = tk.Frame(Choosing)
            frame3.grid(row = 2, column = 0)
            global stringname
            #global stringname

            select_button = tk.Button(frame3,text = "Select",padx = 40,command= lambda: setavt(mode))
            select_button.pack()

            exitbutton = tk.Button(frame3,text = "Back",padx =40, command = Choosing.destroy)
            exitbutton.pack()

            playerlistbox.bind("<<ListboxSelect>>",switchavt)


        #Position Button


        acf = ImageTk.PhotoImage(Image.open("Storage/avt.png"))
        lcf = tk.Label(self,image = acf,bd =5)
        lcf.image = acf
        lcf.place(x=150,y=200)

        bcf = tk.Button(self,text = "Choose one...", font = ("Arial",5), command = lambda : choose_player(lcf,"cf"))
        bcf.place(x=150,y=190)

        aam = ImageTk.PhotoImage(Image.open("Storage/avt.png"))
        lam = tk.Label(self, image=aam,bd =5)
        lam.image = aam
        lam.place(x=150, y=300)

        bam = tk.Button(self, text="Choose one...", font=("Arial", 5), command = lambda : choose_player(lam,"am"))
        bam.place(x=150, y=290)

        acm = ImageTk.PhotoImage(Image.open("Storage/avt.png"))
        lcm = tk.Label(self, image=acm,bd =5)
        lcm.image = acm
        lcm.place(x=100, y=360)

        bcm = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(lcm,"cm"))
        bcm.place(x=100, y=350)

        adm = ImageTk.PhotoImage(Image.open("Storage/avt.png"))
        ldm = tk.Label(self, image=adm,bd =5)
        ldm.image = adm
        ldm.place(x=200, y=360)

        bdm = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(ldm,"dm"))
        bdm.place(x=200, y=350)

        arw = ImageTk.PhotoImage(Image.open("Storage/avt.png"))
        lrw = tk.Label(self, image=arw,bd =5)
        lrw.image = arw
        lrw.place(x=260, y=220)

        brw = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(lrw,"rw"))
        brw.place(x=260, y=210)

        alw = ImageTk.PhotoImage(Image.open("Storage/avt.png"))
        llw = tk.Label(self, image=alw,bd =5)
        llw.image = alw
        llw.place(x=40, y=220)

        blw = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(llw,"lw"))
        blw.place(x=40, y=210)

        arcb = ImageTk.PhotoImage(Image.open("Storage/avt.png"))
        lrcb = tk.Label(self, image=arcb,bd =5)
        lrcb.image = arcb
        lrcb.place(x=190, y=460)

        brcb = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(lrcb,"rcb"))
        brcb.place(x=190, y=450)

        alcb = ImageTk.PhotoImage(Image.open("Storage/avt.png"))
        llcb = tk.Label(self, image=alcb,bd =5)
        llcb.image = alcb
        llcb.place(x=110, y=460)

        blcb = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(llcb,"lcb"))
        blcb.place(x=110, y=450)

        arb = ImageTk.PhotoImage(Image.open("Storage/avt.png"))
        lrb = tk.Label(self, image=arb,bd =5)
        lrb.image = arb
        lrb.place(x=280, y=450)

        brb = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(lrb,"rb"))
        brb.place(x=280, y=440)

        alb = ImageTk.PhotoImage(Image.open("Storage/avt.png"))
        llb = tk.Label(self, image=alb)
        llb.image = alb
        llb.place(x=20, y=450)

        blb = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(llb,"lb"))
        blb.place(x=20, y=440)

        agk = ImageTk.PhotoImage(Image.open("Storage/avt.png"))
        lgk = tk.Label(self, image=agk,bd =5)
        lgk.image = agk
        lgk.place(x=150, y=550)

        bgk = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(lgk,"gk"))
        bgk.place(x=150, y=540)

        #Nothing

class SecondPage2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("Storage/bsbackground.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        #Command Button
        self.back_image = ImageTk.PhotoImage(file = r"Storage\\backbutton.jpg")
        self.saveas_image = ImageTk.PhotoImage(file = r"Storage\saveasbutton.png")
        self.save_image = ImageTk.PhotoImage(file = r"Storage\savebutton.png")
        backbutton = tk.Button(self,image = self.back_image, command = lambda: controller.show_frame(mainscreen))
        backbutton.place(x =0 , y = 0)

        saveasbutton = tk.Button(self, image=self.saveas_image, command = lambda : takeScreenshot(parent,1,SAVE_PATH))
        saveasbutton.place(x=340,y=550)

        savebutton = tk.Button(self, image=self.save_image, command = lambda : takeScreenshot(parent,2,SAVE_PATH))
        savebutton.place(x=340,y =500)

        def choose_player(lab,mode):

            Choosing = tk.Toplevel()
            Choosing.title('Select one')
            Choosing.iconbitmap(r'iconbitmap\icon.ico')

            global frame2

            self.defaulfavt = ImageTk.PhotoImage(Image.open(r"Storage\playerchoose.png"))
            frame2 = tk.Label(Choosing, image=self.defaulfavt)
            frame2.grid(row=1, column=0)

            def switchavt(lab):

                try:
                    str1 = playerlistbox.get("anchor")
                    newlink = "Player/" + str1 + ".jpg"

                    self.pav = ImageTk.PhotoImage(Image.open(newlink))
                    frame2.config(image=self.pav)
                except:
                    pass
            frame1 = tk.LabelFrame(Choosing, text = " Player")
            scrollbar = tk.Scrollbar(frame1, orient= "vertical")

            playerlistbox = tk.Listbox(frame1, width=30,height =10, selectmode= "SINGLE" ,yscrollcommand=scrollbar.set)
            scrollbar.config(command=playerlistbox.yview)
            scrollbar.pack(side="right", fill="y")
            playerlistbox.pack(pady=15)
            frame1.grid(row=1,column = 1)
            playerlistbox.insert("end", "bernardo")
            playerlistbox.insert("end", "bruno")
            playerlistbox.insert("end", "cancelo")
            playerlistbox.insert("end", "cavani")
            playerlistbox.insert("end", "degea")
            playerlistbox.insert("end", "kdb")
            playerlistbox.insert("end", "kimmich")
            playerlistbox.insert("end", "maguire")
            playerlistbox.insert("end", "rashford")
            playerlistbox.insert("end", "rubbendias")
            playerlistbox.insert("end", "shaw")

            def setavt(mode):
                str2 = playerlistbox.get("anchor")
                index1 = "Storage/JPEG/" + str2 + "mini" + ".jpg"
                if mode == "cf":
                    self.avtcf = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtcf)
                    bcf.config(text = str2,font =("Arial",5),padx =14)
                elif mode == "am":
                    self.avtam = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtam)
                    bam.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "cm":
                    self.avtcm = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtcm)
                    bcm.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "dm":
                    self.avtdm = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtdm)
                    bdm.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "rw":
                    self.avtrw = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtrw)
                    brw.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "lw":
                    self.avtlw = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtlw)
                    blw.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "lcb":
                    self.avtlcb = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtlcb)
                    blcb.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "rcb":
                    self.avtrcb = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtrcb)
                    brcb.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "rb":
                    self.avtrb = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtrb)
                    brb.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "lb":
                    self.avtlb = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtlb)
                    blb.config(text=str2, font=("Arial", 5), padx=14)
                elif mode == "gk":
                    self.avtgk = ImageTk.PhotoImage(Image.open(index1))
                    lab.config(image=self.avtgk)
                    bgk.config(text=str2, font=("Arial", 5), padx=14)

            frame3 = tk.Frame(Choosing)
            frame3.grid(row = 2, column = 0)
            global stringname
            #global stringname

            select_button = tk.Button(frame3,text = "Select",padx = 40,command= lambda: setavt(mode))
            select_button.pack()

            exitbutton = tk.Button(frame3,text = "Back",padx =40, command = Choosing.destroy)
            exitbutton.pack()

            playerlistbox.bind("<<ListboxSelect>>",switchavt)


        #Position Button


        acf = ImageTk.PhotoImage(Image.open("Storage\\avt.png"))
        lcf = tk.Label(self,image = acf,bd =5)
        lcf.image = acf
        lcf.place(x=90,y=200)

        bcf = tk.Button(self,text = "Choose one...", font = ("Arial",5), command = lambda : choose_player(lcf,"cf"))
        bcf.place(x=90,y=190)

        aam = ImageTk.PhotoImage(Image.open("Storage\\avt.png"))
        lam = tk.Label(self, image=aam,bd =5)
        lam.image = aam
        lam.place(x=200, y=200)

        bam = tk.Button(self, text="Choose one...", font=("Arial", 5), command = lambda : choose_player(lam,"am"))
        bam.place(x=200, y=190)

        acm = ImageTk.PhotoImage(Image.open("Storage\\avt.png"))
        lcm = tk.Label(self, image=acm,bd =5)
        lcm.image = acm
        lcm.place(x=100, y=340)

        bcm = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(lcm,"cm"))
        bcm.place(x=100, y=330)

        adm = ImageTk.PhotoImage(Image.open("Storage\\avt.png"))
        ldm = tk.Label(self, image=adm,bd =5)
        ldm.image = adm
        ldm.place(x=200, y=340)

        bdm = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(ldm,"dm"))
        bdm.place(x=200, y=330)

        arw = ImageTk.PhotoImage(Image.open("Storage\\avt.png"))
        lrw = tk.Label(self, image=arw,bd =5)
        lrw.image = arw
        lrw.place(x=280, y=260)

        brw = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(lrw,"rw"))
        brw.place(x=280, y=250)

        alw = ImageTk.PhotoImage(Image.open("Storage\\avt.png"))
        llw = tk.Label(self, image=alw,bd =5)
        llw.image = alw
        llw.place(x=0, y=260)

        blw = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(llw,"lw"))
        blw.place(x=0, y=250)

        arcb = ImageTk.PhotoImage(Image.open("Storage\\avt.png"))
        lrcb = tk.Label(self, image=arcb,bd =5)
        lrcb.image = arcb
        lrcb.place(x=190, y=460)

        brcb = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(lrcb,"rcb"))
        brcb.place(x=190, y=450)

        alcb = ImageTk.PhotoImage(Image.open("Storage\\avt.png"))
        llcb = tk.Label(self, image=alcb,bd =5)
        llcb.image = alcb
        llcb.place(x=110, y=460)

        blcb = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(llcb,"lcb"))
        blcb.place(x=110, y=450)

        arb = ImageTk.PhotoImage(Image.open("Storage\\avt.png"))
        lrb = tk.Label(self, image=arb,bd =5)
        lrb.image = arb
        lrb.place(x=280, y=450)

        brb = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(lrb,"rb"))
        brb.place(x=280, y=440)

        alb = ImageTk.PhotoImage(Image.open("Storage\\avt.png"))
        llb = tk.Label(self, image=alb)
        llb.image = alb
        llb.place(x=20, y=450)

        blb = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(llb,"lb"))
        blb.place(x=20, y=440)

        agk = ImageTk.PhotoImage(Image.open("Storage\\avt.png"))
        lgk = tk.Label(self, image=agk,bd =5)
        lgk.image = agk
        lgk.place(x=150, y=550)

        bgk = tk.Button(self, text="Choose one...", font=("Arial", 5),command = lambda : choose_player(lgk,"gk"))
        bgk.place(x=150, y=540)

        #Nothing

class MediatePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.wpp = ImageTk.PhotoImage(Image.open(r"Storage\wpp2.jpg"))
        bglabel = tk.Label(self,image = self.wpp)
        bglabel.place(x=0,y=0)

        button433 = tk.Button(self,text = "4  3  3", font = ("Courier",20), bg = "green", fg = "white",command= lambda: controller.show_frame(SecondPage))
        button433.place(x = 160, y =340)

        button442 = tk.Button(self, text="4  4  2", font=("Courier", 20),bg = "green", fg = "white",command= lambda: controller.show_frame(SecondPage2))
        button442.place(x=160, y=400)

        backbutton = tk.Button(self,text ="BACK",font=("Courier", 20),bg = "green", fg = "white",command= lambda: controller.show_frame(mainscreen),padx = 25 )
        backbutton.place(x=160, y=460)

class LibraryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        bgimg = ImageTk.PhotoImage(file = r"Storage\librarywallpaper.jpg")
        background = tk.Label(self,image = bgimg )
        background.image = bgimg
        background.place(x=0,y=0)

        eximg = ImageTk.PhotoImage(file =r"Storage\rootw.jpg" )
        lab = tk.Label(self,image = eximg)
        lab.image = eximg
        lab.place(x=187,y=150)

        def changeplayer(e):
            my_pic1 = ImageTk.PhotoImage(file=r"Storage\messi.jpg")
            lab.config(image=my_pic1)
            lab.image = my_pic1
        def changeclub(e):
            my_pic2 = ImageTk.PhotoImage(file=r"Storage\clubwallpaper.jpg")
            lab.config(image=my_pic2)
            lab.image = my_pic2
        def changenation(e):
            my_pic3 = ImageTk.PhotoImage(file=r"Storage\italy2006.jpg")
            lab.config(image=my_pic3)
            lab.image = my_pic3
        def changeback(e):
            my_pic4 = ImageTk.PhotoImage(file=r"Storage\rootw.jpg")
            lab.config(image=my_pic4)
            lab.image = my_pic4

        player_button = tk.Button(self,text = "Players", font=("Courier",20),fg = "white", bg="green",command = lambda :controller.show_frame(PlayerPage))
        player_button.place(x=0,y=200)

        club_button = tk.Button(self, text="Clubs", font=("Courier", 20), fg="white", bg="green",padx = 16)
        club_button.place(x=0, y=270)

        nation_button = tk.Button(self, text="Nation", font=("Courier", 20), fg="white", bg="green",padx = 6)
        nation_button.place(x=0, y=340)

        backimg = ImageTk.PhotoImage(file = r"Storage\backbutton.jpg")
        backbutton = tk.Button(self,image =backimg,command = lambda :controller.show_frame(mainscreen))
        backbutton.image = backimg
        backbutton.place(x=0,y=0)

        player_button.bind("<Enter>",changeplayer)
        club_button.bind(("<Enter>"),changeclub)
        nation_button.bind("<Enter>",changenation)
        background.bind("<Enter>",changeback)

class PlayerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.bg = ImageTk.PhotoImage(file = r"Storage\playerback.jpg")
        labback = tk.Label(self,image = self.bg)
        labback.place(x=0,y=0)

        backimg = ImageTk.PhotoImage(file=r"Storage\backbutton.jpg")
        backbutton = tk.Button(self, image=backimg, command=lambda: controller.show_frame(mainscreen))
        backbutton.image = backimg
        backbutton.grid(row =0, column =0)

        self.shawimg = ImageTk.PhotoImage(file = r"Storage\JPEG\shawmini.jpg")
        shawlab = tk.Button(self,image = self.shawimg)
        shawlab.grid(row=5,column=0,pady=20)

        self.canceloimg = ImageTk.PhotoImage(file=r"Storage\JPEG\cancelomini.jpg")
        cancelolab = tk.Button(self, image=self.canceloimg)
        cancelolab.grid(row=5, column=1, pady=20)



class Form(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
#Taskbar Menu

        def changelocation():
            global SAVE_PATH,pathfile
            def checklink(string1):
                global SAVE_PATH,pathfile
                if (path.isdir(string1)) == True or path.isfile(string1) == True:
                    SAVE_PATH = string1 + "\dreamteam.png"
                    messagebox.showinfo("Successed", message="File location changed\n" + SAVE_PATH)

                else:
                    messagebox.showerror(message="Invalid file location")

                x = open("enterhere.txt", "wt")
                x.write(SAVE_PATH)
                x.close()

            cfile = tk.Toplevel()
            cfile.title("Change file location!")
            lbf = tk.Label(cfile, text="Change the location you want", font=("Arial", 15))
            lbf.pack()

            frame1 = tk.LabelFrame(cfile, text="Enter here", pady=20)
            frame1.pack()
            vt = tk.StringVar(frame1,value=SAVE_PATH)
            entryf = tk.Entry(frame1, width=90, textvariable=vt)
            entryf.pack()

            changebutton = tk.Button(cfile, text="Change", padx=20, command=lambda: checklink(entryf.get()))
            changebutton.pack(side="left")

            exitbutton = tk.Button(cfile, text="Exit", padx=20, command=cfile.destroy)
            exitbutton.pack(side="left")

        def helpwindow():
            global imghelp
            hw = tk.Toplevel()
            hw.title("Help")
            hw.grid()
            imghelp = ImageTk.PhotoImage(
                Image.open(r"Help\heplw.jpg"))
            l1 = tk.Label(hw, image=imghelp)
            l1.pack()
            qb = tk.Button(hw, text="Back", font=("Helvetica", 20), command=hw.destroy).pack()

        def aboutuswindow():
            global imgab
            aw = tk.Toplevel()
            aw.title("About me")
            aw.grid()

            def openfb():
                url = 'https://fb.com/thanh.coi.1042'
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(url)

            imgab = ImageTk.PhotoImage(
                Image.open(r"Help\aboutus.jpg"))
            l2 = tk.Label(aw, image=imgab)
            l2.pack()
            qa = tk.Button(aw, text="Back", font=("Helvetica", 20), command=aw.destroy).pack()
            qb = tk.Button(aw, text="Go to my page", font=("Helvetica", 20), command=lambda: openfb()).pack()


        self.menutaskbar = tk.Menu(master=self)
        self.config(menu = self.menutaskbar)

        file_menu = tk.Menu(self.menutaskbar)
        self.menutaskbar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Home", command =lambda :self.show_frame(mainscreen) )
        file_menu.add_command(label="Open" )
        file_menu.add_command(label="Exit",command = self.quit)

        option_menu = tk.Menu(self.menutaskbar)
        self.menutaskbar.add_cascade(label="Option", menu=option_menu)
        option_menu.add_command(label="Font", )
        option_menu.add_command(label="Size",)
        option_menu.add_command(label="Colour", )
        option_menu.add_command(label="Change saved squad location", command = changelocation)

        help_menu = tk.Menu(self.menutaskbar)
        self.menutaskbar.add_command(label="Help", command= helpwindow)

        aboutus_menu = tk.Menu(self.menutaskbar)
        self.menutaskbar.add_command(label="About me", command= aboutuswindow)

        # creating a window
        window = tk.Frame(self)
        window.place(x=0,y=0)

        window.grid_rowconfigure(0, minsize=600)
        window.grid_columnconfigure(0, minsize=450)

        self.frames = {}
        for F in (mainscreen, SecondPage, Form, SecondPage2,MediatePage,LibraryPage,PlayerPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(mainscreen)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Dream Team Maker")
        self.iconbitmap(r'iconbitmap\icon.ico')

#Run app
app = Application()
app.minsize(450,600)
app.maxsize(450,600)
app.mainloop()
