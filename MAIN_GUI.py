# -*- coding: utf-8 -*-
import os, sys, inspect
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2 ** 32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap
import Tkinter
from Tkinter import *
from PIL import Image, ImageTk
import MAIN_ALGO
from hangul_utils import split_syllables, join_jamos
import webbrowser
import Sensitivity
from keras.models import model_from_json
import numpy as np

predict_data = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "float32")  # 적용 데이터
Dynamic_predict_data = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
        "float32")

# load json and create model
json_file = open('model.json', 'r')
json_file2 = open('Dynamic_model.json', 'r')
json_file3 = open('Number_model.json', 'r')
json_file4 = open('One_Dynamic_model.json', 'r')
loaded_model_json = json_file.read()
loaded_model_json2 = json_file2.read()
loaded_model_json3 = json_file3.read()
loaded_model_json4 = json_file4.read()
json_file.close()
json_file2.close()
json_file3.close()
json_file4.close()
model = model_from_json(loaded_model_json)
Dynamic_model = model_from_json(loaded_model_json2)
Number_model = model_from_json(loaded_model_json3)
One_Dynamic_model = model_from_json(loaded_model_json4)
    # load weights into new model
model.load_weights("model.h5")
Dynamic_model.load_weights("Dynamic_model.h5")
Number_model.load_weights("Number_model.h5")
One_Dynamic_model.load_weights("One_Dynamic_model.h5")
print("Loaded model from disk")



static_value = [""]


class PaintBox(Frame):
    middle_font = ('Verdana', 18)
    large_font = ('Verdana', 25)

    paintCanvas = Canvas(width="600", height="450")



    def Switch_Dynamic(self, event):
        MAIN_ALGO.TouchPointListener.Dynamic_Flag = 1
        MAIN_ALGO.TouchPointListener.Static_Flag = 0
        MAIN_ALGO.TouchPointListener.Number_Flag = 0
        mycolor = '#%02x%02x%02x' % (222, 235, 247)
        self.Mode = Label(text="수화 MODE",bg=mycolor)
        self.Two_Mode = PhotoImage(file="../image/Two_Mode.gif")
        self.Mode.config(image=self.Two_Mode)
        self.Mode.pack()
        self.Mode.place(x=685, y=20)
        print "수화모드"

    def Switch_Static(self, event):
        MAIN_ALGO.TouchPointListener.Dynamic_Flag = 0
        MAIN_ALGO.TouchPointListener.Static_Flag = 1
        MAIN_ALGO.TouchPointListener.Number_Flag = 0
        mycolor = '#%02x%02x%02x' % (222, 235, 247)
        self.Mode = Label(text="지화 MODE",bg=mycolor)
        self.One_Mode = PhotoImage(file="../image/One_Mode.gif")
        self.Mode.config(image=self.One_Mode)
        self.Mode.pack()
        self.Mode.place(x=685, y=20)
        print "지화 모드"

    def Switch_Num(self, event):
        MAIN_ALGO.TouchPointListener.Dynamic_Flag = 0
        MAIN_ALGO.TouchPointListener.Static_Flag = 0
        MAIN_ALGO.TouchPointListener.Number_Flag = 1
        mycolor = '#%02x%02x%02x' % (222, 235, 247)
        self.Mode = Label(text="숫자 MODE", bg=mycolor)
        self.Num_Mode = PhotoImage(file="../image/Num_Mode.gif")
        self.Mode.config(image=self.Num_Mode)
        self.Mode.pack()
        self.Mode.place(x=685, y=20)
        print "숫자 모드"

    def delete(self,event):
        MAIN_ALGO.TouchPointListener.LB.delete(0, END)

    def Send_Click(self, event):
        if not self.static_value == [""]:
            restored_text = join_jamos(self.static_value)
            print(restored_text)
            self.LB.insert(END, restored_text)
            self.LB.see("end")
            self.static_value = [""]
            self.v2 = StringVar(value=restored_text)
            self.txt = Entry(textvariable=self.v2, font=self.large_font, width=21)

            self.txt.place(x=700, y=560)
            self.txt.delete(0, 'end')

        else:
            print "nothing"

    def callback(self, event):
        webbrowser.open_new(r"http://handstalk.co.kr")

    def __init__(self):
        Frame.__init__(self)
        self.leap = Leap.Controller()
        self.painter = MAIN_ALGO.TouchPointListener()
        self.leap.add_listener(self.painter)
        self.grid(row=0, column=0)

        self.master.title("HandsTalk")
        self.master.geometry("1400x650")
        mycolor = '#%02x%02x%02x' % (222, 235, 247)
        self.master.configure(background=mycolor)

        # create Canvas component

        self.paintCanvas.configure(background='white')
        self.paintCanvas.pack(padx=45, pady=100)
        self.paintCanvas.place(x=45,y=100)

        self.painter.set_canvas(self.paintCanvas)





        self.Send_Button = Button(text="OK", background=mycolor,borderwidth=0,activebackground=mycolor,)
        self.send_image = PhotoImage(file="../image/send.gif")
        self.Send_Button.config(image=self.send_image)
        self.Send_Button.pack()
        self.Send_Button.bind("<Button-1>", self.Send_Click)
        self.Send_Button.place(x=1195 ,y=540)

        self.ST_Button = Button(text="인식속도 ↓", background=mycolor,borderwidth=0,activebackground=mycolor,)
        self.sense_down_image = PhotoImage(file="../image/sense_down.gif")
        self.ST_Button.config(image=self.sense_down_image)
        self.ST_Button.pack()
        self.ST_Button.bind("<Button-1>", Sensitivity.Sense_Up)
        self.ST_Button.place(x=990, y=20)

        self.ST_Button2 = Button(text="인식속도 ↑", background=mycolor,borderwidth=0,activebackground=mycolor,)
        self.sense_up_image = PhotoImage(file="../image/sense_up.gif")
        self.ST_Button2.config(image=self.sense_up_image)
        self.ST_Button2.pack()
        self.ST_Button2.bind("<Button-1>", Sensitivity.Sense_Down)
        self.ST_Button2.place(x=1165, y=20)

        self.SWITCH_Button = Button(text="수화 하기", background=mycolor,borderwidth=0,activebackground=mycolor,  height = 140, width = 140)
        self.Hand_Image = PhotoImage(file="../image/Two_Hands.gif")
        self.SWITCH_Button.config(image=self.Hand_Image)
        self.SWITCH_Button.pack()
        self.SWITCH_Button.bind("<Button-1>", self.Switch_Dynamic)
        self.SWITCH_Button.place(x=1200, y=90)

        self.SWITCH_Button2 = Button(text="지화 하기",  background=mycolor,borderwidth=0,activebackground=mycolor, height = 140, width = 140)
        self.Hand_Image2 = PhotoImage(file="../image/One_Hand.gif")
        self.SWITCH_Button2.config(image=self.Hand_Image2)
        self.SWITCH_Button2.pack()
        self.SWITCH_Button2.bind("<Button-1>", self.Switch_Static)
        self.SWITCH_Button2.place(x=1200, y=240)

        self.SWITCH_Button3 = Button(text="숫자 쓰기", background=mycolor,borderwidth=0, height = 140, width = 140)
        self.Num_Image = PhotoImage(file="../image/Number.gif")
        self.SWITCH_Button3.config(image=self.Num_Image)
        self.SWITCH_Button3.pack()
        self.SWITCH_Button3.bind("<Button-1>", self.Switch_Num)
        self.SWITCH_Button3.place(x=1200, y=390)



        self.v2 = StringVar(value="")
        self.txt = Entry(textvariable=self.v2, font=self.large_font, width=21)
        self.txt.xview_moveto(1)
        self.txt.place(x=700, y=550)



        self.Mode = Label(text="지화 MODE", bg=mycolor)
        self.One_Mode = PhotoImage(file="../image/One_Mode.gif")
        self.Mode.config(image=self.One_Mode)
        self.Mode.pack()
        self.Mode.place(x=685, y=20)

        self.team_logo = Button(background=mycolor, borderwidth=0,
                                  activebackground=mycolor,
                                  )
        self.team_logo_image = PhotoImage(file="../image/team_logo.gif")
        self.team_logo.config(image=self.team_logo_image)
        self.team_logo.pack()
        self.team_logo.bind("<Button-1>", self.delete)
        self.team_logo.place(x=160, y=570)

        self.Logo_Button = Button(text="Handstalk HomePage", background=mycolor, borderwidth=0, activebackground=mycolor,
                                     height=40, width=300)
        self.handstalk_Image = PhotoImage(file="../image/handstalk_image.gif")
        self.Logo_Button.config(image=self.handstalk_Image)
        self.Logo_Button.pack()
        self.Logo_Button.bind("<Button-1>", self.callback)
        self.Logo_Button.place(x=200, y=30)

        self.link = Label(text="HandsTalk HomePage", fg="blue", bg=mycolor)
        self.link.pack()
        self.link.bind("<Button-1>", self.callback)
        self.link.place(x=1207, y=620)



def main():
    PaintBox().mainloop()


if __name__ == "__main__":


    # evaluate loaded model on test data


    main()
