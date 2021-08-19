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
import psutil

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
    try:
        # for proc in psutil.process_iter():
        #     if proc.name() == "excel.exe":
        #         proc.kill()
        for proc in psutil.process_iter():
            try:
                PROCNAME = "excel.exe"
                if proc.name().lower() == PROCNAME.lower():
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        if os.path.exists("D:\\home\\ProcessingUnit\\TempSingleFile\\helloworld.xlsm"):
            listOfFiles = getListOfFiles((config_dic["YourLocalPath"]) + '\\')
            if listOfFiles:
                for i in listOfFiles:
                    os.remove(i)
                    info(f"deleted old file: {i}")    
            
            info("0"*40)
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
            for proc in psutil.process_iter():
                try:
                    PROCNAME = "excel.exe"
                    if proc.name().lower() == PROCNAME.lower():
                        proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            '''Killing excel in task manager'''
            for proc in psutil.process_iter():
                if proc.name() == "excel.exe":
                    proc.kill()
            info("1"*40)
            listOfFiles = getListOfFiles((config_dic["YourLocalPath"]) + '\\')
            if listOfFiles:
                for i in listOfFiles:
                    filepath = i
                    filename = i.split("\\")[-1]
                    res = config_dic["FilePath"]
                    data = open(filepath, 'rb').read()
                    blobdata = base64.b64encode(data).decode('UTF-8')
                    info("2"*40)
                    '''inserting file to azure'''
                    az.insert_file_azure(share_name, res, filename, base64.b64decode(blobdata))
                    info("3"*40)
                    os.remove(i)
    except com_error as e:
        info("---------------------------------------------------------------------------------------------")
        info(e)
        pass
        # com_error
            
    return jsonify("hello world")
