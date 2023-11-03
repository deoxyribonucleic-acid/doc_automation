from docxtpl import DocxTemplate
from tools.FileManager import getPath
def assess(mode,save_path,data):
    
    # print('开始执行')

    inform=data

    # print(mode)

    file=''
    filename=''
    if mode == 0:
        # print('开题')
        filename='开题评审表'
        file = getPath("File_template/中国传媒大学本科毕业论文（设计）开题检查评审表-模板.docx")  # 模板文件

    elif mode == 1:
        # print('中期')
        filename = '中期评审表'
        file = getPath("File_template/中国传媒大学毕业论文（设计）中期检查评审表-模板.docx")


    elif mode == 2:
        # print('答辩')
        filename = '答辩评审表'
        file = getPath("File_template/中国传媒大学本科毕业论文（设计）答辩评审表-模板.docx")


    # print(file)
    tpl = DocxTemplate(file)
    tpl.render(inform)
    res_path = save_path + "/{}-{}.docx".format(inform['name'], filename)
    # print(res_path)
    tpl.save(res_path)
    return res_path
