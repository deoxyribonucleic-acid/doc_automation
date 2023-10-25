import os
import re

from docxtpl import DocxTemplate
from tools.FileManager import getPath

def Template(save_path,data):
    # print('开始填充模板')
    graduation_design=data
    path = getPath("File_template/")
    files = []
    for file in os.listdir(path):
        files.append(path + file)
    for file in files:
        filename = re.findall(r"File_template/(.+?)-模板", file)
        if len(filename)==0:
            # print("Template.py: found dirty file {} in template folder".format(file))
            continue
        tpl = DocxTemplate(file)
        tpl.render(graduation_design)  # 渲染替换
        res_path = save_path + "{}-{}.docx".format(graduation_design['name'], filename[0])
        # print('正在生成'+res_path)
        tpl.save(res_path)


