


CS6320 NATURAL LANGUAGE PROCESSING
FINAL PROJECT REPORT























Comparative Analysis of Twitter data using N-Gram Models

ABSTRACT
	Twitter is one of the most used social platform with plethora of information. Many surveys prove the usability and credence of the data present in twitter. But one of the main concerns in getting plausible information from twitter is the ratio of noise VS actual data. The noise is in the form of hashtags, slangs, colloquialisms and abbreviation, all of which are a result of the language mutation that occurred because of the Web 2.0 .These aren’t particularly noise as they do contain information. Hence, getting this data is of key importance. In this approach the proposed technique to handle this data is by using a dictionary-based approach. After cleaning the data, it is used as an input to the n-gram models. Unigram, bigram and tri-gram models are used to perform a comparative analysis of this data.


INTRODUCTION
	Social media has a lot of information to offer. Its anonymity provides a common ground for people to give their opinions in a safe environment. The data is obtained in a global scale such that people from every corner of the world contribute towards it, thus resulting in a very diverse outlook of the data that we are mining. But extensive use of net lingo and other colloquialisms tend to hide the relevant knowledge which results in them being considered as noise by the existing systems.

	In this project, I am extensively working on twitter data.The above stated problems are applicable in all aspects of social media. This problem takes a very special take in twitter because here the user is restricted as they are allowed to use a maximum of 280 characters including all whitespace characters. Thus the users tend to shorten the words in order to accommodate more words for example: “how are you” is abbreviated to “hru”.



	The focus of this project is to improve the quality of the raw data obtained from twitter. After performing certain cleaning operations on the raw data obtained, it can be use in any existing applications such as performing Sentiment Analysis or applying statistical modelling methods ,etc. The raw data can be separated into different types of noise data:
•	Hashtags, username, RT tags,hyperlinks :- These elements are associated more specifically to twitter and tweepy(api for obtaining twitter data).
•	Slangwords, abbreviations and colloquialisms: These elements are used by the users across all social media.

	The slangwords, abbreviations are handled using a dictionary-based approach. The slangwords’ dictionary is made up of 300 words (sample table:-Table 1(A)) and the abbreviation dictionary is made up of an approximate 2300 abbreviated words ( sample table:-Table 1(B)). 

	N-gram modelling is applied on this cleaned data. N-gram is a type of statistical modelling approach that has applications such as predicting the next word in a sentence or comparing DNA strands in bio-informatics. An N-gram of size one is called unigram, of size two is called bigram and so on. N-gram model can be trained on a certain input or corpus which acts as its vocabulary and this trained model can thus be tested to check its predictability.

 
Table 1(A): Sample of slang dictionary


 
Table 1(B): Sample of abbreviations dictionary

RELATED WORK
	Eleanor Clarka and Kenji Arakia's[1] discusses problems involved in automatically normalizing social media English. The paper describes an experiment which examines the efficacy of conventional spell checkers on casual English, and to what extent this could be improved with preprocessing with the given system. Results showed that average errors per sentence decreased
substantially, from roughly 15% to less than 5% with use of spell checker. Different spell checker has strengths and weaknesses with different types of errors.

	Md Shad Akhtar, Utpal Kumar Sikdar and Asif Ekbal[2] propose a hybrid approach in order to improve the quality of twitter data using machine learning and rule based approach. Their method develops an overall precision of 90.26% which is very impressive.

	Russell Beckley[3] proposes a WNUT based approach to solve this task. The proposed solution has three stages; substitution list, rule based components and sentence re-ranker. Amongst the different datasets on which the method was employed, an average of 65% precision was observed.





APPROACH
	The project is divided into two parts: The first half is collection of data , employing various cleaning methods, etc. The second half of the project is generating ngram models and checking for efficiency of the generated model.

Part A: Data Collection and Cleaning
	Data used in this project is basically mined from twitter. I have used python as my language of choice for programming .I have used tweepy, which is python’s package api to get tweets from twitter. In tweepy, the developer can mention the hashtag/s that they want to fetch and perform operations on it.  I have performed tests on various hashtags and the experimental section contains the details of the same. For every hashtag, I am getting the first 50 tweets ordered by time. These tweets are divided into two parts: first 35 tweets are for training the model and the 15 tweets are used for testing the data. All of these tweets go through various stages of cleaning as mentioned in Figure(1).

	The data is filtered and only alphanumeric characters are processed further. Then all the hashtags, hyperlinks and stopwords are handled. The hashtag words are kept , but the pound sign is removed .For instance ’#machinelearning’ will be considered as ‘machinelearning’ after this stage. Stop words are unnecessary and thus a dictionary is used to compare the generic stopwords and they are removed. We have two main dictionaries to check for the biggest source of noise in the data obtained from social media: Slang words and Abbreviations. Both of these type of data is handled by finding the words in the dictionary and replacing them with the appropriate replacement. There can be multiple occurrences for the same words in the dictionary and hence they are ordered according to their most frequent usage. The data cleaning stage ends here. The above-mentioned steps are common for both, the training and testing data.

Part B:  N-gram model generation and testing
	After the data is cleaned, the ngram models are generated using the training data. The first 35 tweets are considered as the corpus and the rest of the 15 tweets are tested on this corpus. There are three models developed: Unigram, Bigram and Trigram models. The experimental section shows the comparison when the model was tested on various hashtags.


 
Figure(1): Steps in data cleaning

EXPERIMENTAL SECTION
	This section explains the stages through which the data goes through and the final output percentages after testing the data on the models. Table(2)  explains the different probabilities for the data on the three models developed. The mentioned probability are the average on testing the model for 15 tweets per hashtag.

	The observed output probabilities clearly seem to predict the following: the unigram probability is always more than the other two. This output value is after smoothing operations are performed on the data. And thus, the size of vocabulary and the sparseness of the occurrences of the words might be the reason why the probabilities in bigrams and trigrams are so low.









 
TABLE(2): PROBABILITY DISTRIBUTION FOR DIFFERENT HASHTAGS


FUTURE SCOPE & CONCLUSION
	The solution proposed and developed in the project is just a first step towards normalization of data. By including various machine learning models and feedback loops, there can be an extensive list of words in the dictionary. Ngram models can also be improved by collecting more tweets per hashtag and combining tweets from similar hashtags. Other smoothing techniques can also be implemented and thus using them will result in better output.

REFERENCES
[1] Eleanor Clark, Kenji Araki, 2011, Text Normalization in Social Media: Progress, Problems and
Applications for a Pre-Processing System of Casual English
[2] Md Shad Akhtar, Utpal Kumar Sikdar and Asif Ekbal, Hybrid Approach for Text Normalization in Twitter
[3]Russell Beckley, Bekli: A Simple Approach to Twitter Text Normalization
