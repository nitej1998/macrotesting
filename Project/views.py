from Project import app
from flask import jsonify, request


import sys  
import os, os.path
import win32com.client  
import win32com.client as win32
import threading
from queue import Queue
import pythoncom
import threading
from queue import Queue


@app.route("/")
def default():
    if os.path.exists("D:\\home\\ProcessingUnit\\TempSingleFile\\simpleMacroForPython.xlsm"):
        pythoncom.CoInitialize()
        xl = win32.Dispatch('Excel.Application')
        xl.Application.visible = False
        file_path = "D:\\home\\ProcessingUnit\\TempSingleFile\\simpleMacroForPython.xlsm"
        separator_char = os.sep
        try:
            wb = xl.Workbooks.Open(os.path.abspath(file_path))
            xl.Application.run("simpleMacroForPython.xlsm!main.simpleMain")
            # file_path.split(sep=separator_char)[-1] + "!main.simpleMain" 
            wb.Save()
            wb.Close()
            xl.Application.Quit()
            del xl
        except Exception as ex:
            xl.Workbooks(1).Close(SaveChanges=0)
            xl.Application.Quit()
            xl=0
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    return jsonify("Every thing is working fine")

@app.route("/macro", methods=["POST", "Get"])
def macroroute():
    if os.path.exists("C:\\Users\\Admin\\Downloads\\testing.xlsm"):
        print("1"*40)
        pythoncom.CoInitialize()
        xl=win32com.client.Dispatch("Excel.Application")
        print("2"*40)
        wb = xl.Workbooks.Open(os.path.abspath("C:\\Users\\Admin\\Downloads\\testing.xlsm"))
        print("3"*40)
        xl.Application.Run("testing.xlsm!Module1.Macro2")
        print("4"*40)
        wb.Save()
        wb.Close()
        #xl.Application.Save("C:/Users/Admin/Downloads/testing.xlsm")
        # if you want to save then uncomment this line and change delete the ", ReadOnly=1" part from the open function.
        xl.Application.Quit() # Comment this out if your excel script closes
        print("5"*40)
        del xl
        print("6"*40)
 
    return jsonify("hello world")

@app.route("/macro1", methods=["POST", "Get"])
def macro1():
    # C:\\Users\\Admin\\Downloads\\simpleMacroForPython.xlsm
    if os.path.exists("D:\\home\\ProcessingUnit\\TempSingleFile\\testing.xlsm"):
        pythoncom.CoInitialize()
        xl = win32.Dispatch('Excel.Application')
        xl.Application.visible = False
        file_path = "D:\\home\\ProcessingUnit\\TempSingleFile\\testing.xlsm"
        separator_char = os.sep
        try:
            wb = xl.Workbooks.Open(os.path.abspath(file_path))
            xl.Application.run("testing.xlsm!Module1.Macro2")
            # file_path.split(sep=separator_char)[-1] + "!main.simpleMain" 
            wb.Save()
            wb.Close()
            xl.Application.Quit()
            del xl
        except Exception as ex:
            xl.Workbooks(1).Close(SaveChanges=0)
            xl.Application.Quit()
            xl=0
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    return jsonify("hello world")

