import argparse
from pathlib import Path
import pyautogui
import time
import os
import csv
import math
from enum import Enum
import sys
import warnings
from openpyxl import load_workbook
import tkinter as tk
from tkinter import filedialog

class Test(Enum):
    AMS_VI = "AMS-VI"
    AMS_Matrix = "AMS-Matrix"
    none = "None"


class Step:
    addStep     = (105, 1020)
    copyStep    = (185, 1020)
    delStep     = (267, 1020)
    firstStep   = ( 95, 202)
    lastStep    = ( 95, 652)

    incrStep    =   18
    maxStep     =   26

class Instrument:
    End         = (387, 62) # Where test window gets dragged to

class TF:
    new         = ( 14,  77)
    editMode    = ( 80, 115)
    setup_open  = (187, 1107)
    setup_close = (394,  92)
    instructions= (175, 830)


class ReportManager:
    AMS_VI      = ( 96, 232)
    AMS_Matrix  = ( 96, 248)

class AMS_VI:
    AMS_VI      = ( 12, 360) # Bring up test window
    probeSelect = (400, 110)
    pinSelect   = (400,135)

class AMS_Matrix:
    AMS_Matrix  = (12,390)
    pinSelect   = (360, 112)


def clickAt(position):
    pyautogui.click(position)


clickAt(TF.setup_open)

# Remove ATM IC Tester
# clickAt((96,296))

# Add BLF reporting
clickAt((79,328))
clickAt((97,344))
clickAt((115,345))
clickAt((134,409))
clickAt((99,424))
clickAt((134,454))
clickAt((134,473))
clickAt((135,520))


clickAt(TF.setup_close)

