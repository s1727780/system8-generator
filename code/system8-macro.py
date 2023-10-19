import pyautogui
import time
import os
import csv
import math
from enum import Enum
import sys

class Test(Enum):
    AMS_VI = 1
    AMS_Matrix = 2


class Step:
    addStep     = (105, 1020)
    copyStep    = (185, 1020)
    delStep     = (267, 1020)
    firstStep   = ( 95, 202)
    lastStep    = ( 95, 652)

    incrStep    =   18
    maxStep     =   26

class Instrument:
    End         = (387, 62)

class TF:
    new         = ( 14,  77)
    editMode    = ( 80, 115)
    setup_open  = (187, 1107)
    setup_close = (394,  92)


class ReportManager:
    AMS_VI      = ( 96, 232)
    AMS_Matrix  = ( 96, 248)

class AMS_VI:
    AMS_VI      = ( 12, 365)
    probeSelect = (400, 110)
    pinSelect   = (400,135)

class AMS_Matrix:
    AMS_Matrix  = (12,390)
    pinSelect   = (360, 112)


class Preset_steps:
    def __init__(self):
        clickAt(TF.editMode)

    cur_step = 0
    
    def AMS_VI(self, text = "AMS VI", pins = 0):
        self.cur_step += 1
        createX(Test.AMS_VI)

        # Change probe / pins
        moveTo(AMS_VI.probeSelect)        
        if pins != 0:
            if "Probe" in pins:
                scroll(300)
                time.sleep(0.1)
                moveTo(AMS_VI.pinSelect)
                time.sleep(0.1)
                scroll(1000)
                time.sleep(0.1)
                if "Probes" in pins:
                    pins = pins.removesuffix(" Probes")
                    multi = math.floor(float(pins)) -1

                    scroll(-120*multi)
                    time.sleep(0.1)

                print("PROBES")
            elif "Clip" in pins:
                pins = pins.removesuffix(" Clip")
                time.sleep(0.1)
                scroll(-300)
                time.sleep(0.1)
                print("CLIP")
                moveTo(AMS_VI.pinSelect)
                time.sleep(0.1)
                scroll(5000)
            
                multi = math.floor(float(pins) / 2) -1

                scroll(-120*multi)
                time.sleep(0.1)

            else:
                print("Pins input not correct and has not changed")

        rename(text, self.cur_step)



    def AMS_Matrix(self, text = "AMS Matrix", pins = 0):
        self.cur_step += 1
        createX(Test.AMS_Matrix)
        
        #change pin number
        if pins != 0:
            if "Clip" in pins:
                pins = pins.removesuffix(" Clip")
            moveTo(AMS_Matrix.pinSelect)
            time.sleep(0.1)
            scroll(5000)
            
            multi = math.floor(float(pins) / 2) -1

            scroll(-120*multi)
            time.sleep(0.1)
            
        rename(text, self.cur_step)
    
    def IGNORE_STEP(self):
        self.cur_step += 1

def moveTo(position):
    pyautogui.moveTo(position)

def clickAt(position):
    pyautogui.click(position)

def press(key):
    pyautogui.press(key)

def write(text):
    pyautogui.write(text)

def scroll(num):
    pyautogui.scroll(num)


probes = ["1 Probe", "2 Probes", "3 Probes", "4 Probes"]


def createX(test):

    match test:
        case Test.AMS_VI:
            target = AMS_VI.AMS_VI
        case Test.AMS_Matrix:
            target = AMS_Matrix.AMS_Matrix
        case _:
            print("createX(" + str(test) + ") is not supported ")
            sys.exit()

    clickAt(Step.addStep)
    time.sleep(0.2)
    clickAt(target)
    time.sleep(0.5)

    moveWindow()

    time.sleep(0.1)
    reporting(test)

    time.sleep(0.1)


images = os.listdir("drag_images")

def moveWindow():

    location = None

    for image in images:
        location = pyautogui.locateOnScreen("drag_images/"+image, 0.4)
        if location != None:
            #print("found image")
            break

    if location is None:
        for image in images:
            location = pyautogui.locateOnScreen("drag_images/"+image, 1)
            if location != None:
                #print("found image")
                break

    start = (location[0] + 50, location[1] + 10)

    clickAt(start)
    time.sleep(0.5)
    pyautogui.dragTo(Instrument.End, duration=0.25)

rename_time = 0.5

def rename(text, stepNum = 1):

    if(stepNum >= Step.maxStep):
        #scroll down list
        target = Step.lastStep

    else:
        (x,y) = Step.firstStep
        y += Step.incrStep * (stepNum - 1)
        target = (x,y)
    

    clickAt(target)
    time.sleep(rename_time)
    clickAt(target)
    time.sleep(rename_time)
    clickAt(target)
    time.sleep(rename_time)
    clickAt(target)
    time.sleep(0.1)
    pyautogui.hotkey("ctrl", "a")
    write(text)
    press("enter")

def reporting(test):
    # click setup
    clickAt(TF.setup_open)


    # click appropriate test
    match test:
        case Test.AMS_VI:
            clickAt(ReportManager.AMS_VI)
        case Test.AMS_Matrix:
            clickAt(ReportManager.AMS_Matrix)
        case _:
            print("reporting(" + str(test) + ") is not supported")
            sys.exit()

    # close window
    clickAt(TF.setup_close)



# RUN

pyautogui.FAILSAFE = True

preset = Preset_steps()

with open("run.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        line_count += 1
        if len(row) == 3:
            name, step, pins = row  
        
        elif len(row) < 3:
            print("Row " + line_count + " is too short")
            sys.exit()

        elif len(row) > 3:
            print("Row " + line_count + " is too long")
            sys.exit()





        #print(count, name, step)

        if(step == "DO NOT EDIT"):
            preset.IGNORE_STEP()

        if(step == "AMS-VI"):
            preset.AMS_VI(name, pins)

        if(step == "AMS-Matrix"):
            preset.AMS_Matrix(name, pins)


"""
steps = Preset_steps()

steps.AMS_VI()
print(steps.cur_step)
steps.AMS_Matrix()
print(steps.cur_step)

# Start - move all scrollables to the top 

"""