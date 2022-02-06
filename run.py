import sys
import os
import json


sys.path.insert(0, 'src')
from ai_ai_test import ai_test, ai_stats
# from AI_Human_test import 
from optimal_conservative_search import conservative_test, conservative_stats
from utils import convert_nbook


def main(targets):
	ai_plot_test = json.load(open('config/ai-plot-test-params.json'))
	conservative_plot_test = json.load(open('config/conservative-plot-test-params.json'))

	ai_data = json.load(open('config/ai-data-params.json'))
	conservative_data = json.load(open('config/conservative-data-params.json'))
	ai_plot = json.load(open('config/ai-plot-params.json'))
	conservative_plot = json.load(open('config/conservative-plot-params.json'))

	utils_param = json.load(open('config/utils-params.json'))

	if not os.path.isdir("figures"):
		os.makedirs("figures")

	if 'test' in targets: 
		#generate plots for analysis
		ai_stats(**ai_plot_test)
		conservative_stats(**conservative_plot_test)

		#convert notebook to html
		convert_nbook(**utils_param)


	if 'all' in targets:
		#run simulations and collect data
		ai_test(**ai_data) 
		conservative_test(**conservative_data)

		#generate plots for analysis
		ai_stats(**ai_plot)
		conservative_stats(**conservative_plot)

		#convert notebook to html
		convert_nbook(**utils_param)


	# if 'clean' in targets: #rm all file/figure outputs




if __name__ == '__main__':
	targets = sys.argv[1:]
	main(targets)