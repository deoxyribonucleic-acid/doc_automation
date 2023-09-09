import os
import re

from docxtpl import DocxTemplate


def Template(save_path,data):
    print('开始执行')
    graduation_design=data
    path = os.getcwd() + '/File_template/'  # 模板文件夹
    files = []
    for file in os.listdir(path):
        files.append(path + file)
    for file in files:
        filename = re.findall(r"File_template/(.+?)-模板", file)
        tpl = DocxTemplate(file)
        tpl.render(graduation_design)  # 渲染替换
        res_path = save_path + "{}-{}.docx".format(graduation_design['name'], filename[0])
        string=str('正在生成'+res_path)
        tpl.save(res_path)


