PROJECT NAME:-
Tone Detection/Sentiment Analysis

TABLE OF CONTENTS
1. PROJECT DETAILS 
2. BACKGROUND 
•	2.1. PROBLEM DEFINITION AND SOLUTION APPROACH
•	2.2. INPUT DATA
•	2.3. CREATION OF THE INITIAL DATASET
•	2.4. APPROACH EXPLORATORY DATA ANALYSIS
•	2.5. FEATURE ENGINEERING
•	2.6. PREDICTIVE MODELS
3. SAVING MODEL 
4. DEPLOYMENT USING FLASK













2.1	Problem definition and solution approach:
Problem Definition: - The organization wants to monitor customer feedback, on its product quality and service of the product based on customer feedback/tweets which are getting generated on daily basis. If any negative feedback comes it takes a lot of time to respond to that feedback because analyzing all reviews manually takes a lot of time to respond, monitor the customer feedback manually may cause the loss the customers and service and sales of the product because of delay in the action plan, for that we need to automate the task that can help quick action plan on customer feedback,
To automate the task we are going to build a model with ML technics for sentimental analysis by using advanced python language.

Solution Approach: - As per the problem, it comes under the sentimental analysis of customer opinion it analyses the feelings and emotions, urgency, even intentions, and polarity, It is used to detect positive or negative, or neutral sentiments in it, we have several techniques that train the model then we can detect the positive and negative in the sentiment, The below mentioned types sentimental analysis helps us to build a perfect model to analyze the customer.
1.	Fine-grained sentiment analysis 	
2.	Emotion detection 
3.	Aspect-based sentiment analysis 
4.	Multilingual sentiment analysis
Using natural language processing techniques, the machine learning model can sort unstructured text by emotion and opinion, which can detect customer feedback and gives us the solution for that which reduces the time and increase the service of a product.
The benefits of sentimental analysis:-
	Sentiment analysis could be used to sort thousands of customer support messages instantly by understanding words and phrases that contain negative and positive opinions.
	If any negative opinions or angry customer occurs in real-time, with help of a sentimental analysis model we can detect the customer points immediately and take proper action right away.
Methodology: - To perform the sentimental analysis we are required to collect the data from the desired sources. This data undergoes various steps of preprocessing which makes it machine sensible, then we are going to build a model using ML techniques.














2.2	INPUT DATA

	There are 992 rows & 6 columns in a dataset.
	5 columns having object type of data.
	1 column having a numerical value.
	There are 3605 null values present in the dataset.
	Null values present in columns wise are shown in the below table.


Column Name	Null values Count
Review	0
Liked	0
Unnamed: 2	705
Unnamed: 3	929
Unnamed: 4	980
Unnamed: 5	991

2.3. CREATION OF THE INITIAL DATASET.

	The reviews are distributed into 6 columns and are segregated into 1 column.
	The liked column data are divided into 5 columns segregated into 1 column and converted into an Integer value. 
	Special characters present in the reviews columns are removed.
Observation: - the restaurant dataset is cleaned.

The below-mentioned 10 Reviews are going to use the test, my model.
1.	The food was delicious….
2.	They serve Roast and Dose with your name on it which was surprisingly amazing and very unique.
3.	The Thali is amazing and at a pretty good price. Highly recommended.
4.	The food quality is very very bad had ordered some soup it was so terrible could not eat more than a spoonful. They need to change the chef at the earliest.
5.	Bad food quality, wastage of money, we can get better food in the other hotels.
Service was also not good.
6.	This is a no-frills restaurant, fairly clean, good ambiance, on the main road, and easy to access. We had their lunch buffet which was quite adequate and good value for the money.
7.	Food tastes great. Nice place to visit on a chilly winter night. Good ambiance too.
8.	The food was great. We ordered veg and non-veg dishes. Non-vegetarian was outstanding. Must surely have at least 1 meal in this restaurant.
9.	The cost is so high but the food is worst and you get is so chill and the taste is very bad......
10.	The food was horrible except for the dosa everything was old and rubber-like we asked for a replacement but were denied.

















2.4	Data Extraction through web

	The Data Extraction from the web was done using the below-mentioned Library.
a.	Request Module:-Using the request library, we can fetch the content from the URL given.
b.	BeautifulSoup Module: - beautiful soup library helps to parse it and fetch the details the way we want.
	The Dine-Out Website is used to fetch customer reviews.
	A total of 482 numbers of Reviews and ratings are extracted.
	The Ratings are converted to 0 & 1 (If the ratings 3 & Above are converted to 1, If less than 3 Converted to 0)
	The Extracted reviews are cleaned and added to the main data frame.
	In extracted reviews 363 reviews belong to 1 rating & 119 reviews belong to 0 ratings.

















2.5	EXPLORATORY DATA ANALYSIS

	Plotted the graph between reviews and liked columns.
 
	795 Reviews belong to 1 & 585 Reviews belong to 0.
	Majority of Reviews are belongs to 1.
	There are 5 Null values present in the Review Column.
	57% of reviews belong to 1 & 43% of reviews belong to 0.
Graph of Null Values:-
 
Observation: - There are 1469 rows present in my data set, and 855 Reviews belong to Liked (1) & 614 Reviews belong to not liked (0).
2.6	FEATURE ENGINEERING

	In feature engineering we have converted text reviews into numerical form for that we used the below-mentioned libraries. 

1.	NLTK – NLTK is a toolkit built for working with NLP in Python. It provides us with various text-processing libraries.
2.	RE - A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern.

	The below-mentioned steps are followed to clean the text.
1.	Reviewing each row and removing all unwanted characters.
2.	Converting each review into lowercase.
3.	Splitting each word from reviews.
4.	Creating an instance for Porter stemmer  and Lemmatizer.
5.	Downloading stop words from NLTK library.
6.	Removing NOT word from stop words.
7.	Removing stop words and stemming each word.
8.	Stemming is not proving the proper meaning of words to fix that I’m using Lemmatizer.
9.	Joining each word after removing stop words and lemmatizing each word.

	After cleaning the text convert the text into numerical values to apply the ML module.
1.	To convert the text to numerical I used the Keras Tokenizer & pad sequence module from the Keras library.
2.	Converting into a numerical value and converting into an array.

	Creating train and test datasets using the Sklearn library.
1.	Creating 80% of data to train the module & 20% of data to test the module.

Conclusion: - The dataset is ready to build an ML or DL module.
.






2.7	PREDICTIVE MODELS.

	Building an LSTM model with 516 neurons.
	Used Embedding layer because not to consider unwanted data that was added in padding sequence.
	Used Activation function as Softmax & Dense layer is 2 because the output is classified between 0 & 1.
	Predicted our model with 20 Epoch.
	The Train Accuracy is 0.9947 & Validation accuracy is 0.753.
	The Test accuracy is 0.768 & Test loss is 0.9134.
	Saved the model in the name of ‘sentimental_analysis_model’.
	Load the model using the load model in the Keras library.

Observation: - My model is kind of under-fitting due to fewer data.


