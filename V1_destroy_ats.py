#------------HEADER--------------------------------
import docx 
from docxtpl import DocxTemplate
import re
import os
os.system("cls") #use this for windows. change to os.system("clear") for linux

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

with open('word2.txt') as f:
    cont = f.read()

print(colorText(cont))


cv = input('CV FILE: ')
job = input('JOB DESCRIPTION FILE: ')
print('\nExtracting Data From CV..')

#---------------------HEADERS FINISHED-----------------------------


print('Extracting Job Description Data..\n')
with open(job) as f:
    job_desc = f.read()
job_desc = job_desc.split('\n')

print(job_desc)
print('Job Description: ')
for x in job_desc:
    print(x)
print('')
dic_of_edit = {'one':0,
    'two':1,
    'three':2,
    'four':3,
    'five':4,
    'six':5,
    'seven':6,
    'eight':7,
    'nine':8,
    'ten':9}

# print(dic_of_edit)
for k,v in dic_of_edit.items():
    dic_of_edit[k] = job_desc[int(v)]

cont = input('Generate Anti-ATS CV? [Y/N] ')
if cont.lower() == 'n':
    exit()
def mkw():
    tpl = DocxTemplate(cv)
    context = dic_of_edit
    tpl.render(context)
    tpl.save("cv_anti_ats.docx")

mkw()
