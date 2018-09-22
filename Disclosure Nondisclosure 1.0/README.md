# Disclosure OR Non-disclosure?

NLP Project for Classifying Disclosure and Non-Disclosure

### Data Overview

* 5000 private content and 5000 public content are being used.
* Post/Content are stored one per file with a naming convention `00000_CATE-GORY.txt` to `04999_CATE-GORY.txt` 
* Posts that contains at least 1000 characters in it are crawled.
* Data I picked as **Medical/Private** content - 
	* Abuse Support 
	* Teen Pregnancy Concerns 
	* Cancer 
	* Divorce-Breakups 
	* Menopause 
	* Stress 
	* Teen-Depression 
	* Depression 
	* Borderline Personality Disorder 
	* Step Parenting 
	* Anger Management 
	* Single Parenting 
	* Schizophrenia 

* Data I picked as **Article/Public** content -
	* SimpleWiki
	* EnWikiNews
 
### Data Crawler

* I used `wikiextractor` to collect data from SimpleWiki and EnWikiNews then used a custom Python script to save each article as separate text file. Those can been seen inside `Data/Disclose_Nondisclose/public`
* I made a new crawler using Python to pullout user's post from http://www.medhelp.org/ and saved each post as separate text file. Those can be seen inside `Data/Disclose_Nondisclose/private`

### Data Usage

* 4000 of Private content/file/post and 4000 of Public content/file/article (total 8000) have been used to **Train** the Convolutional Neural Network.
* 1000 of Private content/file/post and 1000 of Public content/file/article (total 2000) have been used to **Test** the Convolutional Neural Network.

### Final CNN Model

* First layer is Word Embedding layer to learn the word embeddings.
* Second layer is the Convolution Layer with 32 filters with each filter of size 8
* Third layer is a Maxpooling Layer to reduce the feature maps in half.
* Then the Flatten Layer to prepare for the next Fully Connected Layer
* Fifth layer is a Fully Connected Layer with 10 neurons
* Final or Output layer is a Single Neuron Layer with `sigmoid` as activation function.

### Model Evaluation

* Model was evaluated using the **Test** dataset that was totally unseen to the Model while training.
* So far the model shows **98.7% accuracy**
* Also, I made a **Predict** function to test the learned model using custom content by a text file. 

### Considering

* Diagnosis of **Overfitting**. Though, I don't think its Overfitted now because the accuracy metrics is based on the Test data which is unseen to the Model while training. Data are highly biased, so this result was supposed to happen.
* Using LSTM for sequence classification, Dropout for regularization. 
