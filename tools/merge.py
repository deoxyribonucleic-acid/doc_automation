from os import path, listdir, remove, mkdir
import sys
from re import findall
from shutil import copyfile
from time import sleep
from PyPDF2 import PdfMerger


if sys.platform == 'darwin' or sys.platform == 'linux':
    from docx2pdf import convert
if sys.platform == 'win32':
    from win32com.client import constants, gencache

from tools.doc2docx import doc_to_docx

def del_file(path=sys.argv[0]+'/temp_pdf'):
    ls = listdir(path)
    for i in ls:
        c_path = path.join(path, i)
        if path.isdir(c_path):  # 如果是文件夹那么递归调用一下
            del_file(c_path)
        else:  # 如果是一个文件那么直接删除
            remove(c_path)
    # print('文件已经清空完成')

def Word_to_Pdf(Word_path,Pdf_path):
    if sys.platform == 'win32':
        word = gencache.EnsureDispatch('Word.Application')
        doc = word.Documewin32s.Open(Word_path,ReadOnly = 1)
        # 转换方法
        doc.ExportAsFixedFormat(Pdf_path,constants.wdExportFormatPDF)
        doc.Close()  # 关闭原来word文件
        word.Quit()
    if sys.platform == 'darwin' or sys.platform == 'linux':
        convert(Word_path, Pdf_path)
    sleep(0.1)


def merge(name,file_path,res_path):
    for file in file_path:
        if 'pdf' in file:
            new_file = file.split('/')
            filename = new_file[len(new_file) - 1]
            filename = findall(r"(.+?).pdf", filename)[0]
            if not path.exists(res_path+'/temp_pdf'):
                mkdir(res_path+'/temp_pdf')
            pdf_path=res_path+'/temp_pdf/'+filename+'.pdf'
            # print(pdf_path)
            copyfile(file,pdf_path)
        else:
            file=doc_to_docx(file)
            new_file = file.split('/')
            filename = new_file[len(new_file) - 1]
            filename=findall(r"(.+?).docx", filename)[0]
            if not path.exists(res_path+'/temp_pdf'):
                mkdir(res_path+'/temp_pdf')
            pdf_path=res_path+'/temp_pdf/'+filename+'.pdf'
            word_path=file
            # print('word_path',word_path)
            # print('pdf_path',pdf_path)
            Word_to_Pdf(word_path,pdf_path)

    files=[]
    zpath=res_path+'/temp_pdf/'
    for file in listdir(zpath):
        if file.endswith(".pdf"):
            files.append(zpath + file)

    file_merger = PdfMerger()

    #按照特定顺序读取
    for file in files:
        if '开题报告' in file:
            file_merger.append(file, import_outline=False)

    for file in files:
        if '开题评审' in file:
            file_merger.append(file, import_outline=False)

    for file in files:
        if '中期报告' in file:
            file_merger.append(file, import_outline=False)

    for file in files:
        if '中期检查' in file:
            file_merger.append(file, import_outline=False)

    for file in files:
        if '第一阶段' in file:
            file_merger.append(file, import_outline=False)

    for file in files:
        if '第二阶段' in file:
            file_merger.append(file, import_outline=False)

    for file in files:
        if '第三阶段' in file:
            file_merger.append(file, import_outline=False)

    for file in files:
        if '第四阶段' in file:
            file_merger.append(file, import_outline=False)

    for file in files:
        if '第五阶段' in file:
            file_merger.append(file, import_outline=False)

    for file in files:
        if '第六阶段' in file:
            file_merger.append(file, import_outline=False)

    for file in files:
        if '评语' in file:
            file_merger.append(file, import_outline=False)

    for file in files:
        if '简洁报告' in file:
            file_merger.append(file, import_outline=False)

    for file in files:
        if '答辩评审' in file:
            file_merger.append(file, import_outline=False)

    for file in files:
        if '成绩' in file:
            file_merger.append(file, import_outline=False)


    merge_res_path = res_path + '/'+name+'-合并文件'+'.pdf'
    # print(merge_res_path)
    file_merger.write(merge_res_path)


if __name__ == '__main__':
    name = "1111"
    file_path = ['/Users/centaurus/Desktop/out/方法-中国传媒大学毕业论文（设计）中期报告表.docx','/Users/centaurus/Desktop/out/方法-中国传媒大学毕业论文（设计）指导教师评语表.docx']
    out_path = '/Users/centaurus/Desktop/merge/'
    merge(name,file_path,out_path)