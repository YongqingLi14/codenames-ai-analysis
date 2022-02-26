import os
import numpy as np
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt


def conservative_test(outfile, num_games, algorithms, data, cb_range, ci_range):
	# num_games = 100
	# algorithms = ['1', '2'] 
	# outfile = '../../data/optimal_conservative_data.csv'
	# data = 33
	# cb_range = [0.8, 1.0, 0.02]
	# ci_range = [0.0, 0.01, 0.001]

	#create data directory and add headings
	if not os.path.isdir('./data'):
		os.mkdir('./data')
	with open('./data/optimal_conservative_data.csv', 'w') as f:
	    f.write(",".join(['turn', 'assassin', 'algorithm', 'data', 'seed', 'cb', 'ci']) + "\n")

	#change to game directory to run simulations and collect data
	os.chdir("game/code")

	data = [str(i) for i in range(1, 2)] 
	seeds = [str(i) for i in np.random.randint(2**31 - 1, size = (num_games))]
	#loop through all combinations between algorithm, dataset, and seed
	for cb in np.arange(cb_range[0], cb_range[1], cb_range[2]):
		for ci in np.arange(ci_range[0], ci_range[1], ci_range[2]):
			print('----- cb={}, ci={}'.format(cb, ci))
			for s in tqdm(seeds):
				cmd = 'python codenames.py -p 2 2 2 2 -m pure_ai -a {} -d {} -cb {} -ci {} -s {} -o {}'.format(1, 1, cb, ci, s, outfile)
				os.system(cmd)
	os.chdir("../../codenames-ai-analysis")


def conservative_stats(datafile, outdir): #read in data, create plots
	# datafile = 'data/optimal_conservative_data.csv'
	# outdir =''

	df = pd.read_csv(datafile)
	df = df.groupby(['cb', 'ci']).mean().reset_index()

	# mean number of turns taken
	x = df['cb'].values.reshape(10,10)
	y = df['ci'].values.reshape(10,10)
	z = df['turn'].values.reshape(10,10)

	fig = plt.figure(figsize = (10,10))
	ax = plt.axes(projection='3d')
	ax.grid()
	ax.xaxis.set_major_locator(plt.MultipleLocator(0.02))
	ax.yaxis.set_major_locator(plt.MultipleLocator(0.001))
	ax.plot_surface(x, y, z, cmap ='viridis')
	ax.set_title('Hyperparameter Tuning for Conservative Index (Num Turns)', size=14)

	# Set axes label and save figure
	ax.set_xlabel('mean conservative base', labelpad=10)
	ax.set_ylabel('mean conservative increment', labelpad=10)
	ax.set_zlabel('mean number of turns taken', labelpad=10)
	plt.savefig(os.path.join(outdir, 'conservative_num_turns.png'))


	# mean assassin word triggered
	x = df['cb'].values.reshape(10,10)
	y = df['ci'].values.reshape(10,10)
	z = df['assassin'].values.reshape(10,10)

	fig = plt.figure(figsize = (10,10))
	ax = plt.axes(projection='3d')
	ax.grid()
	ax.xaxis.set_major_locator(plt.MultipleLocator(0.02))
	ax.yaxis.set_major_locator(plt.MultipleLocator(0.001))

	ax.plot_surface(x, y, z, cmap ='viridis')
	ax.set_title('Hyperparameter Tuning for Conservative Index (Assassin Word)', size=14)

	# Set axes label and save figure
	ax.set_xlabel('mean conservative base', labelpad=10)
	ax.set_ylabel('mean conservative increment', labelpad=10)
	ax.set_zlabel('mean assassin word triggered', labelpad=10)
	plt.savefig(os.path.join(outdir, 'conservative_num_assassin.png'))

	return None


