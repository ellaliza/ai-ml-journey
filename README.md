# AI/ML Learning Journey 🚀

Hi! I'm currently on a journey to become an AI/ML Engineer. 
I have done some extensive research, taken a look at a couple of roadmaps, and other resources for getting started with Machine Learning and have decided to make my own roadmap. My journey is in two pases for now.


Phase One is about laying the foundations, making my way around and getting used to the essential python libraries. Since I am already very familiar with the basics of programming, I will skip that part. As I learn new things, I will come up with projects to practice what I have learnt. 

## 📚 Phase One – Foundations
- [x] Numpy
- [x] SQL
- [x] Matplotlib
- [x] Pandas
- [x] Scipy
- [x] Mathematical Foundations

## 📚 Phase Two – Core ML Models and Concepts
Focus: Learn, implement, and build intuition around essential machine learning models, starting with supervised learning and progressing to unsupervised and more advanced techniques.

- Supervised Learning
    * Regression and classification

        [ ] Linear Regression

        [ ] Polynomial Regression

        [ ] Logistic Regression

        [ ] Nearest Neighbour (KNN)

        [ ] Naive Bayes 

        [ ] Decision Trees

- Unsupervised Learning
    * Clustering 

    * Gaussian Mixtures

    * Dimensionality Reduction 



This repo documents my hands-on practice and mini-projects.
##

## 🔧 Projects
- [Student Performance Dashboard](./projects/student-performance-dashboard/) 

## 📖 Notes
- [Numpy Notes](./notes/numpy-notes.md)
- [SQL Snippets](./notes/sql-snippets.md)

## Experiments
| What I practice as I learn new things.
- [Medical Charges](./notebooks/experiments/medical_charges_example.ipynb)

## Machine Learning
| Any models I learn or practice
- Linear Models
    * [Medical Charges](./notebooks/machine_learning/linear_models/medical_charges_example.ipynb)
    * [Logistic Regression](./notebooks/machine_learning/linear_models/logistic_regression.ipynb)
    
## TinkerPad
| A notebook where I practice a new method, or anything new I learn.



# New Challenge : 100 Days of Machine Learning!
Today, 15th October 2025, I decided to end my season of inconsistency in this journey and took on a new challenge. 100 days of Machine Learning. This new challenge does not follow anyone's preset challenge rules or roadmap. I intend to continue with my roadmap, and the whole point of the challenge is to grow and learn something new and practical daily. 

## Week 1
- Focusing on basic ideas like linear models
    ### Day 1 - 15th October 2025
    - I did some exploratory data analysis on a dataset on medical charges.
    - I learnt some basic use of the plotly library, as well as seaborn.
    - I visualized the data and trends and understood the term "correlation coefficient"
    - I understood causation fallacy, which led me to also understand that as ML engineers, it is our responsibility to ensure that our models do not mislead users. Computers cannot do it all on their own, and that's why we do what we do.

    ### Day 2 - 16th October 2025
    - I trained a model using sklearn to predict charges based on age. 
    - I compared the LinearRegression model to the Schotastic Gradient Descent. The former had the minimum loss.    

    ### Day 3 - 18th October 2025
    - I trained a linear regression model using 2 feature.
    - I visualized the model using a 3d scatter plot in plotly express.
    - I also included a third feature in the model
    
    ### Day 4 - 20th October 2025
    - I included categorical columns in my model by converting to numbers
    - I practiced one hot encoding

    ### Day 5 - 21st October 2025
    - I learnt about feature scaling.
    - I learnt about creating test sets and training sets.
    - I learnt a general strategy to apply to any ML problem.
    
    ### Day 6 - 22nd October 2025
    - I learnt about logistic regression for classification and how it works.
    - I learnt how to do exploratory data analysis and visualization, and why it's important
    - I learnt that separating data into training, validation and test sets may use some criteria.

    ### Day 7 - 23rd October 2025
    - I learnt how to identify target and input columns.
    - I practiced converting yes/no columns to 1/0 columns
    - I practiced using a correlation table to visualize relationships.

    ### Day 8 - 24th October 2025
    - I learnt how to use pandas `nuniqe()`
    - I learnt what imputation actually was.
    - I practiced using `SimpleImputer()` class of sklearn.
    - I learnt why the entire dataset was used in fitting the imputer.

    ### Day 9 - 25th October 2025
    - I properly understood why scaling was necessary.
    - I practiced scaling with the `MinMaxScaler()`.
    - I learnt why the entire dataset was used in fitting the scaler too.

    ### Day 10 - 27th October 2025
    - I learnt different types of encoding and when they are useful.
    - Practiced the use of `OneHotEncoder()` class of sklearn.
    - I practiced saving inputs and targets to disk after the various transformations.

    ### Day 11 - 28th October 2025
    - Train a logistic regression model
    - Predicted targets for all the sets.
    - Did comparison to dumb models to compare accuracy using `sklearn.metrics.accuracy_score()`
    - Tested the model on new inputs and checked probability.