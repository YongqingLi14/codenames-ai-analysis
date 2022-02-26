import sys
import os
import json


sys.path.insert(0, 'src')
from ai_ai_test import ai_ai_test, ai_ai_stats
from ai_human_test import ai_human_test, ai_human_stats
from optimal_conservative_search import conservative_test, conservative_stats
from utils import convert_nbook


def main(targets):
	#test targets
	conservative_plot_test = json.load(open('config/conservative-plot-test-params.json'))
	ai_plot_test = json.load(open('config/ai-plot-test-params.json'))
	human_plot_test = json.load(open('config/human-plot-test-params.json'))

	#all targets
	conservative_data = json.load(open('config/conservative-data-params.json'))
	ai_data = json.load(open('config/ai-data-params.json'))
	human_data = json.load(open('config/human-data-params.json'))

	conservative_plot = json.load(open('config/conservative-plot-params.json'))
	ai_plot = json.load(open('config/ai-plot-params.json'))
	human_plot = json.load(open('config/human-plot-params.json'))

	#utility 
	utils_param = json.load(open('config/utils-params.json'))

	if not os.path.isdir("figures"):
		os.makedirs("figures")

	if 'test' in targets: 
		#generate plots for analysis using test data
		conservative_stats(**conservative_plot_test)
		ai_ai_stats(**ai_plot_test)
		ai_human_stats(**human_plot_test)
		
		#convert notebook to html
		convert_nbook(**utils_param)


	if 'all' in targets:
		#run simulations and collect data
		conservative_test(**conservative_data)
		ai_ai_test(**ai_data) 
		ai_human_test(**human_data)

		# #generate plots for analysis
		conservative_stats(**conservative_plot)
		ai_ai_stats(**ai_plot)
		ai_human_stats(**human_plot)

		#convert notebook to html
		convert_nbook(**utils_param)


	if 'clean' in targets: #restore repo to original/clean state
		os.system('rm -r figures')
		os.system('rm -r data')
		os.chdir("notebooks")
		os.system('rm Report.html')



if __name__ == '__main__':
	targets = sys.argv[1:]
	main(targets)




