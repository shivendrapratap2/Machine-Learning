## Affinity Analysis process overview
#### Problem Statement
Given an e-commerce dataset where each record is a combination of some user 'u' & some item 'i' & the task is to predict if user 'u' will buy item 'i' or not.

#### Data Provided
data provided was a cleaned data with unknown attributes. Data Contains date columns as well and some of the features were already scaled.
[Readme1](link)

#### Data Pre-processing
To Explorer and Analyse data, converted it into pandas DataFrame and after analysing the columns converted them into proper data type ex. Integer, float, datetime.
[Readme1](link)

### Exploratory Data Analysis
### Imbalanced Class problem
Firstly decided to find the distribution of class labels and found around 76% labels were ‘0’  and only 24% records were labelled as ‘1’. A Model can achieve 76% accuracy ny just predicting ‘0’ for all records. To handle imbalance class problem we can do Up-sampling of minority classes and Down-sampling of Majority classes using sklearn’s resample module. But I decided to choose confusion matrix as the performance measure instead of accuracy.  
[Readme1](link)

#### Correlation and Multi-collinearity Check
Checked the correlation among numerical attributes and found attribute F-19 and F-20  were correlated with F-17 and F-18  respectively with +ve value of .68. In VIF test for multi-collinearity, attributes F19 and F20 were highly multi-correlated, so decided to drop them from dataset.
[Readme1](link)

