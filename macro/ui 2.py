import pyfirmata
import json
import time
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import os
from multiprocessing import Process
import keyboard
import pyautogui, sys
import threading
import fileinput
import re 
import psutil


file = open('config.json','r+')
json_dict = json.load(file)
json_dict["CodeButton1"]=0
file.close()





def func1():




    window = Tk()
    window.title("")
    window.geometry('600x300')
    #window.wm_iconbitmap(r'lol.ico')
    window.configure(background="red")

    colourstyle = Style()

    #colourstyle.configure("TNotebook", background="red",foreground="blue")
    #colourstyle.configure("TFrame", background="red",foreground="blue")
    colourstyle.configure('Custom.TNotebook.Tab',padding=[45, 0], font=('Impact', 20, "bold"),background="red",foreground="#4dacff")
    #Style().map("Custom.TNotebook.Tab",
        #foreground=[("selected", "yellow"), ("active", "blue")],
        #background=[("selected", "!disabled", "pink"), ("active", "purple")])
    
    def focus(event): 
        print(window.focus_get())
        widget = tab2.focus_get() 
        tab2.focus_set()
    ###### 
    #TABS#
    ######

    def _on_frame_configure(self, event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))

    tab_parent = ttk.Notebook(window,style='Custom.TNotebook')

    def callback(event):
            print("test")

    tab1 = ttk.Frame(tab_parent)
    tab_parent.add(tab1, text="Ⓒreate")




    #CODE INPUT
    








    #title

    title = Entry(tab1)
    title.place(x=1, y=1,width=398)
    title.insert(0,"NEEDS TITLE")





    createeentry = Text(tab1)
    createeentry.place(width=399,height=120, x=1, y=25)


    def windowopen():
        createeentry.delete('1.0', END)
        createeentry.insert(1.0,"")

    openwindow = Button(tab1, text="Open", command=windowopen)
    openwindow.place(x=400,y=0)





    def create():

        if title.get() =="NEEDS TITLE":
            return
        else:
#$$\      $$\  $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  
#$$$\    $$$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
#$$$$\  $$$$ |$$ /  $$ |$$ /  \__|$$ |  $$ |$$ /  $$ |
#$$\$$\$$ $$ |$$$$$$$$ |$$ |      $$$$$$$  |$$ |  $$ |
#$$ \$$$  $$ |$$  __$$ |$$ |      $$  __$$< $$ |  $$ |
#$$ |\$  /$$ |$$ |  $$ |$$ |  $$\ $$ |  $$ |$$ |  $$ |
#$$ | \_/ $$ |$$ |  $$ |\$$$$$$  |$$ |  $$ | $$$$$$  |
#\__|     \__|\__|  \__| \______/ \__|  \__| \______/ 

            filetot = len([iq for iq in os.scandir('macro/')])
            maxe = int(filetot)+1

            #print(len([iq for iq in os.scandir('Macro/')]))


            finaltwo = open("macro/"+str(maxe)+".txt", "x")
            with open('template2.txt','r+') as f:
                text = f.read()
                text =text.replace('REPLACE',createeentry.get("1.0",'end-1c'))
            
            
            with open("macro/"+str(maxe)+".txt", "w+") as f:
                f.write(text)

#$$\                   $$\     $$\                         
#$ |                  $$ |    $$ |                        
#$$$$$$$\  $$\   $$\ $$$$$$\ $$$$$$\    $$$$$$\  $$$$$$$\  
#$$  __$$\ $$ |  $$ |\_$$  _|\_$$  _|  $$  __$$\ $$  __$$\ 
#$$ |  $$ |$$ |  $$ |  $$ |    $$ |    $$ /  $$ |$$ |  $$ |
#$$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |$$\ $$ |  $$ |$$ |  $$ |
#$$$$$$$  |\$$$$$$  |  \$$$$  |\$$$$  |\$$$$$$  |$$ |  $$ |
#\_______/  \______/    \____/  \____/  \______/ \__|  \__|



           

            #template = open("template.txt","r")
            #final = open("button/"+title.get()+".txt","x")
            
            #button/"+title.get()+".txt"

            with open('template.txt','r+') as f:
                text = f.read()
                text =text.replace('def i():','def g'+str(maxe)+'():')
                text =text.replace('json_dict["CodeButton1"]=i', 'json_dict["CodeButton1"]='+str(maxe))
                text =text.replace('json_dict["CodeButton2"]=i', 'json_dict["CodeButton2"]='+str(maxe))
                text =text.replace('json_dict["CodeButton3"]=i', 'json_dict["CodeButton3"]='+str(maxe))
                text =text.replace('i.button = Button(frame, text="Open Chrome",command=i, width=20,style="C.TButton")', 'button'+str(maxe)+' = Button(frame, text='+"\""+title.get()+"\""+',command='+"g"+str(maxe)+', width=20,style='+"\""+str(maxe)+".TButton"+"\""+')')
                text =text.replace('i.button.grid(column=i, row=i,sticky=W) ', 'button'+str(maxe)+'.grid(column=0, row='+str(maxe)+',sticky=W)')
                text =text.replace('','')
                text =text.replace('if json_dict["Select1"]==0:','if json_dict['+"\""+str(maxe)+"json"+"\""']==0:')
                text =text.replace('if json_dict["Select1"]==1:','if json_dict['+"\""+str(maxe)+"json"+"\""']==1:')
                text =text.replace('json_dict["Select1"]=1','json_dict['+"\""+str(maxe)+"json"+"\""']=1')
                text =text.replace('json_dict["Select1"]=0','json_dict['+"\""+str(maxe)+"json"+"\""']=0')
                text =text.replace('style.configure("C.TButton", foreground="black", background="red")','style.configure('+"\""+str(maxe)+".TButton"+"\""+', foreground="black", background="red")')
                text =text.replace('style.configure("C.TButton", foreground="black", background="blue")','style.configure('+"\""+str(maxe)+".TButton"+"\""+',  foreground="black", background="blue")')
                text =text.replace('style.configure("C.TButton", foreground="black", background="green")','style.configure('+"\""+str(maxe)+".TButton"+"\""+', foreground="black", background="green")')
                text =text.replace('style.configure("C.TButton", foreground="black", background="white")','style.configure('+"\""+str(maxe)+".TButton"+"\""+' ,foreground="black", background="white")')
                text =text.replace('style.configure("C.TButton", foreground="black", background=OneSelectColour)','style.configure('+"\""+str(maxe)+".TButton"+"\""+', foreground="black", background=OneSelectColour)')
                text =text.replace('def d():','def d'+str(maxe)+'():')
                #text =text.replace('C.TButton.destroy()',''+str(maxe)+'.TButton.destroy()')
                text =text.replace('os.remove("Macro/i.txt")','os.remove("Macro/'+str(maxe)+'.txt")')
                text =text.replace('os.remove("Button/test.txt")','os.remove("Button/'+str(title.get())+'.txt")')
                text =text.replace('i.delbutton = Button(frame, text="X",command=i, width=5,style="C.TButton")', 'delbutton'+str(maxe)+' = Button(frame, text="X",command='+"d"+str(maxe)+', width=20,style='+"\""+str(maxe)+".TButton"+"\""+')')
                text =text.replace('i.delbutton.grid(column=i, row=i,sticky=W) ', 'delbutton'+str(maxe)+'.grid(column=1, row='+str(maxe)+',sticky=W)')

                jfile = open('config.json','r+')
                json_dict = json.load(jfile)

                json_dict[str(maxe)+"json"]=0
                jfile.seek(0)
                json.dump(json_dict,jfile, indent=4)
                jfile.truncate()
                jfile.close()


                    #final.write(line)
    

            with open("button/"+title.get()+".txt","w+") as f:
                f.write(text)
            window.destroy()
            func1()




    Createbutton = Button(tab1,text="Create",command=create)
    Createbutton.place(x=1,y=150)


    tab2 = ttk.Frame(tab_parent)
    tab_parent.add(tab2, text="Ⓒurrent")


    frame = Frame(tab2,borderwidth=0)
    frame.grid(column=0, row=0, sticky=N+S+E+W)


    yscrollbar = Scrollbar(frame)
    yscrollbar.grid(column=1, row=0, sticky=N+S)

    canvas = Canvas(frame, bd=0, yscrollcommand=yscrollbar.set, width=167)
    canvas.grid(column=0, row=0, sticky=N+S+E+W)

    yscrollbar.config(command=canvas.yview)

    frame = Frame(canvas,borderwidth=0)
    canvas.create_window(4, 4, window=frame, anchor='nw')
    frame.bind("<Configure>", _on_frame_configure)

 


    for i in range(30):
        for top, dirs, files in os.walk('Button'):
            for macro in files:
                f = open("Button/"+os.path.join(macro),'r')       
                #return(os.path.join(macro))
                content = f.read()
                exec(content)
                f.close()

    def MainSelectOne():
        file = open('config.json','r+')
        json_dict = json.load(file)
        json_dict["MainSelectOne"]=1
        json_dict["MainSelectTwo"]=0
        json_dict["MainSelectthree"]=0
        file.seek(0)
        json.dump(json_dict,file, indent=4)
        file.truncate()
        file.close()
    def MainSelectTwo():
        file = open('config.json','r+')
        json_dict = json.load(file)
        json_dict["MainSelectOne"]=0
        json_dict["MainSelectTwo"]=1
        json_dict["MainSelectthree"]=0
        file.seek(0)
        json.dump(json_dict,file, indent=4)
        file.truncate()
        file.close()
    def MainSelectThree():
        file = open('config.json','r+')
        json_dict = json.load(file)
        json_dict["MainSelectOne"]=0
        json_dict["MainSelectTwo"]=0
        json_dict["MainSelectthree"]=1
        file.seek(0)
        json.dump(json_dict,file, indent=4)
        file.truncate()
        file.close()

    rad1 = Radiobutton(tab2,text='Button 1', value=1,command=MainSelectOne)
    rad1.grid(column=1, row=0,sticky=E+N)




    tab_parent.pack(expand=1,fill="both")

    

    

    window.bind_all("<Button-1>", lambda e: focus(e)) 
    window.mainloop()
 


def func2():
    file = open('config.json','r+')
    json_dict = json.load(file)
    board = pyfirmata.Arduino('COM3')
    it = pyfirmata.util.Iterator(board)
    it.start()
    board.digital[2].mode = pyfirmata.INPUT
    Button1filefolder = open("Macro/"+str(json_dict["CodeButton1"])+".txt", "r")
    b1read = Button1filefolder.read()
    while True:
        sw = board.digital[2].read()
        if sw is True:
            Button1filefolder = open("Macro/"+str(json_dict["CodeButton1"])+".txt", "r")
            b1read = Button1filefolder.read()
            file = open('config.json','r+')
            json_dict = json.load(file)
            if json_dict[str(json_dict["CodeButton1"])+"json"]==1:
                exec(b1read)
            else:
                print("its okay man it works <3")
        time.sleep(0.1)



    Button1filefolder.close()
    file.close()


        
if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p1.join()
    p2.join()
















