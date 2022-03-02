# convert ipynb to html 
import os
import subprocess

def convert_nbook(directory):
    os.chdir(directory)
    os.system('jupyter nbconvert --to html Report.ipynb')