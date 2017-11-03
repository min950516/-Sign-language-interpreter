# -*- coding: utf-8 -*-
from Tkinter import *
import time
import os, sys, inspect

import Send_Message

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2 ** 32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap

import numpy as np
from gtts import gTTS
import playsound
from hangul_utils import split_syllables, join_jamos
from operator import eq
import Draw_Function
import Sensitivity
import pygame

import MAIN_GUI

pygame.mixer.init()
pygame.mixer.music.load("song.mp3")
a = pygame.mixer.Sound("clap.wav")
a2 = pygame.mixer.Sound("eva_call_end.wav")

mycolor = '#%02x%02x%02x' % (222, 235, 247)
recog_color = '#%02x%02x%02x' % (157, 195 ,230)
class TouchPointListener(Leap.Listener):
    middle_font = ('Verdana', 18)
    LB = Listbox(width=30, height=14)
    SB = Scrollbar(orient=VERTICAL)
    LB.config(yscrollcommand=SB.set, font=middle_font)
    SB.config(command=LB.yview)
    SB.pack(side=RIGHT, fill=Y)
    LB.pack(side=LEFT, fill=BOTH, expand=Y)
    SB.place(x=1150, y=100)
    LB.place(x=700, y=100)

    WORD = Label(text="예상단어: ", bg=mycolor, fg="RoyalBlue3", font="Helvetica 15 bold")
    WORD.pack()
    WORD.place(x=700, y=605)

    Dynamic_Flag = 0
    Static_Flag = 1
    Number_Flag = 0

    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0
    S11 = 0
    S12 = 0
    S13 = 0
    S14 = 0
    S15 = 0
    S16 = 0
    S17 = 0
    S18 = 0
    S19 = 0
    S20 = 0
    S21 = 0
    S22 = 0
    S23 = 0
    S24 = 0
    S25 = 0
    S26 = 0
    S27 = 0
    S28 = 0
    S29 = 0
    S30 = 0
    S31 = 0
    S32 = 0
    S33 = 0

    nice = 0
    meet = 0
    sorry = 0
    funny = 0
    like = 0
    clear_var = 0
    love = 0
    fact = 0
    very = 0
    hungry = 0
    thank = 0
    hello = 0
    regretful = 0
    thank2 = 0

    but = 0
    but2 = 0

    what = 0
    eat = 0
    eat2 = 0
    fine = 0
    sleep = 0
    tomorrow = 0
    forward = 0
    delicious = 0
    food = 0
    team = 0
    senior = 0
    junior = 0
    well = 0
    well2 = 0
    dokdo = 0
    grand = 0
    evaluate = 0
    coach = 0
    sir = 0

    noon = 0
    night = 0
    meat = 0
    do = 0
    donot = 0
    connect = 0
    nicetomeet = 0
    no = 0
    now = 0
    byebye = 0
    time = 0
    is_16 = 0

    buy = 0
    buy2 = 0
    weather = 0
    weather2 = 0
    today = 0
    this1 = 0
    please = 0
    because = 0
    name = 0
    yes = 0
    me = 0
    we = 0
    rank = 0
    hope = 0
    question = 0
    question2 = 0
    different = 0
    be = 0
    hate = 0
    lee = 0
    shin = 0
    seo = 0
    sensitive = 20

    money = 0
    everyone = 0
    learn = 0
    give = 0

    support = 0
    receive = 0
    cellphone = 0
    clap = 0
    signlang = 0
    teach = 0
    hard = 0
    happy = 0
    baseball = 0
    eman = 0
    sk = 0

    predict_data = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "float32")  # 적용 데이터
    Dynamic_predict_data = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
        "float32")
    direction_index = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 손 그리기 위한 방향 배열 만든 후 삽입
    wrist_index = [0, 0, 0]  # 손목 방향 pitch,yaw,roll

    def on_init(self, controller):
        print "Initialized"

    def Label_UPDATE(self):
            large_font = ('Verdana', 25)
            restored_text = join_jamos(MAIN_GUI.static_value)
            print(restored_text)
            # self.v2 = StringVar(value=json.dumps(MAIN_GUI.static_value, ensure_ascii=False))
            self.v2 = StringVar(value=restored_text)
            self.txt = Entry(textvariable=self.v2, font=large_font)
            self.txt.xview_moveto(1)
            self.txt.place(x=700, y=550)

            mycolor = '#%02x%02x%02x' % (222, 235, 247)
            self.WORD.config(text="예상단어: ", bg=mycolor)

    def initializeVal(self):
        self.one = 0
        self.two = 0
        self.three = 0
        self.four = 0
        self.five = 0
        self.six = 0
        self.seven = 0
        self.eight = 0
        self.nine = 0
        self.ten = 0
        self.S11 = 0
        self.S12 = 0
        self.S13 = 0
        self.S14 = 0
        self.S15 = 0
        self.S16 = 0
        self.S17 = 0
        self.S18 = 0
        self.S19 = 0
        self.S20 = 0
        self.S21 = 0
        self.S22 = 0
        self.S23 = 0
        self.S24 = 0
        self.S25 = 0
        self.S26 = 0
        self.S27 = 0
        self.S28 = 0
        self.S29 = 0
        self.S30 = 0
        self.S31 = 0
        self.S32 = 0
        self.S33 = 0

        self.eat = 0
        self.eat2 = 0
        self.nice = 0
        self.meet = 0
        self.sorry = 0
        self.funny = 0
        self.like = 0
        self.very = 0
        self.fact = 0
        self.love = 0
        self.hungry = 0
        self.thank = 0
        self.thank2 = 0
        self.hello = 0
        self.regretful = 0
        self.do = 0
        self.donot = 0
        self.connect = 0
        self.but = 0
        self.but2 = 0
        self.noon = 0
        self.night = 0
        self.meat = 0
        self.this1 = 0
        self.what = 0

        self.fine = 0
        self.sleep = 0
        self.tomorrow = 0
        self.forward = 0
        self.delicious = 0
        self.food = 0
        self.different = 0
        self.nicetomeet = 0
        self.no = 0
        self.now = 0
        self.byebye = 0
        self.time = 0
        self.is_16 = 0
        self.eat = 0
        self.me = 0
        self.we = 0
        self.buy = 0
        self.buy2 = 0
        self.weather = 0
        self.weather2 = 0
        self.today = 0

        self.name = 0
        self.yes = 0
        self.we = 0
        self.rank = 0
        self.hope = 0
        self.team = 0
        self.senior = 0
        self.junior = 0
        self.well = 0
        self.well2 = 0
        self.dokdo = 0
        self.grand = 0
        self.evaluate = 0
        self.coach = 0
        self.sir = 0
        self.question = 0
        self.question2 = 0
        self.be = 0
        self.hate = 0
        self.lee = 0
        self.shin = 0
        self.seo = 0
        self.please = 0
        self.because = 0
        self.sk = 0
        self.money = 0
        self.everyone = 0
        self.learn = 0
        self.give = 0

        self.support = 0
        self.receive = 0
        self.cellphone = 0
        self.clap = 0
        self.signlang = 0
        self.teach = 0
        self.hard = 0
        self.happy = 0
        self.baseball = 0
        self.eman = 0

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        # self.paintCanvas.delete("all")
        time.sleep(0.01)
        frame = controller.frame()

        self.paintCanvas.delete("all")
        left = 0
        right = 0
        interactionBox = frame.interaction_box
        point_count = 0

        # Get hands
        for hand in frame.hands:
            for pointable in frame.pointables:
                direction = pointable.direction  # 손가락 마다의 방향 지시
                handType = "Left hand" if pointable.hand.is_left else "Right hand"
                if len(frame.pointables) == 10:
                    if handType == "Left hand" and left % 5 == 0:
                        thumb = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][3] = float(thumb / 180)
                        thumb2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][4] = float(thumb2 / 180)
                        thumb3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][5] = float(thumb3 / 180)
                        left += 1
                    elif handType == "Left hand" and left % 5 == 1:
                        Index = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][6] = float(Index / 180)
                        Index2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][7] = float(Index2 / 180)
                        Index3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][8] = float(Index3 / 180)
                        left += 1
                    elif handType == "Left hand" and left % 5 == 2:
                        Middle = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][9] = float(Middle / 180)
                        Middle2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][10] = float(Middle2 / 180)
                        Middle3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][11] = float(Middle3 / 180)
                        left += 1
                    elif handType == "Left hand" and left % 5 == 3:
                        Ring = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][12] = float(Ring / 180)
                        Ring2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][13] = float(Ring2 / 180)
                        Ring3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][14] = float(Ring3 / 180)
                        left += 1
                    elif handType == "Left hand" and left % 5 == 4:
                        Pinky = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][15] = float(Pinky / 180)
                        Pinky2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][16] = float(Pinky2 / 180)
                        Pinky3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][17] = float(Pinky3 / 180)
                        left += 1
                    if handType == "Right hand" and right % 5 == 0:
                        thumb = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][18] = float(thumb / 180)
                        thumb2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][19] = float(thumb2 / 180)
                        thumb3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][20] = float(thumb3 / 180)
                        right += 1
                    elif handType == "Right hand" and right % 5 == 1:
                        Index = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][21] = float(Index / 180)
                        Index2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][22] = float(Index2 / 180)
                        Index3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][23] = float(Index3 / 180)
                        right += 1
                    elif handType == "Right hand" and right % 5 == 2:
                        Middle = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][24] = float(Middle / 180)
                        Middle2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][25] = float(Middle2 / 180)
                        Middle3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][26] = float(Middle3 / 180)
                        right += 1
                    elif handType == "Right hand" and right % 5 == 3:
                        Ring = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][27] = float(Ring / 180)
                        Ring2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][28] = float(Ring2 / 180)
                        Ring3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][29] = float(Ring3 / 180)
                        right += 1
                    elif handType == "Right hand" and right % 5 == 4:
                        Pinky = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][30] = float(Pinky / 180)
                        Pinky2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][31] = float(Pinky2 / 180)
                        Pinky3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.Dynamic_predict_data[0][32] = float(Pinky3 / 180)
                        right += 1

                if len(frame.pointables) == 5:
                    if point_count % 5 == 0:
                        thumb = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][3] = float(thumb / 180)
                        thumb2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][4] = float(thumb2 / 180)
                        thumb3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][5] = float(thumb3 / 180)
                    if point_count % 5 == 1:
                        Index = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][6] = float(Index / 180)
                        Index2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][7] = float(Index2 / 180)
                        Index3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][8] = float(Index3 / 180)
                    if point_count % 5 == 2:
                        Middle = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][9] = float(Middle / 180)
                        Middle2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][10] = float(Middle2 / 180)
                        Middle3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][11] = float(Middle3 / 180)
                    if point_count % 5 == 3:
                        Ring = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][12] = float(Ring / 180)
                        Ring2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][13] = float(Ring2 / 180)
                        Ring3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][14] = float(Ring3 / 180)
                    if point_count % 5 == 4:
                        Pinky = float(direction[0] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][15] = float(Pinky / 180)
                        Pinky2 = float(direction[1] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][16] = float(Pinky2 / 180)
                        Pinky3 = float(direction[2] * Leap.RAD_TO_DEG)
                        MAIN_GUI.predict_data[0][17] = float(Pinky3 / 180)

                point_count += 1
            finger_count = 0
            arm = hand.arm
            self.wrist_index[0] = interactionBox.normalize_point(arm.wrist_position)
            # self.drawPoint(self.wrist_index[0].x * 600, 400 - self.wrist_index[0].y * 400, 20, 20, color="light Gray")
            for finger in hand.fingers:
                for b in range(0, 4):
                    bone = finger.bone(b)
                    if b == 1 and finger_count == 0:
                        self.direction_index[0] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and finger_count == 0:
                        self.direction_index[1] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and finger_count == 1:
                        self.direction_index[2] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and finger_count == 2:
                        self.direction_index[3] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and finger_count == 3:
                        self.direction_index[4] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and finger_count == 4:
                        self.direction_index[5] = interactionBox.normalize_point(bone.next_joint)
                        Draw_Function.drawRect(self, self.direction_index[0].x * 600,
                                               400 - self.direction_index[0].y * 400,
                                               self.direction_index[1].x * 600, 400 - self.direction_index[1].y * 400,
                                               self.direction_index[2].x * 600, 400 - self.direction_index[2].y * 400,
                                               self.direction_index[3].x * 600, 400 - self.direction_index[3].y * 400,
                                               self.direction_index[4].x * 600, 400 - self.direction_index[4].y * 400,
                                               self.direction_index[5].x * 600,
                                               400 - self.direction_index[5].y * 400, self.wrist_index[0].x * 600,
                                               400 - self.wrist_index[0].y * 400)  # 손바닥 그리기

                    if b == 1 and finger_count == 5:
                        self.direction_index[6] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and finger_count == 5:
                        self.direction_index[7] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and finger_count == 6:
                        self.direction_index[8] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and finger_count == 7:
                        self.direction_index[9] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and finger_count == 8:
                        self.direction_index[10] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and finger_count == 9:
                        self.direction_index[11] = interactionBox.normalize_point(bone.next_joint)
                        Draw_Function.drawRect(self, self.direction_index[6].x * 600,
                                               400 - self.direction_index[6].y * 400,
                                               self.direction_index[7].x * 600, 400 - self.direction_index[7].y * 400,
                                               self.direction_index[8].x * 600, 400 - self.direction_index[8].y * 400,
                                               self.direction_index[9].x * 600, 400 - self.direction_index[9].y * 400,
                                               self.direction_index[10].x * 600, 400 - self.direction_index[10].y * 400,
                                               self.direction_index[11].x * 600,
                                               400 - self.direction_index[11].y * 400, self.wrist_index[0].x * 600,
                                               400 - self.wrist_index[0].y * 400)

                    normalbone = interactionBox.normalize_point(bone.prev_joint)
                    normalbone2 = interactionBox.normalize_point(bone.next_joint)

                    # self.drawPoint(normalbone.x * 600, 400 - normalbone.y * 400, 20, 20, color="light Gray")
                    if not b == 0:
                        Draw_Function.drawLine(self, normalbone.x * 600, 400 - normalbone.y * 400, normalbone2.x * 600,
                                               400 - normalbone2.y * 400)
                finger_count += 1
            handType = "Left hand" if hand.is_left else "Right hand"

            normal = hand.palm_normal
            direction = hand.direction

            if handType == "Left hand":
                pitch = float(direction.pitch * Leap.RAD_TO_DEG)
                MAIN_GUI.predict_data[0][0] = float(float(pitch) / float(180))
                roll = float(normal.roll * Leap.RAD_TO_DEG)
                MAIN_GUI.predict_data[0][1] = float(roll / 180)
                yaw = float(direction.yaw * Leap.RAD_TO_DEG)
                MAIN_GUI.predict_data[0][2] = float(yaw / 180)

                MAIN_GUI.Dynamic_predict_data[0][0] = float(float(pitch) / float(180))
                MAIN_GUI.Dynamic_predict_data[0][1] = float(roll / 180)
                MAIN_GUI.Dynamic_predict_data[0][2] = float(yaw / 180)


            elif handType == "Right hand":
                pitch = float(direction.pitch * Leap.RAD_TO_DEG)
                MAIN_GUI.predict_data[0][0] = float(float(pitch) / float(180))
                roll = float(normal.roll * Leap.RAD_TO_DEG)
                MAIN_GUI.predict_data[0][1] = float(roll / 180)
                yaw = float(direction.yaw * Leap.RAD_TO_DEG)
                MAIN_GUI.predict_data[0][2] = float(yaw / 180)

                MAIN_GUI.Dynamic_predict_data[0][33] = float(float(pitch) / float(180))
                MAIN_GUI.Dynamic_predict_data[0][34] = float(roll / 180)
                MAIN_GUI.Dynamic_predict_data[0][35] = float(yaw / 180)

            if handType == "Right hand" and len(frame.hands) == 1 and self.Static_Flag == 1:

                try:
                    if not len(frame.hands) == 0:

                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [0] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][0] > 0.9:
                            if self.one == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㄱ 저장완료"
                                MAIN_GUI.static_value.append(u"ㄱ")
                                self.paintCanvas.configure(background=recog_color)

                                pygame.mixer.music.play()

                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.one += 1
                            print self.one
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [1] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][1] > 0.9:

                            if self.two == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)

                                print "ㄴ 저장완료"
                                MAIN_GUI.static_value.append(u"ㄴ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.two += 1
                            print self.two
                            print "!!!!!!!!!!!!!!!!!!!!!!!"
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [2] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][2] > 0.9:
                            if self.three == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㄷ 저장완료"
                                MAIN_GUI.static_value.append(u"ㄷ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.Label_UPDATE()
                                self.initializeVal()
                            self.three += 1
                            print self.three
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [3] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][3] > 0.9:
                            if self.four == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print MAIN_GUI.model.predict(MAIN_GUI.predict_data)
                                print "ㄹ 저장완료"
                                MAIN_GUI.static_value.append(u"ㄹ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.four += 1
                            print self.four
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [4] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][4] > 0.9:
                            if self.five == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)

                                print "ㅁ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅁ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.five += 1
                            print self.four
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [5] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][5] > 0.9:
                            if self.six == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)

                                print "ㅂ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅂ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.six += 1
                            print self.six
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [6] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][6] > 0.9:
                            if self.seven == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)

                                print "ㅅ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅅ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.seven += 1
                            print self.seven
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [7] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][7] > 0.9:
                            if self.eight == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)

                                print "ㅇ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅇ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.eight += 1
                            print self.eight
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [8] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][8] > 0.9:
                            if self.nine == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)

                                print "ㅈ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅈ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.nine += 1
                            print self.nine
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [9] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][9] > 0.9:
                            if self.ten == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅊ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅊ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.ten += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [10] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][10] > 0.9:
                            if self.S11 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅋ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅋ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S11 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [11] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][11] > 0.9:
                            if self.S12 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅌ 저장완료"
                                print MAIN_GUI.model.predict(MAIN_GUI.predict_data)
                                MAIN_GUI.static_value.append(u"ㅌ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S12 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [12] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][12] > 0.9:
                            if self.S13 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅍ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅍ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S13 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [13] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][13] > 0.9:
                            if self.S14 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅎ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅎ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S14 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [14] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][14] > 0.9:
                            if self.S15 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅏ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅏ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S15 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [15] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][15] > 0.9:
                            if self.S16 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅑ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅑ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S16 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [16] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][16] > 0.9:
                            if self.S17 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅓ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅓ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S17 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [17] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][17] > 0.9:
                            if self.S18 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅕ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅕ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S18 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [18] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][18] > 0.9:
                            if self.S19 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅗ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅗ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S19 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [19] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][19] > 0.9:
                            if self.S20 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅛ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅛ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S20 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [20] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][20] > 0.9:
                            if self.S21 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅜ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅜ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S21 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [21] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][21] > 0.9:
                            if self.S22 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅠ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅠ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S22 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [22] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][22] > 0.9:
                            if self.S23 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅡ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅡ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S23 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [23] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][23] > 0.9:
                            if self.S24 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅣ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅣ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S24 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [24] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][24] > 0.9:
                            if self.S25 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅐ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅐ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S25 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [25] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][25] > 0.9:
                            if self.S26 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅒ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅒ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S26 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [26] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][26] > 0.9:
                            if self.S27 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅔ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅔ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S27 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [27] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][27] > 0.9:
                            if self.S28 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅖ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅖ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S28 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [28] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][28] > 0.9:
                            if self.S29 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅚ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅚ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S29 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [29] and \
                                        MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][29] > 0.9:
                            if self.S30 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅟ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅟ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S30 += 1
                            print self.ten
                        if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [30] and \
                                        MAIN_GUI.MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][30] > 0.9:
                            if self.S31 == Sensitivity.TouchPointListener.sensitive:
                                print MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                                print "ㅢ 저장완료"
                                MAIN_GUI.static_value.append(u"ㅢ")
                                self.paintCanvas.configure(background=recog_color)
                                pygame.mixer.music.play()
                                time.sleep(1)

                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.Label_UPDATE()
                            self.S31 += 1
                            print self.ten

                        if MAIN_GUI.static_value[-1] == MAIN_GUI.static_value[-2]:
                            if eq(MAIN_GUI.static_value[-1], u"ㄱ"):
                                MAIN_GUI.static_value.pop()
                                MAIN_GUI.static_value.pop()
                                MAIN_GUI.static_value.append(u"ㄲ")
                                self.Label_UPDATE()
                            if eq(MAIN_GUI.static_value[-1], u"ㄷ"):
                                MAIN_GUI.static_value.pop()
                                MAIN_GUI.static_value.pop()
                                MAIN_GUI.static_value.append(u"ㄸ")
                                self.Label_UPDATE()
                            if eq(MAIN_GUI.static_value[-1], u"ㅂ"):
                                MAIN_GUI.static_value.pop()
                                MAIN_GUI.static_value.pop()
                                MAIN_GUI.static_value.append(u"ㅃ")
                                self.Label_UPDATE()
                            if eq(MAIN_GUI.static_value[-1], u"ㅅ"):
                                MAIN_GUI.static_value.pop()
                                MAIN_GUI.static_value.pop()
                                MAIN_GUI.static_value.append(u"ㅆ")
                                self.Label_UPDATE()
                            if eq(MAIN_GUI.static_value[-1], u"ㅈ"):
                                MAIN_GUI.static_value.pop()
                                MAIN_GUI.static_value.pop()
                                MAIN_GUI.static_value.append(u"ㅉ")
                                self.Label_UPDATE()

                        if eq(MAIN_GUI.static_value[-2], u"ㅜ") == 1 and eq(MAIN_GUI.static_value[-1], u"ㅓ") == 1:
                            MAIN_GUI.static_value.pop()
                            MAIN_GUI.static_value.pop()
                            MAIN_GUI.static_value.append(u"ㅝ")
                            self.Label_UPDATE()
                        if eq(MAIN_GUI.static_value[-2], u"ㅗ") == 1 and eq(MAIN_GUI.static_value[-1], u"ㅏ") == 1:
                            MAIN_GUI.static_value.pop()
                            MAIN_GUI.static_value.pop()
                            MAIN_GUI.static_value.append(u"ㅘ")
                            self.Label_UPDATE()
                        if eq(MAIN_GUI.static_value[-2], u"ㅗ") == 1 and eq(MAIN_GUI.static_value[-1], u"ㅐ") == 1:
                            MAIN_GUI.static_value.pop()
                            MAIN_GUI.static_value.pop()
                            MAIN_GUI.static_value.append(u"ㅙ")
                            self.Label_UPDATE()
                        if eq(MAIN_GUI.static_value[-2], u"ㅜ") == 1 and eq(MAIN_GUI.static_value[-1], u"ㅔ") == 1:
                            MAIN_GUI.static_value.pop()
                            MAIN_GUI.static_value.pop()
                            MAIN_GUI.static_value.append(u"ㅞ")
                            self.Label_UPDATE()
                except:
                    pass
            elif handType == "Right hand" and len(frame.hands) == 1 and self.Dynamic_Flag == 1:
                print "수화 한손 모드"
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [0] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][0] > 0.9:
                    if self.like == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "좋아해요."
                        MAIN_GUI.static_value.append(u"좋아해요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.like += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [1] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][1] > 0.9:
                    if self.love == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "사랑해요."
                        MAIN_GUI.static_value.append(u"사랑해요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.love += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [2] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][2] > 0.9:
                    if self.very == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "매우"
                        MAIN_GUI.static_value.append(u"매우 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.very += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [3] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][3] > 0.9:
                    if self.fact == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "사실"
                        MAIN_GUI.static_value.append(u"사실 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.fact += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [4] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][4] > 0.9:
                    if self.what == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "예뻐요."
                        MAIN_GUI.static_value.append(u"예뻐요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.what += 1

                # if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [6] and \
                #                 MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][6] > 0.9:
                #     if self.fine == Sensitivity.TouchPointListener.sensitive:
                #         print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                #         print "괜찮아요"
                #         MAIN_GUI.static_value.append(u"괜찮아요 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.fine += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [7] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][7] > 0.9:
                    if self.sleep == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "졸려요."
                        MAIN_GUI.static_value.append(u"졸려요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.sleep += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [8] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][8] > 0.9:
                    if self.tomorrow == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "내일"
                        MAIN_GUI.static_value.append(u"내일 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.tomorrow += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [9] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][9] > 0.9:
                    if self.forward == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "앞으로"
                        MAIN_GUI.static_value.append(u"앞으로 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.forward += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [10] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][10] > 0.9:
                    if self.delicious == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "맛있어요"
                        MAIN_GUI.static_value.append(u"맛있어요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.delicious += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [11] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][11] > 0.9:
                    if self.food == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "음식"
                        MAIN_GUI.static_value.append(u"음식 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.food += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [12] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][12] > 0.9:
                    if self.name == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "이름"
                        MAIN_GUI.static_value.append(u"이름 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.name += 1
                # if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [13] and \
                #                 MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][13] > 0.9:
                #     if self.yes == Sensitivity.TouchPointListener.sensitive:
                #         print "네"
                #         MAIN_GUI.static_value.append(u"네 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.yes += 1

                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [5] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][5] > 0.9 and self.me == 0:
                    self.initializeVal()
                    self.me += 1
                    self.WORD.config(text="예상단어: 우리", bg=mycolor)
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [14] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][14] > 0.9 and self.me == 1:
                    if self.we == Sensitivity.TouchPointListener.sensitive:
                        print "우리"
                        MAIN_GUI.static_value.append(u"우리 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.we += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [15] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][15] > 0.9:
                    if self.rank == Sensitivity.TouchPointListener.sensitive:
                        print "싶다"
                        MAIN_GUI.static_value.append(u"싶다. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.rank += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [26] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][
                                    26] > 0.9 and self.question == 0:
                    self.initializeVal()
                    self.question += 1
                    self.WORD.config(text="예상단어: 질문", bg=mycolor)
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [16] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][
                                    16] > 0.9 and self.question == 1 and not self.but == 1:
                    if self.question2 == Sensitivity.TouchPointListener.sensitive:
                        print "질문"
                        MAIN_GUI.static_value.append(u"질문 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.question2 += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [17] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][17] > 0.9:
                    if self.be == Sensitivity.TouchPointListener.sensitive:
                        print "있다"
                        MAIN_GUI.static_value.append(u"있다. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.be += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [18] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][18] > 0.9:
                    if self.hate == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "싫어요"
                        MAIN_GUI.static_value.append(u"싫어요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.hate += 1

                # if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [22] and \
                #                 MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][22] > 0.9:
                #     if self.noon == Sensitivity.TouchPointListener.sensitive:
                #         print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                #         print "정오"
                #         MAIN_GUI.static_value.append(u"정오 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.noon += 1

                # if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [23] and \
                #                 MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][23] > 0.9:
                #     if self.night == Sensitivity.TouchPointListener.sensitive:
                #         print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                #         print "저녁"
                #         MAIN_GUI.static_value.append(u"저녁 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.night += 1

                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [16] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][
                                    16] > 0.9 and self.but == 0 and not self.question == 1:
                    self.initializeVal()
                    self.but += 1
                    self.WORD.config(text="예상단어: 하지만", bg=mycolor)

                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [14] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][
                                    14] > 0.9 and self.but == 1:
                    if self.but2 == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "하지만"
                        MAIN_GUI.static_value.append(u"하지만 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.but2 += 1

                # if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [24] and \
                #                 MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][24] > 0.9:
                #     if self.meat == Sensitivity.TouchPointListener.sensitive:
                #         print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                #         print "고기"
                #         MAIN_GUI.static_value.append(u"고기 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.meat += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [25] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][25] > 0.9:
                    if self.this1 == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "이것"
                        MAIN_GUI.static_value.append(u"이것 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.this1 += 1

                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [27] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][27] > 0.9:
                    if self.money == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "금"
                        MAIN_GUI.static_value.append(u"금 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.money += 1

                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [28] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][28] > 0.9:
                    if self.everyone == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "여러분"
                        MAIN_GUI.static_value.append(u"여러분 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.everyone += 1

                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [29] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][29] > 0.9:
                    if self.learn == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "배우다"
                        MAIN_GUI.static_value.append(u"배우다. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.learn += 1

                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [30] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][30] > 0.9:
                    if self.give == Sensitivity.TouchPointListener.sensitive:
                        print MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data, verbose=0)
                        print "드릴게요."
                        MAIN_GUI.static_value.append(u"드릴게요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.give += 1


            elif len(frame.hands) == 2 and self.Dynamic_Flag == 1:
                print "수화 두손 모드"
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [0] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][0] > 0.9:
                    if self.meet == Sensitivity.TouchPointListener.sensitive:
                        print "만나다"
                        MAIN_GUI.static_value.append(u"만나다. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.meet += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [1] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][1] > 0.9:
                    if self.funny == Sensitivity.TouchPointListener.sensitive:

                        print "즐거워요"
                        MAIN_GUI.static_value.append(u"즐거워요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.funny += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [2] and \
                #                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][2] > 0.9:
                #    if self.sorry == Sensitivity.TouchPointListener.sensitive:
                #        print model.predict_classes(predict_data, verbose=0)
                #        print "죄송해요"
                #        MAIN_GUI.static_value.append(u"죄송해요 ")
                #        self.paintCanvas.configure(background=recog_color)
                #        pygame.mixer.music.play() time.sleep(1)
                #
                #        self.paintCanvas.configure(background='white')
                #        self.initializeVal()
                #        self.Label_UPDATE()
                #    self.sorry += 1
                #
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [3] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][3] > 0.9:
                    if self.hungry == Sensitivity.TouchPointListener.sensitive:

                        print "배고파요"
                        MAIN_GUI.static_value.append(u"배고파요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.hungry += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [28] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][
                                    28] > 0.9 and self.thank2 == 0:
                    self.initializeVal()
                    self.thank2 += 1
                    self.WORD.config(text="예상단어: 감사합니다.", bg=mycolor)

                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [4] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][
                                    4] > 0.9 and self.thank2 == 1:
                    if self.thank == Sensitivity.TouchPointListener.sensitive:
                        print "감사합니다."
                        MAIN_GUI.static_value.append(u"감사합니다. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.thank += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [5] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][5] > 0.9:
                    if self.hello == Sensitivity.TouchPointListener.sensitive:

                        print "안녕하세요."
                        MAIN_GUI.static_value.append(u"안녕하세요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.hello += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [6] and \
                #                 MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][6] > 0.9:
                #     if self.regretful == Sensitivity.TouchPointListener.sensitive:
                #
                #         print "안타까워요"
                #         MAIN_GUI.static_value.append(u"안타까워요 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.regretful += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [7] and \
                #                 MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][7] > 0.9:
                #     if self.do == Sensitivity.TouchPointListener.sensitive:
                #         print "해"
                #         MAIN_GUI.static_value.append(u"해 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.do += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [8] and \
                #                 MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][8] > 0.9:
                #     if self.donot == Sensitivity.TouchPointListener.sensitive:
                #
                #         print "하지마"
                #         MAIN_GUI.static_value.append(u"하지마 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.donot += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [9] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][9] > 0.9:
                    if self.connect == Sensitivity.TouchPointListener.sensitive:
                        print "연락주세요."
                        MAIN_GUI.static_value.append(u"연락주세요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.connect += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [10] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][10] > 0.9:
                    if self.nicetomeet == Sensitivity.TouchPointListener.sensitive:
                        print "반갑다"
                        MAIN_GUI.static_value.append(u"반갑다. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.nicetomeet += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [11] and \
                #                 MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][11] > 0.9:
                #     if self.no == Sensitivity.TouchPointListener.sensitive:
                #         print "아니요"
                #         MAIN_GUI.static_value.append(u"아니요 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.no += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [12] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][12] > 0.9:
                    if self.now == Sensitivity.TouchPointListener.sensitive:
                        print "이제"
                        MAIN_GUI.static_value.append(u"이제 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.now += 1
                #헤어져요
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [13] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][13] > 0.9:
                    if self.byebye == Sensitivity.TouchPointListener.sensitive:
                        print "헤어져요"
                        MAIN_GUI.static_value.append(u"헤어져요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.byebye += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [14] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][14] > 0.9:
                    if self.time == Sensitivity.TouchPointListener.sensitive:

                        print "시간"
                        MAIN_GUI.static_value.append(u"시간 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.time += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [15] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][15] > 0.9:
                    if self.is_16 == Sensitivity.TouchPointListener.sensitive:
                        print "이다"
                        MAIN_GUI.static_value.append(u"이다. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.is_16 += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [16] and \
                                    MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][16] > 0.9 and self.eat==0:
                    self.initializeVal()
                    self.eat+=1
                    self.WORD.config(text="예상단어: 먹다.", bg=mycolor)
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [48] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][48] > 0.9 and self.eat==1:
                    if self.eat2 == Sensitivity.TouchPointListener.sensitive:

                        print "먹다"
                        MAIN_GUI.static_value.append(u"먹다. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.eat2 += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [17] and \
                #                 MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][17] > 0.9:
                #     if self.rank == Sensitivity.TouchPointListener.sensitive:
                #         print "등"
                #         MAIN_GUI.static_value.append(u"등 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.rank += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [18] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][18] > 0.9:
                    if self.team == Sensitivity.TouchPointListener.sensitive:
                        print "팀"
                        MAIN_GUI.static_value.append(u"팀 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.team += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [19] and \
                #                 MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][19] > 0.9:
                #     if self.senior == Sensitivity.TouchPointListener.sensitive:
                #         print "선배"
                #         MAIN_GUI.static_value.append(u"선배 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.senior += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [20] and \
                #                 MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][20] > 0.9:
                #     if self.junior == Sensitivity.TouchPointListener.sensitive:
                #
                #         print "후배"
                #         MAIN_GUI.static_value.append(u"후배 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.junior += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [21] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][
                                    21] > 0.9 and self.well == 0:
                    self.initializeVal()
                    self.well += 1
                    self.WORD.config(text="예상단어: 잘해요.", bg=mycolor)
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [37] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][
                                    37] > 0.9 and self.well == 1:
                    if self.well2 == Sensitivity.TouchPointListener.sensitive:
                        print "잘해요"
                        MAIN_GUI.static_value.append(u"잘해요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.well2 += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [22] and \
                #                 MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][22] > 0.9:
                #     if self.dokdo == Sensitivity.TouchPointListener.sensitive:
                #
                #         print "독도"
                #         MAIN_GUI.static_value.append(u"독도 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.dokdoe += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [23] and \
                #                 MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][23] > 0.9:
                #     if self.grand == Sensitivity.TouchPointListener.sensitive:
                #
                #         print "땅"
                #         MAIN_GUI.static_value.append(u"땅 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.grand += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [24] and \
                #                 MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][24] > 0.9:
                #     if self.evaluate == Sensitivity.TouchPointListener.sensitive:
                #
                #         print "평가"
                #         MAIN_GUI.static_value.append(u"평가 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.evaluate += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [25] and \
                #                 MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][25] > 0.9:
                #     if self.coach == Sensitivity.TouchPointListener.sensitive:
                #
                #         print "멘토"
                #         MAIN_GUI.static_value.append(u"멘토 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.coach += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [26] and \
                #                 MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][26] > 0.9:
                #     if self.sir == Sensitivity.TouchPointListener.sensitive:
                #
                #         print "님"
                #         MAIN_GUI.static_value.append(u"님 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.sir += 1

                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [29] and \
                                    MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][29] > 0.9 and self.buy==0:
                    self.initializeVal()
                    self.buy+=1
                    self.WORD.config(text="예상단어: 사다.", bg=mycolor)

                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [30] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][30] > 0.9 and self.buy==1:
                    if self.buy2 == Sensitivity.TouchPointListener.sensitive:
                        print "사다."
                        MAIN_GUI.static_value.append(u"사다. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.buy2 += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [31] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][
                                    31] > 0.9 and self.weather == 0:
                    self.weather += 1
                    self.WORD.config(text="예상단어: 날씨", bg=mycolor)

                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [32] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][
                                    32] > 0.9 and self.weather == 1:
                    if self.weather2 == Sensitivity.TouchPointListener.sensitive:
                        print "날씨"
                        MAIN_GUI.static_value.append(u"날씨 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.weather2 += 1

                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [33] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][33] > 0.9:
                    if self.today == Sensitivity.TouchPointListener.sensitive:
                        print "오늘"
                        MAIN_GUI.static_value.append(u"오늘 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()

                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.today += 1

                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [34] and \
                #                     MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][34] > 0.9:
                #         if self.different == Sensitivity.TouchPointListener.sensitive:
                #             print "다른"
                #             MAIN_GUI.static_value.append(u"다른 ")
                #             self.paintCanvas.configure(background=recog_color)
                #             pygame.mixer.music.play()
                #             time.sleep(1)
                #
                #             self.paintCanvas.configure(background='white')
                #             self.initializeVal()
                #             self.Label_UPDATE()
                #         self.different += 1

                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [35] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][35] > 0.9:
                    if self.please == Sensitivity.TouchPointListener.sensitive:
                        print "부탁해요"
                        MAIN_GUI.static_value.append(u"부탁해요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.please += 1

                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [36] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][36] > 0.9:
                    if self.because == Sensitivity.TouchPointListener.sensitive:
                        print "때문"
                        MAIN_GUI.static_value.append(u"때문 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.because += 1

                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [38] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][38] > 0.9:
                    if self.support == Sensitivity.TouchPointListener.sensitive:
                        print "지원"
                        MAIN_GUI.static_value.append(u"지원")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.support += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [39] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][39] > 0.9:
                    if self.receive == Sensitivity.TouchPointListener.sensitive:
                        print "받아서"
                        MAIN_GUI.static_value.append(u"받아서 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.receive += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [40] and \
                #                     MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][40] > 0.9:
                #         if self.cellphone == Sensitivity.TouchPointListener.sensitive:
                #             print "통신사"
                #             MAIN_GUI.static_value.append(u"통신사 ")
                #             self.paintCanvas.configure(background=recog_color)
                #             pygame.mixer.music.play()
                #             time.sleep(1)
                #
                #             self.paintCanvas.configure(background='white')
                #             self.initializeVal()
                #             self.Label_UPDATE()
                #         self.cellphone += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [41] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][41] > 0.9:
                    if self.clap == Sensitivity.TouchPointListener.sensitive:
                        print "박수"
                        MAIN_GUI.static_value.append(u"박수 ")
                        self.paintCanvas.configure(background=recog_color)
                        #a.play()
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.clap += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [42] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][42] > 0.9:
                    if self.signlang == Sensitivity.TouchPointListener.sensitive:
                        print "수어"
                        MAIN_GUI.static_value.append(u"수어 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.signlang += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [43] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][43] > 0.9:
                    if self.teach == Sensitivity.TouchPointListener.sensitive:
                        print "가르쳐"
                        MAIN_GUI.static_value.append(u"가르쳐 ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.teach += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [44] and \
                #                     MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][44] > 0.9:
                #         if self.hard == Sensitivity.TouchPointListener.sensitive:
                #             print "열심히"
                #             MAIN_GUI.static_value.append(u"열심히 ")
                #             self.paintCanvas.configure(background=recog_color)
                #             pygame.mixer.music.play()
                #             time.sleep(1)
                #
                #             self.paintCanvas.configure(background='white')
                #             self.initializeVal()
                #             self.Label_UPDATE()
                #         self.hard += 1
                if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [45] and \
                                MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][45] > 0.9:
                    if self.happy == Sensitivity.TouchPointListener.sensitive:
                        print "행복해요."
                        MAIN_GUI.static_value.append(u"행복해요. ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.happy += 1

                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [46] and \
                #                     MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][46] > 0.9:
                #         if self.baseball == Sensitivity.TouchPointListener.sensitive:
                #             print "야구"
                #             MAIN_GUI.static_value.append(u"야구 ")
                #             self.paintCanvas.configure(background=recog_color)
                #             pygame.mixer.music.play()
                #             time.sleep(1)
                #
                #             self.paintCanvas.configure(background='white')
                #             self.initializeVal()
                #             self.Label_UPDATE()
                #         self.baseball += 1
                # if MAIN_GUI.Dynamic_model.predict_classes(MAIN_GUI.Dynamic_predict_data) == [47] and \
                #                 MAIN_GUI.Dynamic_model.predict(MAIN_GUI.Dynamic_predict_data)[0][47] > 0.9:
                #     if self.eman == Sensitivity.TouchPointListener.sensitive:
                #         print "끝내다"
                #         MAIN_GUI.static_value.append(u"끝내다 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.eman += 1

                print "hands two!!!!!!!!!"
            elif handType == "Right hand" and len(frame.hands) == 1 and self.Number_Flag == 1:
                if MAIN_GUI.Number_model.predict_classes(MAIN_GUI.predict_data) == [0] and \
                                MAIN_GUI.Number_model.predict(MAIN_GUI.predict_data)[0][0] > 0.9:
                    if self.one == Sensitivity.TouchPointListener.sensitive:
                        print "1 저장완료"
                        MAIN_GUI.static_value.append(u"1")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.one += 1
                    print self.one
                if MAIN_GUI.Number_model.predict_classes(MAIN_GUI.predict_data) == [1] and \
                                MAIN_GUI.Number_model.predict(MAIN_GUI.predict_data)[0][1] > 0.9:

                    if self.two == Sensitivity.TouchPointListener.sensitive:
                        print "2 저장완료"
                        MAIN_GUI.static_value.append(u"2")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.two += 1
                    print self.two
                    print "!!!!!!!!!!!!!!!!!!!!!!!"
                if MAIN_GUI.Number_model.predict_classes(MAIN_GUI.predict_data) == [2] and \
                                MAIN_GUI.Number_model.predict(MAIN_GUI.predict_data)[0][2] > 0.9:
                    if self.three == Sensitivity.TouchPointListener.sensitive:
                        print "3 저장완료"
                        MAIN_GUI.static_value.append(u"3")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.Label_UPDATE()
                        self.initializeVal()
                    self.three += 1
                    print self.three
                if MAIN_GUI.Number_model.predict_classes(MAIN_GUI.predict_data) == [3] and \
                                MAIN_GUI.Number_model.predict(MAIN_GUI.predict_data)[0][3] > 0.9:
                    if self.four == Sensitivity.TouchPointListener.sensitive:
                        print "4 저장완료"
                        MAIN_GUI.static_value.append(u"4")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.four += 1
                    print self.four
                if MAIN_GUI.Number_model.predict_classes(MAIN_GUI.predict_data) == [4] and \
                                MAIN_GUI.Number_model.predict(MAIN_GUI.predict_data)[0][4] > 0.9:
                    if self.five == Sensitivity.TouchPointListener.sensitive:
                        print "5 저장완료"
                        MAIN_GUI.static_value.append(u"5")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.five += 1
                    print self.four
                if MAIN_GUI.Number_model.predict_classes(MAIN_GUI.predict_data) == [5] and \
                                MAIN_GUI.Number_model.predict(MAIN_GUI.predict_data)[0][5] > 0.9:
                    if self.six == Sensitivity.TouchPointListener.sensitive:
                        print "6 저장완료"
                        MAIN_GUI.static_value.append(u"6")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.six += 1
                    print self.six
                if MAIN_GUI.Number_model.predict_classes(MAIN_GUI.predict_data) == [6] and \
                                MAIN_GUI.Number_model.predict(MAIN_GUI.predict_data)[0][6] > 0.9:
                    if self.seven == Sensitivity.TouchPointListener.sensitive:
                        print "7 저장완료"
                        MAIN_GUI.static_value.append(u"7")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.seven += 1
                    print self.seven
                if MAIN_GUI.Number_model.predict_classes(MAIN_GUI.predict_data) == [7] and \
                                MAIN_GUI.Number_model.predict(MAIN_GUI.predict_data)[0][7] > 0.9:
                    if self.eight == Sensitivity.TouchPointListener.sensitive:
                        print "8 저장완료"
                        MAIN_GUI.static_value.append(u"8")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.eight += 1
                    print self.eight
                if MAIN_GUI.Number_model.predict_classes(MAIN_GUI.predict_data) == [8] and \
                                MAIN_GUI.Number_model.predict(MAIN_GUI.predict_data)[0][8] > 0.9:
                    if self.nine == Sensitivity.TouchPointListener.sensitive:
                        print "9 저장완료"
                        MAIN_GUI.static_value.append(u"9")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.nine += 1
                    print self.nine
                if MAIN_GUI.Number_model.predict_classes(MAIN_GUI.predict_data) == [9] and \
                                MAIN_GUI.Number_model.predict(MAIN_GUI.predict_data)[0][9] > 0.9:
                    if self.ten == Sensitivity.TouchPointListener.sensitive:
                        print "0 저장완료"
                        MAIN_GUI.static_value.append(u"0")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.ten += 1
                    print self.nine
            elif handType == "Left hand" and len(frame.hands) == 1:
                if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [31]:
                    if self.S32 == 30:
                        print "삭제"
                        MAIN_GUI.static_value.pop()
                        self.paintCanvas.configure(background=recog_color)
                        time.sleep(0.5)
                        self.paintCanvas.configure(background='white')
                        restored_text = join_jamos(MAIN_GUI.static_value)
                        self.Label_UPDATE()
                        self.initializeVal()
                    self.S32 += 1

                if MAIN_GUI.model.predict_classes(MAIN_GUI.predict_data) == [32] and \
                                MAIN_GUI.model.predict(MAIN_GUI.predict_data)[0][32] > 0.9:
                    if self.S33 == 50:
                        restored_text = join_jamos(MAIN_GUI.static_value)
                        print "보내기"

                        a2.play()


                        restored_text = join_jamos(MAIN_GUI.static_value)
                        asciidata = restored_text.encode("utf-8", "ignore")
                        tts = gTTS(text=asciidata, lang='ko')
                            # from tempfile import TemporaryFile
                            # f = TemporaryFile()
                            # tts.write_to_fp(f)
                            # f.close()
                        Go_str = str(frame.id)
                        tts.save("speak"+Go_str+".mp3")


                        playsound.playsound("speak"+Go_str+".mp3")
                       # winsound.PlaySound('tts.mp3', winsound.SND_PURGE)
                        self.Send_Message()
                        self.initializeVal()
                        try:
                            os.remove("speak"+Go_str+".mp3")
                        except OSError:
                            pass

                    self.S33 += 1
                    print self.ten
                print MAIN_GUI.static_value

                # if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [19] and \
                #             MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][19] > 0.9:
                #     if self.lee == Sensitivity.TouchPointListener.sensitive:
                #
                #         print "이건녕"
                #         MAIN_GUI.static_value.append(u"이건녕 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.lee += 1


                # if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [20] and \
                #                 MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][20] > 0.9:
                #     if self.shin == Sensitivity.TouchPointListener.sensitive:
                #
                #         print "신명국"
                #         MAIN_GUI.static_value.append(u"신명국 ")
                #         self.paintCanvas.configure(background=recog_color)
                #         pygame.mixer.music.play()
                #         time.sleep(1)
                #
                #         self.paintCanvas.configure(background='white')
                #         self.initializeVal()
                #         self.Label_UPDATE()
                #     self.shin += 1


                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [21] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][21] > 0.9:
                    if self.seo == Sensitivity.TouchPointListener.sensitive:
                        #print "ITsHansung"
                        #MAIN_GUI.static_value.append(u"ITsHansung ")
                        print "HandsTalk"
                        MAIN_GUI.static_value.append(u"HandsTalk ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.seo += 1
                if MAIN_GUI.One_Dynamic_model.predict_classes(MAIN_GUI.predict_data) == [31] and \
                                MAIN_GUI.One_Dynamic_model.predict(MAIN_GUI.predict_data)[0][31] > 0.9:
                    if self.sk == Sensitivity.TouchPointListener.sensitive:
                        print "SKT"
                        MAIN_GUI.static_value.append(u"SKT ")
                        self.paintCanvas.configure(background=recog_color)
                        pygame.mixer.music.play()
                        time.sleep(1)

                        self.paintCanvas.configure(background='white')
                        self.initializeVal()
                        self.Label_UPDATE()
                    self.sk += 1

            try:
                if eq(MAIN_GUI.static_value[-2], u"정오 ") == 1 and eq(MAIN_GUI.static_value[-1], u"먹다. ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"점심 ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"좋아해요. ") == 1 and eq(MAIN_GUI.static_value[-1], u"질문 ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"좋죠? ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"HandsTalk ") == 1 and eq(MAIN_GUI.static_value[-1], u"이다. ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"HandsTalk입니다. ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"ITsHansung ") == 1 and eq(MAIN_GUI.static_value[-1], u"이다. ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"ITsHansung입니다. ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"SKT ") == 1 and eq(MAIN_GUI.static_value[-1], u"이다. ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"SKT에요. ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"박수 ") == 1 and eq(MAIN_GUI.static_value[-1], u"지원") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"응원 ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"이것 ") == 1 and eq(MAIN_GUI.static_value[-1], u"때문 ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"그래서 ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"매우 ") == 1 and eq(MAIN_GUI.static_value[-1], u"열심히 ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"더 열심히 ")
                    self.Label_UPDATE()

                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"배우다. ") == 1 and eq(MAIN_GUI.static_value[-1], u"질문 ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"배워 보실래요? ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"이제 ") == 1 and eq(MAIN_GUI.static_value[-1], u"끝내다. ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"이제 끝낼게요. ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"해 ") == 1 and eq(MAIN_GUI.static_value[-1], u"이다. ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"하겠습니다. ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"먹다. ") == 1 and eq(MAIN_GUI.static_value[-1], u"질문 ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"먹었어요? ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-3], u"등 ") == 1 and eq(MAIN_GUI.static_value[-2], u"해 ") == 1 and eq(MAIN_GUI.static_value[-1], u"싶다. ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"등 하고 싶어요. ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"해 ") == 1 and eq(MAIN_GUI.static_value[-1], u"싶다. ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"해보고 싶은 ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"잘해요. ") == 1 and eq(MAIN_GUI.static_value[-1], u"부탁해요. ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"잘 부탁해요. ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"응원 ") == 1 and eq(MAIN_GUI.static_value[-1], u"해 ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"응원해요. ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"있다. ") == 1 and eq(MAIN_GUI.static_value[-1], u"질문 ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"있나요? ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"만나다. ") == 1 and eq(MAIN_GUI.static_value[-1], u"반갑다. ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"만나서 반갑습니다. ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"매우 ") == 1 and eq(MAIN_GUI.static_value[-1], u"예뻐요. ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"정말 예뻐요. ")
                    self.Label_UPDATE()
                if eq(MAIN_GUI.static_value[-2], u"팀 ") == 1 and eq(MAIN_GUI.static_value[-1], u"수어 ") == 1:
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.pop()
                    MAIN_GUI.static_value.append(u"팀이 수어 ")
                    self.Label_UPDATE()


            except:
                pass

    def Send_Message(self):
        if not MAIN_GUI.static_value == [""]:
            restored_text = join_jamos(MAIN_GUI.static_value)


            self.LB.insert(END, restored_text)
            self.LB.see("end")
            MAIN_GUI.static_value = [""]
            self.txt.delete(0, 'end')
        else:
            print ("MAIN_GUI.static_value no value")

    def set_canvas(self, canvas):
        self.paintCanvas = canvas

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % rgb


