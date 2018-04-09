#-*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('UTF8')


import pip,os
pip.main(["install","easygui","xlutils","xlsxwriter","python-pptx"])
print u"la instalación ha finalizado correctamente"
os.system("pause")
