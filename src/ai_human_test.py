import os
import numpy as np
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt


def ai_human_test(outfile, num_games, data):
	# outfile = '../../codenames-ai-analysis/data/ai_human_data.csv'
	# num_games = 100
	# data = ["1", "2", "3"]

	#create data directory and add headings
	if not os.path.isdir('./data'):
		os.mkdir('./data/')
	with open("./data/ai_human_data.csv", 'a') as f:
	    f.write(",".join(['turn', 'assassin', 'intended correct', 'unintended correct', 
	    					'wrong', 'total intended', 'data', 'seed']) + "\n")

	#change to game directory to run simulations and collect data
	os.chdir("game")
	os.system('git checkout performance_testing')
	os.chdir("code")
   
	seeds = [str(i) for i in np.random.randint(2**31 - 1, size = (num_games))]
	#loop through each datasets and record performance
	for d in data:
		print('----- data={}/{}'.format(d, len(data)))
		for s in tqdm(seeds):
			cmd = 'python codenames.py -p 2 1 2 1 -m testing -d {} -s {} -o {}'.format(d, s, outfile)
			os.system(cmd)

	os.chdir("../../codenames-ai-analysis")

def ai_human_stats(datafile, outdir): #read in data, create plots
	# datafile = 'data/ai_human_(test_)data.csv'
	# outdir = 'figures'

	data = pd.read_csv(datafile)
	data['data'] = data['data'].str.split('.').str[0]
	data['true accuracy'] = data['intended correct']/data['total intended']
	data['total accuracy'] = (data['intended correct'] + data['unintended correct'])/data['total intended']
	complete_game = data[data['assassin'] == False]


	# generate statistics
	stats = pd.DataFrame(index = ['glove','word2vec','wup'])
	stats['Num Games'] = data.groupby('data')['turn'].count()
	stats['Avg Turn All'] = data.groupby('data')['turn'].mean()
	stats['Avg Turn Complete'] = complete_game.groupby('data')['turn'].mean()
	stats['Assassin'] = data.groupby('data')['assassin'].sum()
	stats['Avg True Accuracy '] = data.groupby('data')['true accuracy'].mean()
	stats['Avg Total Accuracy '] = data.groupby('data')['total accuracy'].mean()
	stats = stats.replace({np.nan:0})
	stats.to_csv(os.path.join(outdir, 'human_stats.csv'))


	# num assassin by dataset
	num_assassin = stats.iloc[:,[3]].plot.bar(rot = 0)
	num_assassin.bar_label(num_assassin.containers[0])
	num_assassin.set_ylim(0,80)	
	num_assassin.set(xlabel="Dataset", 
	                 ylabel="Num Assassin Triggered", 
	                 title = "Number of Assassins Triggered v. Dataset")
	plt.savefig(os.path.join(outdir, 'human_assassin.png'))


	# average turns taken
	turns = stats.transpose().iloc[1:3,].plot.bar(rot = 0)
	for container in turns.containers:
		turns.bar_label(container, fmt='%.2f')
	turns.set_ylim(0,10)
	turns.set(xlabel="Dataset", 
				ylabel="Avg Turns Per Game", 
				title = "Average Turns v. Dataset")
	plt.savefig(os.path.join(outdir, 'human_turns.png'))


	# accuracy
	acc = stats.transpose().iloc[4:,].plot.bar(rot = 0)
	for container in acc.containers:
		acc.bar_label(container, fmt='%.2f')
	acc.set_ylim(0,1)
	acc.set(xlabel="Dataset", 
			ylabel="Accuracy", 
			title = "Accuracy v. Dataset")
	plt.savefig(os.path.join(outdir, 'human_accuracy.png'))


	return None








