from Project import app
from flask import jsonify, request
# from azure.storage.common.models import LocationMode
from Project.azure import AZURE, getListOfFiles, create_directory_local, share_name
from .logger import info, logger, get_time, config_dic
# from .models import DB
from .azure import AZURE,share_name


import sys  
import os, os.path
import win32com.client  
import win32com.client as win32
import threading
from queue import Queue
import pythoncom
import threading
from queue import Queue
import base64
from pywintypes import com_error
import time

@app.route("/")
def default():
    # az = AZURE()
    # if os.path.exists("D:\\home\\ProcessingUnit\\TempSingleFile\\helloworld.xlsm"):
    #     pythoncom.CoInitialize()
    #     xl = win32.Dispatch('Excel.Application')
    #     xl.Application.visible = False
    #     file_path = "D:\\home\\ProcessingUnit\\TempSingleFile\\helloworld.xlsm"
    #     separator_char = os.sep
    #     try:
    #         wb = xl.Workbooks.Open(os.path.abspath(file_path))
    #         xl.Application.run("helloworld.xlsm!Module1.helloworldmacro")
    #         # file_path.split(sep=separator_char)[-1] + "!main.simpleMain" 
    #         wb.Save()
    #         wb.Close()
    #         xl.Application.Quit()
    #         del xl
    #         '''inserting file to azure'''
    #         filepath = "D:\\home\\ProcessingUnit\\TempSingleFile\\output1.xlsx"
    #         filename = "output1.xlsx"
    #         res = config_dic["FilePath"]
    #         data = open(filepath, 'rb').read()
    #         blobdata = base64.b64encode(data).decode('UTF-8')
    #         az.insert_file_azure(share_name, res, filename, base64.b64decode(blobdata))
    #     except Exception as ex:
    #         xl.Workbooks(1).Close(SaveChanges=0)
    #         xl.Application.Quit()
    #         xl=0
    #         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    #         message = template.format(type(ex).__name__, ex.args)
    #         print(message)

    return jsonify("Every thing is working fine")

@app.route("/macro", methods=["POST", "Get"])
def macroroute():
    az = AZURE()
    if os.path.exists("D:\\home\\ProcessingUnit\\TempSingleFile\\helloworld.xlsm"):
        
        try:
            info("0"*40)
            if os.path.exists("D:\\home\\ProcessingUnit\\TempSingleFile\\output1.xlsx"):
                os.remove("D:\\home\\ProcessingUnit\\TempSingleFile\\output1.xlsx")
                print("5"*40)
            pythoncom.CoInitialize()
            xl = win32.Dispatch('Excel.Application')
            xl.Application.visible = False
            path1 = "D:\\home\\ProcessingUnit\\TempSingleFile\\helloworld.xlsm"
            wb = xl.Workbooks.Open(os.path.abspath(path1))
            xl.Application.run("helloworld.xlsm!Module1.helloworldmacro")
            wb.Save()
            wb.Close()
            xl.Application.Quit()
            del xl
            info("1"*40)
            '''inserting file to azure'''
            filepath = "D:\\home\\ProcessingUnit\\TempSingleFile\\output1.xlsx"
            filename = "output1.xlsx"
            res = config_dic["FilePath"]
            data = open(filepath, 'rb').read()
            blobdata = base64.b64encode(data).decode('UTF-8')
            info("2"*40)
            az.insert_file_azure(share_name, res, filename, base64.b64decode(blobdata))
            info("3"*40)
            os.remove("D:\\home\\ProcessingUnit\\TempSingleFile\\output1.xlsx")
        except com_error as e:
            pass
            # com_error
            
    return jsonify("hello world")
