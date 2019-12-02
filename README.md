# NLP
NLP chatbot project: 
Chatbots (Chat-oriented Conversational Agent) are designed to handle full conversations, mimicking the unstructured flow of a human to human conversation. In this project, I implemented a chatbot using Sequence to Sequence (seq2seq) model and Word Embeddings. The detailed information for each implementation steps are specified in the following sections.

1.	Data Preprocessing for Chatbot
In this project, I used Microsoft BotBuilder Personality Chat Datasets, which includes three different personality chat (professional, friend, comics) datasets. With these datasets, I built my social chatbot and implement changing personality function. In this Data Preprocessing section, I implemented the following functions:

●	Download all three datasets on Google Colab virtual server
(https://github.com/Microsoft/BotBuilder-PersonalityChat/tree/master/CSharp/Datasets) The three following datasets (qna_chitchat_the_professional.tsv, qna_chitchat_the_friend.tsv, and qna_chitchat_the_comic.tsv) were downloaded on the Google Colab virtual server.
●	Preprocess data: Pre-processed the chatbot training data by integrating several text pre-processing techniques (tokenisation, removing numbers, converting to lowercase, removing stop words, stemming, etc.) 

2.	Model Implementation
I implemented two models, word embedding model and Sequence model. While the model is being trained, I displayed the Training Loss and the Number of Epochs after hyper-parameter tuning (size of vector for embeddings, learning rate, etc.)

Word Embeddings
First, I built the word embeddings model for my chatbot using word embedding (vector represents of words - such as word2vec-CBOW, word2vec-Skip gram, fastText) as input for seq2seq model

Sequence Modelling
Secondly, I built the Many-to-One (N to 1) Sequence model in order to train a chatbot. I trained three different individual sequence models (using three different personality datasets and those models were individually applied. My chatbot users were able to change the personality (trained model) of chatbot.
