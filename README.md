# Project: StackOverflow Data Analytics

## DESCRIPTION - 
Package contains pythonic implementation for performing StackOverflow Data analysis. The aim is to be able to recommend users to a particular question based on Random Forest classifier and K-means clustering. In order to perform analysis, the UCI's StackOverflow dataset was used. However, in the available form it was insufficient and hence needed some feature engineering to be done. Using Stack Exchange DataExplorer website and API we were able to build features as Question vector and User vector.


## INSTALLATION - 
Requirements
1. Python 2.7
2. scipy
3. numpy
4. pandas
5. nltk
6. sklearn
7. requests

In order to install the above packages, run the following command on the terminal :
sudo pip install scipy numpy pandas nltk sklearn requests

## EXECUTION - 
Data Extraction
UCI StackOverflow Data was retrieved from https://www.ics.uci.edu/~duboisc/stackoverflow/
However, it was found to be incomplete. It consists of features - unique question id, Questioner Id, Answerer Id, Tags, Answer score.
However, in order to build the model, these features weren't enough.

Moreover, the random forest classifier needed Question Vector for which we needed the body of the question. Hence, using the UCI Dataset as "Base data" we queried StackExchange API to perform Feature Engineering.

Accessing StackExchange API
Create an application on StackOverflow, register the app. For more info - https://api.stackexchange.com/docs

Note - For ease of use, our code has API-key hardcoded (for added security we could encrypt it )

1. Question Vector
a. Find unique occurrences of Questions
b. Based on the unique Question identifiers, get the body of the question using StackOverflow API key
c. Given the question text, we cleaned the HTML and extracted features like Readability score, external link count, code count, etc
d. Similarly, for random forest classifier training, we used API to identify whether the questions have been unanswered or not and segregated them accordingly.
Command
python extract.py
python unanswerQ.py

2. User Vector
For building the user vector, we used the API to provide information about users.
First, we had to find the unique users in the StackOverflow UCI dataset and query the API to get user features like reputation, answer count, badge count, etc.
Command
python userExt.py

3. Cleaning
Using python libraries - pyreadability and nltk, we performed 
a. Remove HTML tags from Question body
b. Calculate readability score
c. Determine the number of code fragments
d. Find the number of external links
e. Find the word count of the question

Command 
python clean.py

4. K-means Clustering
In order to cluster the UCI dataset based on similar questions, we used the question tags (e.g. HTML, CSS, java, python) as a parameter.
Command
python Recommender.py

5. RandomForest Classifier
It trains the classifier using scikit-learn library and tests whether it can correctly classify an out of sample data. We performed cross-validation and evaluated the classifier's accuracy using F1-score.
Command
python Classifier.py
