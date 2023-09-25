#!/bin/python

import platform
import os
import glob
import shutil
import datetime

FORCE_REBUILD = True

UI_SOURCE_FOLDER = './forms'
UIPY_TARGET_FOLDER = './pyforms'
QRC_SOURCE_FOLDER = '.'
QRC_PY_TARGET_FOLDER = UIPY_TARGET_FOLDER
QRC_FILENAME = "materials.qrc"



WIN_UIC_EXEC = r"C:\Users\priganns\AppData\Roaming\Python\Python311\Scripts\pyside6-uic.exe "
MAC_UIC_EXEC = ""
LINUX_UIC_EXEC = "pyside6-uic"

MAC_RCC_EXEC = ""
WIN_RCC_EXEC = r"C:\Users\priganns\AppData\Roaming\Python\Python311\Scripts\pyside6-rcc.exe "
LINUX_RCC_EXEC = "pyside6-rcc"

class CmdCol:
    Black = "\u001b[30;1m"
    Red ="\u001b[31:1m"
    Green=  "\u001b[32;1m"
    Yellow= "\u001b[33;1m"
    Blue=  "\u001b[34;1m"
    Magenta= "\u001b[35;1m"
    Cyan = "\u001b[36;1m"
    White = "\u001b[37;1m"
    Reset =  "\u001b[0m"


def print_info(info_str):
    i = 'INFO'
    print(CmdCol.Cyan+f"[  {i:<5} ] {info_str}"+CmdCol.Reset) 


def print_warn(s):
    i = 'WARN'
    print(CmdCol.Yellow+f"[  {i:<5} ] {s}"+CmdCol.Reset) 

def print_err(s):
    i = 'ERROR'
    print(CmdCol.Red+f"[  {i:<5} ] {s}"+CmdCol.Reset) 


def build_target_folder(targetpath):
    if os.path.exists(targetpath):
        print_warn("Folder exists, deleting content.")
        shutil.rmtree(targetpath)
    print_info(f"Creating {targetpath} folder")
    os.mkdir(targetpath)
    with open(targetpath+"/__init__.py",'w') as initFile:
        initFile.write(f"#Auto Generated init File\n#Created {datetime.datetime.now()}\nfrom . import materials_rc")



def build_ui_files(sourcepath,targetpath):
    sys_name = platform.system()
    print_info(f"Converting:")
    maxUiFiles = len(glob.glob1(sourcepath,"*.ui"))
    convertCounter = 0
    for file in os.listdir(sourcepath):
        

        if file.endswith('.ui'):
            if sys_name == 'Darwin':       
               exec_path = MAC_UIC_EXEC
            elif sys_name == 'Windows':  
                exec_path = WIN_UIC_EXEC
            else:     
                exec_path = LINUX_UIC_EXEC
            
            ret = os.system(exec_path+f" {sourcepath}/{file}" +f" -o {targetpath}/ui_{file.replace('.ui','.py')}")
            if ret:
                print_err(f"Error during system call: {ret}")
            convertCounter+=1
            print(f"[{round(convertCounter/maxUiFiles*100,1):<5} % ] "+f"{sourcepath+'/'+file:<40} -->\t{UIPY_TARGET_FOLDER}/ui_{file.replace('.ui','.py')}")

def build_resources(sourcepath,targetpath,filename):
    sys_name = platform.system()
    print_info("Rebuilding QRC Resources:")
    if sys_name == 'Darwin':       
            exec_path = MAC_RCC_EXEC
    elif sys_name == 'Windows':  
        exec_path = WIN_RCC_EXEC
    else:     
        exec_path = LINUX_RCC_EXEC

    os.system(exec_path+f" {sourcepath+'/'+filename} -o {targetpath+'/'+filename.replace('.qrc','_rc.py')}")
    print(f"[  {'DONE':<5} ] {sourcepath+'/'+filename:<40} -->\t{targetpath+'/'+filename.replace('.qrc','_rc.py')}")

def clean_ui_files(uiFilePath):
    stat = 'import materials_rc'
    print_info(f"Replacing wrong import statement: {stat}")

    fileToChange = len(glob.glob1(uiFilePath,"ui_*.py"))
    filesChanged = 0
    for file in os.listdir(uiFilePath):
        if file[0:3] == 'ui_':
            if remove_false_import_statement(uiFilePath+'/'+file,stat):        
                filesChanged+=1
                print(f"[  DONE  ] "+f"{uiFilePath}/{file:<25}")
        




def remove_false_import_statement(file,statement):
    with open(file,'r') as pIn:
        buf = pIn.read()
    res = buf.replace(statement,'#'+statement)

    with open(file,'w') as pOut:
        pOut.write(res)
    
    return not buf==res

def force_rebuild():

    print_info(f"FORCE_REBUILD: {FORCE_REBUILD}")
    build_target_folder(UIPY_TARGET_FOLDER)
    build_resources(QRC_SOURCE_FOLDER,QRC_PY_TARGET_FOLDER,QRC_FILENAME)
    build_ui_files(UI_SOURCE_FOLDER,UIPY_TARGET_FOLDER)
    clean_ui_files(UIPY_TARGET_FOLDER)

if __name__ == '__main__':

    if FORCE_REBUILD:
        force_rebuild()


