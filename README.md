# ![Native2Native](https://github.com/fpark7/Native2Native/assets/logo.png)

## Native2Native

### About
Our hackathon project for Hack.UVA 2018. According to the US Census, there is a high correlation between English speaking ability and employment rate, as well as self confidence. This clearly puts immigrants and non-native speakers at a disadvantage in the United States. 

Current translating applications are very flawed. First of all, syntax and structure between East-Asian languages and Western languages are completely flipped, making translation a difficult task. Many words from other languages also do not have a direct translation in the English language (and vice versa). 

However, we have noticed that non-native English speakers know what they want to say, they're just unable to articulate it well.
Native2Native is a Natural Language Processor that takes in a broken English sentence by a non-native speaker and completes it using Deep Learning... striving to be the "Native" voice for them. (The name "Native2Native" also comes from the Seq2Seq Recurrent Neural Network model used for our application)

### Purpose/Vision
Instead of focusing/training Voice-Recognition and Language-Recognition system on eloquent English speakers, we should focus on dedicating them to the people who need these systems the most. In addition, non-native speakers are more likely to learn from corrections to their own English rather than translations of their own native languages. We hope the Native2Native will be a tool to equalize and empower immigrants by offering them a new voice and method to the English language. 

Our vision is to generalize our technology and see more Voice-Recognition Models and Language-Translation Models train on data from non-natives rather than native speakers for all languages.

### Algorithm
Our naive model trains on "non-native" sentences generated using SpaCy. SpaCy is a power natural language processing library. By labeling linguistic features, tagging parts of speech, and tracing dependencies, we were able to emulate a more clever training data set for our neural network. In the future, we hope to use real world data and have more time to train our models!

A Seq2Seq Recurrent Neural Network is used to train on these "non-native-incomplete" sentences and maps them to "complete" sentences. 
<br>
Our neural network is implemented with TensorFlow and deployed on an EC2 instance in AWS.

## Developers
Fengyang Zhang <br>
Felix Park <br>
Zutong Wang <br>
Jiten Bhatt <br>




