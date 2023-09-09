import os
from win32com import client as wc
import time
import win32com
import win32com.client

def closesoft():
    print('''挂载程序关闭中……
          ''')
    wc = win32com.client.constants
    try:
        wps = win32com.client.gencache.EnsureDispatch('word.application')
    except:
        wps = win32com.client.gencache.EnsureDispatch('wps.application')
    else:
        wps = win32com.client.gencache.EnsureDispatch('kwps.application')
    try:
        wps.Documents.Close()
        wps.Documents.Close(wc.wdDoNotSaveChanges)
        wps.Quit()
    except:
        pass

def doc_to_docx(file_path):
    res_path=file_path
    if os.path.splitext(file_path)[1] == '.doc':
        word = wc.Dispatch("Word.Application")  # 打开word应用程序
        doc = word.Documents.Open(file_path,ReadOnly = 1)  # 打开word文件
        doc.SaveAs('{}x'.format(file_path), 12)  # 另存为后缀为".docx"的文件，其中参数12指docx文件
        res_path = '{}x'.format(file_path)
        doc.Close()  # 关闭原来word文件
        os.remove(file_path)
        word.Quit()
        time.sleep(0.5)
    return res_path
    print("完成！")
