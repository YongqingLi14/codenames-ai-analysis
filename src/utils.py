# convert ipynb to html 
import os
import subprocess

def convert_nbook(directory):
    os.chdir(directory)
    #run notebook
    os.system('jupyter nbconvert --to notebook --inplace --execute Report.ipynb')
    #convert notebook to html
    os.system('jupyter nbconvert --to html Report.ipynb')