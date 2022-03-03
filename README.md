# codenames-ai-analysis

## Introduction
This project includes the experiments and analysis on the performance of Codenames AI, a system capable of replacing human efforts in the game Codenames.
* To play the game, please visit https://github.com/XueweiYan/codenames-game-ai
* For more details on the project, please visit https://xueweiyan.github.io/codenames-ai-website/


## Instructions
* Download the datasets from the below link and store them on the same level as this repository in a file named "AI_dataset":
  * https://drive.google.com/drive/folders/1FqEHYL_uTQDQ_MFw8T4gdD4VHaa2r0jv?usp=sharing
* Clone the game repo and place it on the same level as this repository:
  * https://github.com/XueweiYan/codenames-game-ai
* Resulting set up should look like this:

![alt text](https://github.com/YongqingLi14/codenames-ai-analysis/blob/main/file_organization.png)


## Running the Repository
* Run the following docker image inside a container: 
  * yongqingli/codenames_ai

* To test the pipeline of the project: 
  * `python3 run.py test`
 
* To view full results (total time will take ~15 hours): 
  * `python3 run.py all`
  
* To revert the repo back to its original state: 
  * `python3 run.py clean`
  
* Results will be availale in Report.ipynb and Report.html


## Datasets
We put 3 datasets to the test in this experiment:
* glove: 
  * pretrained word embeddings from Wikipedia
  * cosine similarity
* word2vec
  * word embeddings trained from the English Simple Wiki using the gensim word2vec model
  * cosine similarity
* wup
  * word embeddings from the WordNet dataset
  * Wu-Palmer(wup) similiarity


## Testing Metrics
* Average turns taken to finish the game
* Number of assassins triggered
* Accuracy in correctly guessing the intended words
