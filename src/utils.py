# convert ipynb to html 
import os
import subprocess

def convert_nbook(directory):
    os.chdir(directory)
    run_cmd = 'jupyter nbconvert --to notebook --inplace --execute Report.ipynb'
    convert_cmd = 'jupyter nbconvert --to html Report.ipynb'
    subprocess.run(['/bin/bash', '-c', run_cmd])
    subprocess.run(['/bin/bash', '-c', convert_cmd])