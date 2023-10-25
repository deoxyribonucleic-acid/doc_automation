import os,sys

import time
if sys.platform == 'darwin' or sys.platform == 'linux':
    pass
    #import doc2docx
if sys.platform == 'win32' :
    from win32com import client as wc
    import win32com
    import win32com.client

def closesoft():
    # print('''挂载程序关闭中……''')
    if sys.platform == 'darwin' or sys.platform == 'linux':
        return
    if sys.platform == 'win32' :
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
        if sys.platform == 'darwin' or sys.platform == 'linux':
            pass
            #doc2docx.doc_to_docx(file_path)
        if sys.platform == 'win32' :
            word = wc.Dispatch("Word.Application")  # 打开word应用程序
            doc = word.Documents.Open(file_path,ReadOnly = 1)  # 打开word文件
            doc.SaveAs('{}x'.format(file_path), 12)  # 另存为后缀为".docx"的文件，其中参数12指docx文件
            doc.Close()  # 关闭原来word文件w
            ord.Quit()
        res_path = '{}x'.format(file_path)
        os.remove(file_path)
        time.sleep(0.5)
    return res_path
    # print("完成！")


if __name__ == '__main__':
    file_path = '../out/方法-中国传媒大学毕业论文（设计）中期检查评审表.docx'
    out_path = '../merge/111.docx'
    doc_to_docx(file_path)
    closesoft()