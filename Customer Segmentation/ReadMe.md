### RFM stand for:  
Recency: The freshness of the relationship between your brand and your customer; i.e. how recently customer last bought a product.  
Frequency: The measure of demand; how many times customer have purchased.  
Monetary value: View the monetary value or the proportional value of every selected group of customers compared to the rest.  

In RFM segmentation we calculate above three values(Recency, Frequency, Monetary value) per User.  
Based on no. of segments required we decide the no. of quantiles. Here i decided to go with quartiles because its easy to understand and give enough segments to cluster our users.  
Then We calculate r_quartile, f_quartile, m_quartile according to Recency, Frequency, Monetary values by comparing them with quartile values.  
Then We Find RMF score per user by combining r_quartile, f_quartile, m_quartile.  

RFM segmentation is very easy to understand and analyse rather than K-means.  
#### |SEGMENT|___________________|RMF SCORE|  
Best Customers:__________________111  
Loyal Customers:_________________*1*  
Big Spenders:____________________**1  
Almost Lost Customers:___________311  
Lost Customers:__________________411  
Lost Cheap Customers:____________444  

Here RMF score '111' means customer's Recency, Frequency and spending all falls in first Quartile and is very interpretable that, a very frequent cutomer who purchases much and had a recent purchase is Best Customer.  
We can Also set no. of quantiles according to segments we want our customers to classify in.  
As Data in RFM is 3 dimentinal, its easy to make a visual analysis, which is not possible with k-means if input data is of higher dimention because k-means doesn't work very well with higher dimentional data.  

The reason to went with RFM is, its cost-effective in acquiring important customer behavior analysis and is easy to quantify customer behavior, where customers and transactional data can be stored in an accessible electronic form. As such, decision makers can easily understand the application of RFM model. Secondly, RFM is very valuable in predicting response and can boost a company’s profits in a short term. Thirdly, it is very effective to model with RFM variables as the purchase behavior can be summarized by using a very small number of variables. Fourthly, RFM variables are gathered via an internal database containing customer-specific information regarding the transaction history and are not obtained through the aggregate level information in the demographic databases. Hence, RFM is more meaningful for targeting particular customers. Fifthly, RFM is a long-familiar method to measure the strength of customer relationship as RFM can effectively identify valuable customers.
