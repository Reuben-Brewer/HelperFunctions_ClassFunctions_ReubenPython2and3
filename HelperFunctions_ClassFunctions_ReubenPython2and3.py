# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision G, 09/21/2022

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

#########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
from copy import * #for deepcopy
import inspect #To enable 'TellWhichFileWereIn'
import json
import math
import traceback
import re
import socket, select, struct
import string
import subprocess #for beep command line call
import types #Required for 'ListFunctionNamesInClass'
import decimal
from scipy.spatial.transform import Rotation #For ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ScipyCalculation and ConvertRotationMatrixToEulerAngles_RollPitchYawAbtXYZ
#########################################################

#########################################################
import serial #___IMPORTANT: pip install pyserial (NOT pip install serial).
from serial.tools import list_ports

try:
    import ftd2xx #https://pypi.org/project/ftd2xx/ 'pip install ftd2xx', current version is 1.3.1 as of 05/06/22. For SetAllFTDIdevicesLatencyTimer function
except:
    exceptions = sys.exc_info()[0]
    print("HelperFunctions_ClassFunctions_ReubenPython2and3, warning: Could not import ftd2xx. Exceptions: %s" % exceptions)
#########################################################

#########################################################
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
#########################################################

#########################################################
if sys.version_info[0] < 3:
    from builtins import raw_input as input
else:
    from future.builtins import input as input #"sudo pip3 install future" (Python 3) AND "sudo pip install future" (Python 2)
#########################################################

#########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#########################################################

#class HelperFunctions_ClassFunctions_ReubenPython2and3():

    #######################################################################################################################
    #######################################################################################################################
    #def __init__(self):
    #    pass
    #######################################################################################################################
    #######################################################################################################################

#IF FUNCTIONS ARE NOT CONTAINED WITHIN A CLASS, THEN THEY MUST NOT BE INDENTED AT ALL (WOULD WORK ON WINDOWS BUT NOT RASPBERY PI).

#######################################################################################################################
#######################################################################################################################
def GetMyPlatform(self):

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname(): #os.uname() doesn't work in windows
            self.my_platform = "pi"
        else:
            self.my_platform = "linux"

    elif platform.system() == "Windows":
        self.my_platform = "windows"

    elif platform.system() == "Darwin":
        self.my_platform = "mac"

    else:
        self.my_platform = "other"

    print("The OS platform is: " + self.my_platform)
#######################################################################################################################
#######################################################################################################################

##########################################################################################################
##########################################################################################################
#https://stackoverflow.com/questions/28473415/is-it-possible-to-import-class-method-without-instantiating-class
#@staticmethod
#@classmethod
def ParseGUIparametersDict(self, setup_dict):

        ##########################################
        ##########################################
        if "GUIparametersDict" in setup_dict:
            self.GUIparametersDict = setup_dict["GUIparametersDict"]

            ##########################################
            if "USE_GUI_FLAG" in self.GUIparametersDict:
                self.USE_GUI_FLAG = PassThrough0and1values_ExitProgramOtherwise(self, "USE_GUI_FLAG", self.GUIparametersDict["USE_GUI_FLAG"])
            else:
                self.USE_GUI_FLAG = 0

            print("USE_GUI_FLAG = " + str(self.USE_GUI_FLAG))
            ##########################################

            ##########################################
            if "root" in self.GUIparametersDict:
                self.root = self.GUIparametersDict["root"]
            else:
                print("__init__: ERROR, must pass in 'root'")
                return
            ##########################################

            ##########################################
            if "EnableInternal_MyPrint_Flag" in self.GUIparametersDict:
                self.EnableInternal_MyPrint_Flag = PassThrough0and1values_ExitProgramOtherwise(self, "EnableInternal_MyPrint_Flag", self.GUIparametersDict["EnableInternal_MyPrint_Flag"])
            else:
                self.EnableInternal_MyPrint_Flag = 0

            print("EnableInternal_MyPrint_Flag: " + str(self.EnableInternal_MyPrint_Flag))
            ##########################################

            ##########################################
            if "PrintToConsoleFlag" in self.GUIparametersDict:
                self.PrintToConsoleFlag = PassThrough0and1values_ExitProgramOtherwise(self, "PrintToConsoleFlag", self.GUIparametersDict["PrintToConsoleFlag"])
            else:
                self.PrintToConsoleFlag = 1

            print("PrintToConsoleFlag: " + str(self.PrintToConsoleFlag))
            ##########################################

            ##########################################
            if "NumberOfPrintLines" in self.GUIparametersDict:
                self.NumberOfPrintLines = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "NumberOfPrintLines", self.GUIparametersDict["NumberOfPrintLines"], 0.0, 50.0))
            else:
                self.NumberOfPrintLines = 10

            print("NumberOfPrintLines = " + str(self.NumberOfPrintLines))
            ##########################################

            ##########################################
            if "UseBorderAroundThisGuiObjectFlag" in self.GUIparametersDict:
                self.UseBorderAroundThisGuiObjectFlag = PassThrough0and1values_ExitProgramOtherwise(self, "UseBorderAroundThisGuiObjectFlag", self.GUIparametersDict["UseBorderAroundThisGuiObjectFlag"])
            else:
                self.UseBorderAroundThisGuiObjectFlag = 0

            print("UseBorderAroundThisGuiObjectFlag: " + str(self.UseBorderAroundThisGuiObjectFlag))
            ##########################################

            ##########################################
            if "GUI_ROW" in self.GUIparametersDict:
                self.GUI_ROW = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "GUI_ROW", self.GUIparametersDict["GUI_ROW"], 0.0, 1000.0))
            else:
                self.GUI_ROW = 0

            print("GUI_ROW = " + str(self.GUI_ROW))
            ##########################################

            ##########################################
            if "GUI_COLUMN" in self.GUIparametersDict:
                self.GUI_COLUMN = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "GUI_COLUMN", self.GUIparametersDict["GUI_COLUMN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMN = 0

            print("GUI_COLUMN = " + str(self.GUI_COLUMN))
            ##########################################

            ##########################################
            if "GUI_PADX" in self.GUIparametersDict:
                self.GUI_PADX = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "GUI_PADX", self.GUIparametersDict["GUI_PADX"], 0.0, 1000.0))
            else:
                self.GUI_PADX = 1

            print("GUI_PADX = " + str(self.GUI_PADX))
            ##########################################

            ##########################################
            if "GUI_PADY" in self.GUIparametersDict:
                self.GUI_PADY = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "GUI_PADY", self.GUIparametersDict["GUI_PADY"], 0.0, 1000.0))
            else:
                self.GUI_PADY = 1

            print("GUI_PADY = " + str(self.GUI_PADY))
            ##########################################

            ##########################################
            if "GUI_ROWSPAN" in self.GUIparametersDict:
                self.GUI_ROWSPAN = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "GUI_ROWSPAN", self.GUIparametersDict["GUI_ROWSPAN"], 0.0, 1000.0))
            else:
                self.GUI_ROWSPAN = 1

            print("GUI_ROWSPAN = " + str(self.GUI_ROWSPAN))
            ##########################################

            ##########################################
            if "GUI_COLUMNSPAN" in self.GUIparametersDict:
                self.GUI_COLUMNSPAN = int(PassThroughFloatValuesInRange_ExitProgramOtherwise(self, "GUI_COLUMNSPAN", self.GUIparametersDict["GUI_COLUMNSPAN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMNSPAN = 1

            print("GUI_COLUMNSPAN = " + str(self.GUI_COLUMNSPAN))
            ##########################################

            ##########################################
            if "GUI_STICKY" in self.GUIparametersDict:
                self.GUI_STICKY = str(self.GUIparametersDict["GUI_STICKY"])
            else:
                self.GUI_STICKY = "w"

            print("GUI_STICKY = " + str(self.GUI_STICKY))
            ##########################################

        else:
            self.GUIparametersDict = dict()
            self.USE_GUI_FLAG = 0
            print("__init__: No GUIparametersDict present, setting USE_GUI_FLAG = " + str(self.USE_GUI_FLAG))

        print("GUIparametersDict = " + str(self.GUIparametersDict))
        ##########################################
        ##########################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ComputeListNorm(self, InputList):
    #print("ComputeListNorm: InputList = " + str(InputList))

    norm = -1

    try:
        ElementsSquaredSum = 0.0
        for InputElement in InputList:
            InputElement = float(InputElement)
            ElementsSquaredSum = ElementsSquaredSum + InputElement * InputElement

        norm = math.sqrt(ElementsSquaredSum)

    except:
        exceptions = sys.exc_info()[0]
        print("ComputeListNorm Error, Exceptions: %s" % exceptions)

    return norm
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def NormalizeListToUnitLength(self, InputList):
    OutputList = list(InputList)

    try:
        ElementsSquaredSum = 0.0
        for InputElement in InputList:
            InputElement = float(InputElement)
            ElementsSquaredSum = ElementsSquaredSum + InputElement * InputElement

        norm = math.sqrt(ElementsSquaredSum)

        for i, InputElement in enumerate(InputList):
            InputElement = float(InputElement)
            OutputList[i] = InputElement / norm

    except:
        exceptions = sys.exc_info()[0]
        print("NormalizeListToUnitLength Error, Exceptions: %s" % exceptions)

    return OutputList
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
#@staticmethod
def MultiplyListOfNumbersByScalar(InputList, ScalarToMultiplyBy):
    OutputList = list(InputList)

    try:
        for i, OutputElement in enumerate(OutputList):
            OutputElementFloat = float(OutputElement)
            OutputList[i] = ScalarToMultiplyBy*OutputElementFloat

    except:
        exceptions = sys.exc_info()[0]
        print("MultiplyListOfNumbersByScalar Error, Exceptions: %s" % exceptions)
        return list()

    return OutputList
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def IsInputList(self, InputToCheck):

    result = isinstance(InputToCheck, list)
    return result
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def IsInputListOfNumbers(self, InputToCheck):

    if isinstance(InputToCheck, list) == 1:
        for element in InputToCheck:
            if isinstance(element, int) == 0 and isinstance(element, float) == 0:
                return 0
    else:
        return 0

    return 1  # If InputToCheck was a list and no element failed to be a float or int, then return a success/1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def MyPrint_WithoutLogFile(self, input_string):

    input_string = str(input_string)

    if input_string != "":

        #input_string = input_string.replace("\n", "").replace("\r", "")

        ################################ Write to console
        # Some people said that print crashed for pyinstaller-built-applications and that sys.stdout.write fixed this.
        # http://stackoverflow.com/questions/13429924/pyinstaller-packaged-application-works-fine-in-console-mode-crashes-in-window-m
        if self.PrintToConsoleFlag == 1:
            sys.stdout.write(input_string + "\n")
        ################################

        ################################ Write to GUI
        self.PrintToGui_Label_TextInputHistory_List.append(self.PrintToGui_Label_TextInputHistory_List.pop(0)) #Shift the list
        self.PrintToGui_Label_TextInputHistory_List[-1] = str(input_string) #Add the latest value

        self.PrintToGui_Label_TextInput_Str = ""
        for Counter, Line in enumerate(self.PrintToGui_Label_TextInputHistory_List):
            self.PrintToGui_Label_TextInput_Str = self.PrintToGui_Label_TextInput_Str + Line

            if Counter < len(self.PrintToGui_Label_TextInputHistory_List) - 1:
                self.PrintToGui_Label_TextInput_Str = self.PrintToGui_Label_TextInput_Str + "\n"
        ################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ConvertListOfValuesDegToRad(self, ListOfValuesDegToRadToBeConverted):

    ListOfValuesRadToBeReturned = list()

    try:
        if isinstance(ListOfValuesDegToRadToBeConverted, list) == 0:
            ListOfValuesDegToRadToBeConverted = list([ListOfValuesDegToRadToBeConverted])

        for index, value in enumerate(ListOfValuesDegToRadToBeConverted):
            ListOfValuesRadToBeReturned.append(value*math.pi/180.0)

        return ListOfValuesRadToBeReturned

    except:
        exceptions = sys.exc_info()[0]
        print("ConvertListOfValuesDegToRad Exceptions: %s" % exceptions)
        return ListOfValuesRadToBeReturned
        #traceback.print_exc()

##########################################################################################################
##########################################################################################################

###########################################################################################################
##########################################################################################################
def ConvertListOfValuesRadToDeg(self, ListOfValuesRadToDegToBeConverted):

    ListOfValuesDegToBeReturned = list()

    try:
        if isinstance(ListOfValuesRadToDegToBeConverted, list) == 0:
            ListOfValuesDegToRadToBeConverted = list([ListOfValuesRadToDegToBeConverted])

        for index, value in enumerate(ListOfValuesRadToDegToBeConverted):
            ListOfValuesDegToBeReturned.append(value*180.0/math.pi)

        return ListOfValuesDegToBeReturned

    except:
        exceptions = sys.exc_info()[0]
        print("ConvertListOfValuesRadToDeg Exceptions: %s" % exceptions)
        traceback.print_exc()
        return ListOfValuesDegToBeReturned

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def UpdateFrequencyCalculation_MainThread(self):

    try:
        self.DataStreamingDeltaT_CalculatedFromMainThread = self.CurrentTime_CalculatedFromMainThread - self.LastTime_CalculatedFromMainThread

        if self.DataStreamingDeltaT_CalculatedFromMainThread != 0.0:
            self.DataStreamingFrequency_CalculatedFromMainThread = 1.0/self.DataStreamingDeltaT_CalculatedFromMainThread

        self.LastTime_CalculatedFromMainThread = self.CurrentTime_CalculatedFromMainThread
    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation_MainThread ERROR with Exceptions: %s" % exceptions)
        traceback.print_exc()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def UpdateFrequencyCalculation_DedicatedTxThread(self):

    try:
        self.DataStreamingDeltaT_CalculatedFromDedicatedTxThread = self.CurrentTime_CalculatedFromDedicatedTxThread - self.LastTime_CalculatedFromDedicatedTxThread

        if self.DataStreamingDeltaT_CalculatedFromDedicatedTxThread != 0.0:
            self.DataStreamingFrequency_CalculatedFromDedicatedTxThread = 1.0/self.DataStreamingDeltaT_CalculatedFromDedicatedTxThread

        self.LastTime_CalculatedFromDedicatedTxThread = self.CurrentTime_CalculatedFromDedicatedTxThread
    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation_DedicatedTxThread ERROR with Exceptions: %s" % exceptions)
        traceback.print_exc()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def UpdateFrequencyCalculation_DedicatedRxThread(self):

    try:
        self.DataStreamingDeltaT_CalculatedFromDedicatedRxThread = self.CurrentTime_CalculatedFromDedicatedRxThread - self.LastTime_CalculatedFromDedicatedRxThread

        if self.DataStreamingDeltaT_CalculatedFromDedicatedRxThread != 0.0:
            self.DataStreamingFrequency_CalculatedFromDedicatedRxThread = 1.0/self.DataStreamingDeltaT_CalculatedFromDedicatedRxThread

        self.LastTime_CalculatedFromDedicatedRxThread = self.CurrentTime_CalculatedFromDedicatedRxThread
    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation_DedicatedRxThread ERROR with Exceptions: %s" % exceptions)
        traceback.print_exc()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def UpdateFrequencyCalculation_DedicatedKeyboardListeningThread(self):

    try:
        self.DataStreamingDeltaT_CalculatedFromDedicatedKeyboardListeningThread = self.CurrentTime_CalculatedFromDedicatedKeyboardListeningThread - self.LastTime_CalculatedFromDedicatedKeyboardListeningThread

        if self.DataStreamingDeltaT_CalculatedFromDedicatedKeyboardListeningThread != 0.0:
            self.DataStreamingFrequency_CalculatedFromDedicatedKeyboardListeningThread = 1.0/self.DataStreamingDeltaT_CalculatedFromDedicatedKeyboardListeningThread

        self.LastTime_CalculatedFromDedicatedKeyboardListeningThread = self.CurrentTime_CalculatedFromDedicatedKeyboardListeningThread
    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation_DedicatedKeyboardListeningThread ERROR with Exceptions: %s" % exceptions)
        traceback.print_exc()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback(self):

    print("Exiting all threads for LineDetectionFromCameraFeedSBclass object")

    self.EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def StartGUI(self, GuiParent):

    self.GUI_Thread_ThreadingObject = threading.Thread(target=self.GUI_Thread, args=(GuiParent,))
    self.GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
    self.GUI_Thread_ThreadingObject.start()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def TellWhichFileWereIn(self):

    #We used to use this method, but it gave us the root calling file, not the class calling file
    #absolute_file_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    #filename = absolute_file_path[absolute_file_path.rfind("\\") + 1:]

    frame = inspect.stack()[1]
    filename = frame[1][frame[1].rfind("\\") + 1:]
    filename = filename.replace(".py","")

    return filename
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self, input, number_of_leading_numbers = 4, number_of_decimal_places = 3):

    number_of_decimal_places = max(1, number_of_decimal_places) #Make sure we're above 1

    ListOfStringsToJoin = []

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if isinstance(input, str) == 1:
        ListOfStringsToJoin.append(input)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, int) == 1 or isinstance(input, float) == 1:
        element = float(input)
        prefix_string = "{:." + str(number_of_decimal_places) + "f}"
        element_as_string = prefix_string.format(element)

        ##########################################################################################################
        ##########################################################################################################
        if element >= 0:
            element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1)  # +1 for sign, +1 for decimal place
            element_as_string = "+" + element_as_string  # So that our strings always have either + or - signs to maintain the same string length
        else:
            element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1 + 1)  # +1 for sign, +1 for decimal place
        ##########################################################################################################
        ##########################################################################################################

        ListOfStringsToJoin.append(element_as_string)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, list) == 1:

        if len(input) > 0:
            for element in input: #RECURSION
                ListOfStringsToJoin.append(ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self, element, number_of_leading_numbers, number_of_decimal_places))

        else: #Situation when we get a list() or []
            ListOfStringsToJoin.append(str(input))

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, tuple) == 1:

        if len(input) > 0:
            for element in input: #RECURSION
                ListOfStringsToJoin.append("TUPLE" + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self, element, number_of_leading_numbers, number_of_decimal_places))

        else: #Situation when we get a list() or []
            ListOfStringsToJoin.append(str(input))

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    elif isinstance(input, dict) == 1:

        if len(input) > 0:
            for Key in input: #RECURSION
                ListOfStringsToJoin.append(str(Key) + ": " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self, input[Key], number_of_leading_numbers, number_of_decimal_places))

        else: #Situation when we get a dict()
            ListOfStringsToJoin.append(str(input))

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    else:
        ListOfStringsToJoin.append(str(input))
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if len(ListOfStringsToJoin) > 1:

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        StringToReturn = ""
        for Index, StringToProcess in enumerate(ListOfStringsToJoin):

            ################################################
            if Index == 0: #The first element
                if StringToProcess.find(":") != -1 and StringToProcess[0] != "{": #meaning that we're processing a dict()
                    StringToReturn = "{"
                elif StringToProcess.find("TUPLE") != -1 and StringToProcess[0] != "(":  # meaning that we're processing a tuple
                    StringToReturn = "("
                else:
                    StringToReturn = "["

                StringToReturn = StringToReturn + StringToProcess.replace("TUPLE","") + ", "
            ################################################

            ################################################
            elif Index < len(ListOfStringsToJoin) - 1: #The middle elements
                StringToReturn = StringToReturn + StringToProcess + ", "
            ################################################

            ################################################
            else: #The last element
                StringToReturn = StringToReturn + StringToProcess

                if StringToProcess.find(":") != -1 and StringToProcess[-1] != "}":  # meaning that we're processing a dict()
                    StringToReturn = StringToReturn + "}"
                elif StringToProcess.find("TUPLE") != -1 and StringToProcess[-1] != ")":  # meaning that we're processing a tuple
                    StringToReturn = StringToReturn + ")"
                else:
                    StringToReturn = StringToReturn + "]"

            ################################################

        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

    elif len(ListOfStringsToJoin) == 1:
        StringToReturn = ListOfStringsToJoin[0]

    else:
        StringToReturn = ListOfStringsToJoin

    return StringToReturn
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ConvertDictToProperlyFormattedStringForPrinting(self, DictToPrint, NumberOfDecimalsPlaceToUse = 3, NumberOfEntriesPerLine = 1, NumberOfTabsBetweenItems = 3):

    ProperlyFormattedStringForPrinting = ""
    ItemsPerLineCounter = 0

    for Key in DictToPrint:

        ##########################################################################################################
        if isinstance(DictToPrint[Key], dict): #RECURSION
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 Key + ":\n" + \
                                                 ConvertDictToProperlyFormattedStringForPrinting(self, DictToPrint[Key], NumberOfDecimalsPlaceToUse, NumberOfEntriesPerLine, NumberOfTabsBetweenItems)

        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 Key + ": " + \
                                                 ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self, DictToPrint[Key], 0, NumberOfDecimalsPlaceToUse)
        ##########################################################################################################

        ##########################################################################################################
        if ItemsPerLineCounter < NumberOfEntriesPerLine - 1:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\t"*NumberOfTabsBetweenItems
            ItemsPerLineCounter = ItemsPerLineCounter + 1
        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\n"
            ItemsPerLineCounter = 0
        ##########################################################################################################

    return ProperlyFormattedStringForPrinting
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString(self):
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString_MillisecondsInteger(self):
    ts_milliseconds = int(decimal.Decimal(1000.0 * time.time()))

    return ts_milliseconds
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GetMessageQueueLength_Tx(self):

    return self.TxMessageToSend_Queue.qsize()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GetMostRecentDataDict(self):

    if self.EXIT_PROGRAM_FLAG != 1:
        return self.MostRecentDataDict
    else:
        return dict()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def SendTxMessage(self, MessageToSend, IgnoreNewDataIfQueueIsFullFlag = 1):
    if self.DedicatedTxThread_TxMessageToSend_Queue.qsize() <= self.DedicatedTxThread_TxMessageToSend_Queue_MaxSize:
        self.DedicatedTxThread_TxMessageToSend_Queue.put(MessageToSend)
    else:
        #print("SendTxMessage queue is full!")
        if IgnoreNewDataIfQueueIsFullFlag != 1:
            dummy = self.DedicatedTxThread_TxMessageToSend_Queue.get() #makes room for one more message
            self.DedicatedTxThread_TxMessageToSend_Queue.put(MessageToSend) #backfills that message with new data

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def LimitTextEntryInput_IntOutputOnly(self, min_val, max_val, test_val, TextEntryObject):

    test_val = float(test_val)  # MUST HAVE THIS LINE TO CATCH STRINGS PASSED INTO THE FUNCTION

    if test_val > max_val:
        test_val = max_val
    elif test_val < min_val:
        test_val = min_val
    else:
        test_val = test_val

    test_val = int(test_val)

    if TextEntryObject != "":
        if isinstance(TextEntryObject, list) == 1:  # Check if the input 'TextEntryObject' is a list or not
            TextEntryObject[0].set(str(test_val))  # Reset the text, overwriting the bad value that was entered.
        else:
            TextEntryObject.set(str(test_val))  # Reset the text, overwriting the bad value that was entered.

    return test_val
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def LimitNumber_IntOutputOnly(self, min_val, max_val, test_val):
    if test_val > max_val:
        test_val = max_val

    elif test_val < min_val:
        test_val = min_val

    else:
        test_val = test_val

    test_val = int(test_val)

    return test_val
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def LimitNumber_FloatOutputOnly(self, min_val, max_val, test_val):
    if test_val > max_val:
        test_val = max_val

    elif test_val < min_val:
        test_val = min_val

    else:
        test_val = test_val

    test_val = float(test_val)

    return test_val
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def LimitTextEntryInput_FloatOutputOnly(self, min_val, max_val, test_val, TextEntryObject):

    test_val = float(test_val)  # MUST HAVE THIS LINE TO CATCH STRINGS PASSED INTO THE FUNCTION

    if test_val > max_val:
        test_val = max_val
    elif test_val < min_val:
        test_val = min_val
    else:
        test_val = test_val

    test_val = float(test_val)

    if TextEntryObject != "":
        if isinstance(TextEntryObject, list) == 1:  # Check if the input 'TextEntryObject' is a list or not
            TextEntryObject[0].set(str(test_val))  # Reset the text, overwriting the bad value that was entered.
        else:
            TextEntryObject.set(str(test_val))  # Reset the text, overwriting the bad value that was entered.

    return test_val
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def PassThrough0and1values_ExitProgramOtherwise(self, InputNameString, InputNumber):

    try:
        InputNumber_ConvertedToFloat = float(InputNumber)
    except:
        exceptions = sys.exc_info()[0]
        print("PassThrough0and1values_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()

    try:
        if InputNumber_ConvertedToFloat == 0.0 or InputNumber_ConvertedToFloat == 1:
            return InputNumber_ConvertedToFloat
        else:
            input("PassThrough0and1values_ExitProgramOtherwise Error. '" +
                      InputNameString +
                      "' must be 0 or 1 (value was " +
                      str(InputNumber_ConvertedToFloat) +
                      "). Press any key (and enter) to exit.")

            sys.exit()
    except:
        exceptions = sys.exc_info()[0]
        print("PassThrough0and1values_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def PassThroughFloatValuesInRange_ExitProgramOtherwise(self, InputNameString, InputNumber, RangeMinValue, RangeMaxValue):
    try:
        InputNumber_ConvertedToFloat = float(InputNumber)
    except:
        exceptions = sys.exc_info()[0]
        print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()

    try:
        if InputNumber_ConvertedToFloat >= RangeMinValue and InputNumber_ConvertedToFloat <= RangeMaxValue:
            return InputNumber_ConvertedToFloat
        else:
            input("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. '" +
                      InputNameString +
                      "' must be in the range [" +
                      str(RangeMinValue) +
                      ", " +
                      str(RangeMaxValue) +
                      "] (value was " +
                      str(InputNumber_ConvertedToFloat) + "). Press any key (and enter) to exit.")

            sys.exit()
    except:
        exceptions = sys.exc_info()[0]
        print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread_SetupGUI(self, parent):

    print("Starting the GUI_Thread for object.")

    ###################################################
    self.root = parent
    self.parent = parent
    ###################################################

    ###################################################
    self.myFrame = Frame(self.root)

    if self.UseBorderAroundThisGuiObjectFlag == 1:
        self.myFrame["borderwidth"] = 2
        self.myFrame["relief"] = "ridge"

    self.myFrame.grid(row=self.GUI_ROW,
                      column=self.GUI_COLUMN,
                      padx=self.GUI_PADX,
                      pady=self.GUI_PADY,
                      rowspan=self.GUI_ROWSPAN,
                      columnspan=self.GUI_COLUMNSPAN,
                      sticky = self.GUI_STICKY)
    ###################################################

    ###################################################
    self.TKinter_LightGreenColor = '#%02x%02x%02x' % (150, 255, 150)  # RGB
    self.TKinter_LightBlueColor = '#%02x%02x%02x' % (150, 150, 255)  # RGB
    self.TKinter_LightRedColor = '#%02x%02x%02x' % (255, 150, 150)  # RGB
    self.TKinter_LightYellowColor = '#%02x%02x%02x' % (255, 255, 150)  # RGB
    self.TKinter_DefaultGrayColor = '#%02x%02x%02x' % (240, 240, 240)  # RGB
    ###################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread_StartRootLoopAndHandleExitOfGUI(self):

    ###################################################
    self.GUI_ready_to_be_updated_flag = 1
    ###################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def TimerCallbackFunctionWithFunctionAsArgument_SingleShot_NoParenthesesAfterFunctionName(self, CallbackAfterDeltaTseconds, FunctionToCall_NoParenthesesAfterFunctionName, ArgumentListToFunction):

    self.TimerObject = threading.Timer(CallbackAfterDeltaTseconds, FunctionToCall_NoParenthesesAfterFunctionName, ArgumentListToFunction) #Must pass arguments to callback-function via list as the third argument to Timer call
    self.TimerObject.daemon = True #Without the daemon=True, this recursive function won't terminate when the main program does.
    self.TimerObject.start()

    print("TimerCallbackFunctionWithFunctionAsArgument_SingleShot_NoParenthesesAfterFunctionName event fired to call function: '" + str(FunctionToCall_NoParenthesesAfterFunctionName.__name__) + "' at time " + str(self.getPreciseSecondsTimeStampString()))
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ListFunctionNamesInClass(self, ClassToBeChecked, FilterFunctionNamesWithLeadingUnderscoresFlag = 1):
    FunctionList_All = list()

    for FunctionName, item in ClassToBeChecked.__dict__.items():
        if isinstance(item, types.FunctionType):
            if FilterFunctionNamesWithLeadingUnderscoresFlag == 0:
                FunctionList_All.append(FunctionName)
            else:
                if FunctionName[0] != "_":
                    FunctionList_All.append(FunctionName)

    return FunctionList_All
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def SetAllFTDIdevicesLatencyTimer(self, FTDI_LatencyTimer_ToBeSet = 1):

    try:
        FTDI_LatencyTimer_ToBeSet = self.LimitNumber_IntOutputOnly(1, 16, FTDI_LatencyTimer_ToBeSet)

        FTDI_DeviceList = ftd2xx.listDevices()
        print("FTDI_DeviceList: " + str(FTDI_DeviceList))

        if FTDI_DeviceList != None:

            for Index, FTDI_SerialNumber in enumerate(FTDI_DeviceList):

                #################################
                try:
                    if sys.version_info[0] < 3: #Python 2
                        FTDI_SerialNumber = str(FTDI_SerialNumber)
                    else:
                        FTDI_SerialNumber = FTDI_SerialNumber.decode('utf-8')

                    FTDI_Object = ftd2xx.open(Index)
                    FTDI_DeviceInfo = FTDI_Object.getDeviceInfo()

                    '''
                    print("FTDI device with serial number " +
                          str(FTDI_SerialNumber) +
                          ", DeviceInfo: " +
                          str(FTDI_DeviceInfo))
                    '''

                except:
                    exceptions = sys.exc_info()[0]
                    print("FTDI device with serial number " + str(FTDI_SerialNumber) + ", could not open FTDI device, Exceptions: %s" % exceptions)
                #################################

                #################################
                try:
                    FTDI_Object.setLatencyTimer(FTDI_LatencyTimer_ToBeSet)
                    time.sleep(0.005)

                    FTDI_LatencyTimer_ReceivedFromDevice = FTDI_Object.getLatencyTimer()
                    FTDI_Object.close()

                    if FTDI_LatencyTimer_ReceivedFromDevice == FTDI_LatencyTimer_ToBeSet:
                        SuccessString = "succeeded!"
                    else:
                        SuccessString = "failed!"

                    print("FTDI device with serial number " +
                          str(FTDI_SerialNumber) +
                          " commanded setLatencyTimer(" +
                          str(FTDI_LatencyTimer_ToBeSet) +
                          "), and getLatencyTimer() returned: " +
                          str(FTDI_LatencyTimer_ReceivedFromDevice) +
                          ", so command " +
                          SuccessString)

                except:
                    exceptions = sys.exc_info()[0]
                    print("FTDI device with serial number " + str(FTDI_SerialNumber) + ", could not set/get Latency Timer, Exceptions: %s" % exceptions)
                #################################

        else:
            print("SetAllFTDIdevicesLatencyTimer ERROR: FTDI_DeviceList is empty, cannot proceed.")

    except:
        exceptions = sys.exc_info()[0]
        print("SetAllFTDIdevicesLatencyTimer, Exceptions: %s" % exceptions)
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def FindAssignAndOpenSerialPort(self):
    self.MyPrint_WithoutLogFile("FindAssignAndOpenSerialPort: Finding all serial ports...")

    ##############
    SerialNumberToCheckAgainst = str(self.DesiredSerialNumber)
    if self.my_platform == "linux" or self.my_platform == "pi":
        SerialNumberToCheckAgainst = SerialNumberToCheckAgainst[:-1] #The serial number gets truncated by one digit in linux
    else:
        SerialNumberToCheckAgainst = SerialNumberToCheckAgainst
    ##############

    ##############
    SerialPortsAvailable_ListPortInfoObjetsList = serial.tools.list_ports.comports()
    ##############

    ###########################################################################
    SerialNumberFoundFlag = 0
    for SerialPort_ListPortInfoObjet in SerialPortsAvailable_ListPortInfoObjetsList:

        SerialPortName = SerialPort_ListPortInfoObjet[0]
        Description = SerialPort_ListPortInfoObjet[1]
        VID_PID_SerialNumber_Info = SerialPort_ListPortInfoObjet[2]
        self.MyPrint_WithoutLogFile(SerialPortName + ", " + Description + ", " + VID_PID_SerialNumber_Info)

        if VID_PID_SerialNumber_Info.find(SerialNumberToCheckAgainst) != -1 and SerialNumberFoundFlag == 0: #Haven't found a match in a prior loop
            self.SerialPortNameCorrespondingToCorrectSerialNumber = SerialPortName
            SerialNumberFoundFlag = 1 #To ensure that we only get one device
            self.MyPrint_WithoutLogFile("FindAssignAndOpenSerialPort: Found serial number " + SerialNumberToCheckAgainst + " on port " + self.SerialPortNameCorrespondingToCorrectSerialNumber)
            #WE DON'T BREAK AT THIS POINT BECAUSE WE WANT TO PRINT ALL SERIAL DEVICE NUMBERS WHEN PLUGGING IN A DEVICE WITH UNKNOWN SERIAL NUMBE RFOR THE FIRST TIME.
    ###########################################################################

    ###########################################################################
    if(self.SerialPortNameCorrespondingToCorrectSerialNumber != "default"): #We found a match

        try: #Will succeed as long as another program hasn't already opened the serial line.

            self.SerialObject = serial.Serial(self.SerialPortNameCorrespondingToCorrectSerialNumber, self.SerialBaudRate, timeout=self.SerialTimeoutSeconds, parity=self.SerialParity, stopbits=self.SerialStopBits, bytesize=self.SerialByteSize)
            self.SerialConnectedFlag = 1
            self.MyPrint_WithoutLogFile("FindAssignAndOpenSerialPort: Serial is connected and open on port: " + self.SerialPortNameCorrespondingToCorrectSerialNumber)

        except:
            self.SerialConnectedFlag = 0
            self.MyPrint_WithoutLogFile("FindAssignAndOpenSerialPort: ERROR: Serial is physically plugged in but IS IN USE BY ANOTHER PROGRAM.")

    else:
        self.SerialConnectedFlag = -1
        self.MyPrint_WithoutLogFile("FindAssignAndOpenSerialPort: ERROR: Could not find the serial device. IS IT PHYSICALLY PLUGGED IN?")
    ###########################################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ConvertBytesObjectToString(self, InputBytesObject):

    if sys.version_info[0] < 3:  # Python 2
        OutputString = str(InputBytesObject)

    else:
        OutputString = InputBytesObject.decode('utf-8')

    return OutputString
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ConvertStructToDict(self, InputStruct):

    try:
        OutputDict = dict((field, getattr(InputStruct, field)) for field, _ in InputStruct._fields_)
        return OutputDict

    except:
        exceptions = sys.exc_info()[0]
        print("ConvertStructToDict, Exceptions: %s" % exceptions)
        traceback.print_exc()
        return dict()

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def AverageDataInQueueOfLists(self, InputQueue):
    try:

        if isinstance(InputQueue, Queue.Queue) == 1:

            InputQueueSize = InputQueue.qsize()

            if InputQueueSize > 0:
                DataElement = InputQueue.get()

                IsListFlag = 1
                ####
                if isinstance(DataElement, list) == 0:  # If not a list, make it one.
                    DataElement = [DataElement]
                    IsListFlag = 0
                ####

                DataElementListLength = len(DataElement)

                SumOfIndex_List = list()
                for Value in DataElement:
                    SumOfIndex_List.append(Value)  # Just to initialize SumOfIndex_List with the first element that we removed.

                ##########################################################################################################
                while InputQueue.qsize() > 0:
                    DataElementValue = InputQueue.get()

                    if IsListFlag == 0:
                        DataElementValue = [DataElementValue]

                    for Index in range(0, DataElementListLength):
                        SumOfIndex_List[Index] = SumOfIndex_List[Index] + DataElementValue[Index]

                ##########################################################################################################

                ##########################################################################################################
                AverageOfIndex_List = [0.0] * DataElementListLength
                for Index in range(0, DataElementListLength):
                    AverageOfIndex_List[Index] = SumOfIndex_List[Index] / InputQueueSize
                ##########################################################################################################

                return AverageOfIndex_List

            else:
                print("AverageDataInQueueOfLists, Error: Queue is empty!")
                return [-11111.0]

        else:
            print("AverageDataInQueueOfLists, Error: Input must be a Queue.Queue!")
            return [-11111.0]

    except:
        ##########################################################################################################
        exceptions = sys.exc_info()[0]
        print("AverageDataInQueueOfLists, Exceptions: %s" % exceptions)
        traceback.print_exc()

        #########################################################
        if InputQueue.qsize() > 0:
            DataElement = InputQueue.get()
            if isinstance(DataElement, list) == 1:
                return [-11111.0] * len(DataElement)
            else:
                return [-11111.0]
        else:
            return [-11111.0]
        #########################################################

        ##########################################################################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ConvertRotationMatrixToEulerAngles_RollPitchYawAbtXYZ(self, RotationMatrix):

    try:
        [Roll_AbtXaxis_Radians, Pitch_AbtYaxis_Radians, Yaw_AbtZaxis_Radians] = Rotation.from_matrix(RotationMatrix).as_euler("xyz") ################## must run with python 3.7.3

        #########################
        Roll_AbtXaxis_Degrees = Roll_AbtXaxis_Radians * 180.0 / math.pi
        Pitch_AbtYaxis_Degrees = Pitch_AbtYaxis_Radians * 180.0 / math.pi
        Yaw_AbtZaxis_Degrees = Yaw_AbtZaxis_Radians * 180.0/math.pi
        #########################

        DictToReturn = dict([("RollPitchYaw_AbtXYZ_List_Degrees", [Roll_AbtXaxis_Degrees, Pitch_AbtYaxis_Degrees, Yaw_AbtZaxis_Degrees]),
                             ("RollPitchYaw_AbtXYZ_List_Radians", [Roll_AbtXaxis_Radians, Pitch_AbtYaxis_Radians, Yaw_AbtZaxis_Radians])])

        return DictToReturn

    except:
        exceptions = sys.exc_info()[0]
        print("ConvertRotationMatrixToEulerAngles_RollPitchYawAbtXYZ, Exceptions: %s" % exceptions)
        traceback.print_exc()
        return dict()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ManualCalculation(self, QuaternionsInputListXYZW):

    try:
        #########################
        if self.IsInputList(QuaternionsInputListXYZW) != 1 or len(QuaternionsInputListXYZW) != 4:
            print("ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ManualCalculation Error: Input must be a list of length 4.")
            return dict()
        #########################

        #########################
        [X, Y, Z, W] = list(QuaternionsInputListXYZW)
        #print("X: " + str(X) + ", Y: " + str(Y) + ", Z: " + str(Z) + ", W: " + str(W))
        #########################

        #https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles

        ######################### Roll abt X-axis
        sinr_cosp = 2.0*(W*X + Y*Z)
        cosr_cosp = 1 - 2.0*(X*X + Y*Y)
        Roll_AbtXaxis_Radians = math.atan2(sinr_cosp, cosr_cosp)
        #########################

        ######################### #Pitch aby Y-axis
        sinp = 2.0*(W*Y - Z*X)
        if abs(sinp) >= 1.0:
            Pitch_AbtYaxis_Radians = math.copysign(math.pi/2.0, sinp)
        else:
            Pitch_AbtYaxis_Radians = math.asin(sinp)
        #########################

        ######################### Yaw about Z-axis
        siny_cosp = 2.0*(W*Z + X*Y)
        cosy_cosp = 1 - 2.0*(Y*Y + Z*Z)
        Yaw_AbtZaxis_Radians = math.atan2(siny_cosp, cosy_cosp)
        #########################

        #########################
        Roll_AbtXaxis_Degrees = Roll_AbtXaxis_Radians * 180.0/math.pi
        Pitch_AbtYaxis_Degrees = Pitch_AbtYaxis_Radians * 180.0/math.pi
        Yaw_AbtZaxis_Degrees = Yaw_AbtZaxis_Radians * 180.0/math.pi
        #########################

        DictToReturn = dict([("RollPitchYaw_AbtXYZ_List_Degrees", [Roll_AbtXaxis_Degrees, Pitch_AbtYaxis_Degrees, Yaw_AbtZaxis_Degrees]),
                             ("RollPitchYaw_AbtXYZ_List_Radians", [Roll_AbtXaxis_Radians, Pitch_AbtYaxis_Radians, Yaw_AbtZaxis_Radians])])

        return DictToReturn

    except:
        exceptions = sys.exc_info()[0]
        print("ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ManualCalculation, Exceptions: %s" % exceptions)
        traceback.print_exc()
        return dict()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ScipyCalculation(self, QuaternionsInputListXYZW):

    try:
        #########################
        if self.IsInputList(QuaternionsInputListXYZW) != 1 or len(QuaternionsInputListXYZW) != 4:
            print("ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ScipyCalculation Error: Input must be a list of length 4.")
            return dict()
        #########################

        #########################
        [X, Y, Z, W] = list(QuaternionsInputListXYZW)
        #print("X: " + str(X) + ", Y: " + str(Y) + ", Z: " + str(Z) + ", W: " + str(W))
        #########################

        RotationObject = Rotation.from_quat(QuaternionsInputListXYZW)
        [Roll_AbtXaxis_Radians, Pitch_AbtYaxis_Radians, Yaw_AbtZaxis_Radians] = RotationObject.as_euler("xyz")  ################## must run with python 3.7.3

        #########################
        Roll_AbtXaxis_Degrees = Roll_AbtXaxis_Radians * 180.0/math.pi
        Pitch_AbtYaxis_Degrees = Pitch_AbtYaxis_Radians * 180.0/math.pi
        Yaw_AbtZaxis_Degrees = Yaw_AbtZaxis_Radians * 180.0/math.pi
        #########################

        DictToReturn = dict([("RollPitchYaw_AbtXYZ_List_Degrees", [Roll_AbtXaxis_Degrees, Pitch_AbtYaxis_Degrees, Yaw_AbtZaxis_Degrees]),
                             ("RollPitchYaw_AbtXYZ_List_Radians", [Roll_AbtXaxis_Radians, Pitch_AbtYaxis_Radians, Yaw_AbtZaxis_Radians])])

        return DictToReturn

    except:
        exceptions = sys.exc_info()[0]
        print("ConvertQuaterionsToEulerAngles_RollPitchYawAbtXYZ_ScipyCalculation, Exceptions: %s" % exceptions)
        traceback.print_exc()
        return dict()
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def TimeFunctionCallOverManyIterations(self, FunctionToCall, ArgumentList, NumberOfIterations = 1000):

    StartingTime = time.time()

    for Counter in range(1, NumberOfIterations):
        FunctionToCall(*ArgumentList) #* says to unwrap the list of arguments into individual arguments.

    EndingTime = time.time()

    TimePerFunctionCallInseconds = (EndingTime - StartingTime) / float(NumberOfIterations)
    print("TimeFunctionCallOverManyIterations: After running " + str(NumberOfIterations) + " iterations, found that TimePerFunctionCallInseconds for function '" + FunctionToCall.__name__ + "': " + str(TimePerFunctionCallInseconds))

    return TimePerFunctionCallInseconds
##########################################################################################################
##########################################################################################################








