import sys
import os
import json


sys.path.insert(0, 'src')
from ai_ai_test import ai_ai_test, ai_ai_stats
from ai_human_test import ai_human_test, ai_human_stats
from utils import convert_nbook


def main(targets):
    #test targets
    ai_plot_test = json.load(open('config/ai-plot-test-params.json'))
    human_plot_test = json.load(open('config/human-plot-test-params.json'))

    #all targets
    ai_data = json.load(open('config/ai-data-params.json'))
    human_data = json.load(open('config/human-data-params.json'))

    ai_plot = json.load(open('config/ai-plot-params.json'))
    human_plot = json.load(open('config/human-plot-params.json'))

    #utility 
    utils_param = json.load(open('config/utils-params.json'))

    if not os.path.isdir("figures"):
        os.makedirs("figures")

    if 'test' in targets: 
        #generate plots for analysis using test data
        ai_ai_stats(**ai_plot_test)
        ai_human_stats(**human_plot_test)

        #convert notebook to html
        convert_nbook(**utils_param)


    if 'all' in targets:
        #run simulations and collect data
        ai_ai_test(**ai_data) 
        ai_human_test(**human_data)

        #generate plots for analysis
        ai_ai_stats(**ai_plot)
        ai_human_stats(**human_plot)

        #convert notebook to html
        convert_nbook(**utils_param)


    if 'clean' in targets: #restore repo to original/clean state
        os.system('rm -r figures')
        if os.path.isdir('./data'): 
            os.system('rm -r data')
        os.chdir("notebooks")
        os.system('rm Report.html')



if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)




