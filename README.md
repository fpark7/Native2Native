# ![Native2Native](https://github.com/fpark7/Native2Native/blob/master/assets/logo_70.png)
## Native2Native
<br><i>"A Voice and Text Recognition System Built to Specifically for Non-Native Speakers"</i><br>

### About
Our hackathon project for Hack.UVA 2018. [According to the US Census](https://www.census.gov/hhes/socdemo/language/data/acs/PAA_2005_AbilityandEarnings.pdf), there is a high correlation between English speaking ability and employment rate, as well as self-confidence. This clearly puts immigrants and non-native speakers at a disadvantage in the United States. [Image from US Census](https://www.census.gov/hhes/socdemo/language/data/acs/PAA_2005_AbilityandEarnings.pdf)

<a href="url"><img src="https://github.com/fpark7/Native2Native/blob/master/assets/graph.png" align="middle" width=60% ></a>
<br>

Current translating applications are very flawed. First of all, syntax and structure between East-Asian languages and Western languages are completely flipped, making translation a difficult task. Many words from other languages also do not have a direct translation in the English language (and vice versa). [Image from here](http://nojeokhill.koreanconsulting.com/2014/02/rethinking-the-korean-localization-process.html)

<a href="url"><img src="https://github.com/fpark7/Native2Native/blob/master/assets/translate.png" align="middle" width=60% ></a>
<br>

However, we have noticed that non-native English speakers know what they want to say; they're just unable to articulate it well.
Native2Native is a Natural Language Processor that takes in a "difficult-to-understand" English sentence by a non-native speaker and completes it using Deep Learning, striving to be the "Native" voice for them. (The name "Native2Native" also comes from the Seq2Seq Recurrent Neural Network model used for our application)

### Purpose/Vision
Instead of focusing/training Voice-Recognition and Language-Recognition systems solely on eloquent English speech, we should also focus on dedicating them to the people who need these systems the most. In addition, non-native speakers are more likely to learn from corrections to their own English rather than translations of their own native languages. We hope the Native2Native will be a tool to equalize and empower immigrants by offering them a new voice and method to improve use of the English language. 

Our vision is to generalize our technology and see more Voice-Recognition Models and Language-Translation Models train on data from non-natives rather than native speakers for all languages. We also hope to see more Natural Language Processing (NLP) research focus towards "hard-to-understand" phrases rather than perfect English.

### Algorithm
Our naive model trains on "non-native" sentences generated using SpaCy. SpaCy is a power natural language processing library. By labeling linguistic features, tagging parts of speech, and tracing dependencies, we were able to emulate a more clever training data set for our neural network. This dataset includes proper sentences that were modified by removing stop-words (common, small words) and swapping nouns with neighboring adjectives or descriptive phrases. In the future, we hope to use real world data and have more time to train our models!

A [Seq2Seq Recurrent Neural Network](https://arxiv.org/pdf/1409.3215.pdf) is used to train on these "non-native/incomplete" sentences and maps them to "complete" sentences. The model was trained using an [AWS](https://aws.amazon.com/) EC2 P2 instance equipped with a [NVIDIA Tesla K80 GPU](https://www.nvidia.com/en-us/data-center/tesla-k80/). [Image from here](https://google.github.io/seq2seq/)

![Translation Model](https://3.bp.blogspot.com/-3Pbj_dvt0Vo/V-qe-Nl6P5I/AAAAAAAABQc/z0_6WtVWtvARtMk0i9_AtLeyyGyV6AI4wCLcB/s1600/nmt-model-fast.gif)
<br>
Our neural network is implemented with [Pytorch](http://pytorch.org/) and deployed using the [SAP Cloud Platform](https://cloudplatform.sap.com/index.html).

## Developers
Fengyang Zhang <br>
Felix Park <br>
Yutong Wang <br>
Jiten Bhatt <br>




