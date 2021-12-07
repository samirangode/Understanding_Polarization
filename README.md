# Intro_to_Deep_Learning_Project

## Understanding Political Polarisation using NLP

This repository is for hosting the code for the project 'Understanding Political Polarisation using NLP' 
as a part of 11785-Intro to Deep Learning course at Carnegie Mellon University.


The structure explaining different branches of the report are:

```
web-scraping-dev 
```

```senators.py```  - contains beautiful soup library that fetches all the senators as well as represntatives 
along with their label R or D from each Congress page in the range 104 to 117.

```data-congress.py``` - webscraping for fetching the content in each politicians wikipedia page along with
their personal details such as name, party, education, political life etc.


```
Transformers-Pipeline
```

```TRANSFORMERS_IDL.ipynb```  - The enitre pipeline for running different transformers model and getting model embeddings.


```
Preliminary-tests
```

```Prelimnary_tests_IDL_project.ipynb```  - Pipeline for Wor2Vec and KNN 

```Roberta_Large.ipynb``` - Pipeline for RoBERTa transformer model and SVC

```Updated_Doc2Vec_tests_IDL_project.ipynb``` - Pipeline for Doc2Vec  



### Project Pipeline

* ```senators.py``` is the first file that executes to generate a .csv for all wikipedia links and labels

* ```data-congress.py``` will dump required text content in each page to JSON file by reading the csv geneated by  ```senators.py```

* ```Prelimnary_tests_IDL_project.ipynb``` helps in getting initial baseline/preliminary test results using Word2Vec

* ```Roberta_Large.ipynb```,```Updated_Doc2Vec_tests_IDL_project.ipynb``` and ```TRANSFORMERS_IDL.ipynb```  are various other experiment pipline with different models  



