from Project import app
from flask import jsonify, request
    
import subprocess
import os
import glob
        

@app.route("/application_status")
@app.route("/")
def default():
    return jsonify("Every thing is working fine")


@app.route("/run_macro", methods=["GET", "POST"])
def run_macro():
    try:
        data = request.form
        data = data.to_dict()
        macro_name = data["Name"]
        responce = subprocess.call(['cscript.exe', macro_name])
        return responce
    except Exception as Error:
        print(Error)


@app.route("/insert_macro", methods=["GET", "POST"])
def insert_macro():
    try:
        f = request.files['file']
        folder_name = str(f.filename).split('.')[0]    
        folder_path = str(os.getcwd()) + f"\\Macro Files\\{folder_name}"
        file_path  = f"{folder_path}\\{f.filename}"
        
        l = list(glob.glob(f"{os.getcwd()}\\Macro Files\\*"))
        if folder_path in l:
            return jsonify({"status":False,"message":"Macro already exists"})
        else:
            os.mkdir(folder_path)
            f.save(file_path)
        return  jsonify({"status":True,"message":"Macro created"})
    except Exception as Error:
        print(Error)
        return  jsonify(False)


@app.route("/update_macro", methods=["GET", "POST"])
def update_macro():
    try:
        f = request.files['file']
        folder_name = str(f.filename).split('.')[0]    
        folder_path = str(os.getcwd()) + f"\\Macro Files\\{folder_name}"
        file_path  = f"{folder_path}\\{f.filename}"
        
        l = list(glob.glob(f"{os.getcwd()}\\Macro Files\\*"))
        if folder_path not in l:
            return jsonify({"status":False,"message":"Macro not exists"})
        else:
            os.mkdir(folder_path)
            f.save(file_path)
        return  jsonify({"status":True,"message":"Macro updated"})
    except Exception as Error:
        print(Error)
        return  jsonify(False)
