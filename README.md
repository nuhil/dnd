# Code and resource repository for the following research work -
"Identifying Privacy Disclosures in Natural Language Text using Linguistically-motivated Artificial Neural Networks"

### File and Folder Structure
* Folder `api-server` - The API server built on `Flask web framework` for serving classification prediction to the client (Chrome Browser Extenion). You have to deploy this API server where you will basically use the trained and saved machine learning model (e.g. your pickled model). This API server is minimally developed to handle only `POST` request from the browser extension and return the classification decision in string format.
* Folder `chrome-extension` - This folder contains all the source code of the full chrome extension (client) that can be installed into a Chrome Web Browser. To install this extension you have to drag and drop this folder in the settings page of the browser. Note: You have to update the server URL in the `content.js` file. This should be the URL where you deployed the `api-server` eventually.
* Folders `Disclosure Nondisclosure x.x` - All the research work notebooks along with their associated data. Old versioned folder means early stage of the work. Latest version of the work could be found inside the folder named `4.0` including Jupyter notebooks and associated dataset.

### Data Overview
* Every version of the work has its own dataset inside each folder. Latest version of the work that is named as `4.0` contains disclosure and non-disclosure dataset with folder named `disclosure` and `non_disclosure` under the `data` folder.
* 5000 disclosure sentences and 5000 non-disclosure sentences are used.
* Sentences are stored one per file with a naming convention `00000_xx.txt` to `04999_xx.txt`
* Data sources - 
    * Medhelp Forum Posts
    * Amazon Product Reviews
    * Amazon Food Reviews
    * Hotel Reviews
    * Place of Interest Reviews
    * Psychriatic Forum Posts
    * Twitter Posts
    * Stack Overflow Questions
 
* Data Preparation -
We collected 5000 disclosure sentences and 5000 non-disclosure sentences from the posts of above sources. For preparing the training dataset we used rule based approach (mentioned in the paper). We also have a relatively small dataset with ground truth that is annotated by human.

* Additional Dataset - 
    * For a baseline evaluation and evaluating the generalizability of the proposed framework, we utilized a dataset made available by Schrading et al. and Choudhury et al. That dataset can be [found here](http://nicschrading.com/data/).

### Final Multichannel CNN Model
* First layer is Word Embedding layer to learn the word embeddings.
* Second layer is the Convolution Layer with 32 filters.
* Third layer is dropout layer.
* Fourth layer is a Maxpooling Layer to reduce the feature maps in half.
* Then the Flatten Layer to prepare for the next concatenation Layer.
* Sixth layer is a Fully Connected Layer with 10 neurons.
* Final or Output layer is a Single Neuron Layer with sigmoid as activation function.

### Model Evaluation
We evaluated our approach in a binary classification task with 93% accuracy on our own labeled dataset, and 86% on a dataset of ground truth.

