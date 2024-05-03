This document is a guideline for the project GenZ.
The project is about to do an application of Machine Learning/Deep Learning models into a real life problem; although the dataset is limited in terms of volume of data, it was possible to do interesting things with it. In this case, let’s imagine that you are in HR department and you are struggling with staff turnover, sounds familiar? This app is an approach for a model to identify potential characteristics from GenZ, in order to identify if a person will work within a company beyond 3 years or less.
The columns of the dataset are:
'Your Current Country.', 'Your Current Zip Code / Pin Code',
       'Your Gender',
       'Which of the below factors influence the most about your career aspirations ?',
       'Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.',
       'How likely is that you will work for one employer for 3 years or more ?',
       'Would you work for a company whose mission is not clearly defined and publicly posted.',
       'How likely would you work for a company whose mission is misaligned with their public actions or even their product ?',
       'How likely would you work for a company whose mission is not bringing social impact ?',
       'What is the most preferred working environment for you.',
       'Which of the below Employers would you work with.',
       'Which type of learning environment that you are most likely to work in ?',
       'Which of the below careers looks close to your Aspirational job ?',
       'What type of Manager would you work without looking into your watch ?',
       'Which of the following setup you would like to work ?',

The question target/goal is the one 'How likely is that you will work for one employer for 3 years or more ?
It was taken off couple questions like Country (majority is from India+95%; the rest was used as new data to evaluate the model accuracy), education related questions, except Which type of learning environment that you are most likely to work in ?, zip code (Assuming it does not affect the geographical area), the rest of them were considered for the study (11).
In order to run App.py (Dash app); it has to be considered that requirements.txt file was already run with pip install, due the libraries required to run the logic.py file in here, is where all data transformation & analysis happen, considering Decision Tree, KNN, Random Forest, CNN, models with their proper bagging method applied.
Step 1.- pip install -r requirements.txt
Step 2.- python3 app.py 
You will notice all the analysis and the report will come out with graphs, this means that everything went correctly.
The Github Repo Image is a link to the Github repo
https://github.com/AlfredoSuarez/ucamp_genz_aitest
Also:
You will see this graph as accuracy comparison, and the evaluation of Random Forest as base model, due the high accuracy among the others.

Extra  & refference material:
AWS Container:

Colab: https://colab.research.google.com/drive/1t4OYVPp2sAxgQDPUXai0GckIfhmRNpXC?usp=sharing 
Kaggle dataset: https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fwww.kaggle.com%2Fdatasets%2Fkulturehire%2Funderstanding-career-aspirations-of-genz 
