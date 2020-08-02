## Table of contents
* [Introduction](#Introduction)
* [Approach](#Approach)
* [The OSEM Part](#The-OSEM-Part)
* [To Log or not to Log](#To-Log-or-not-to-Log) 
* [Interpretaions](#Interpretations)
* [Conclusions](#Conclusions)
* [Repo Structure](#Repo-Structure)

## Introduction
The objective of this repo is to build a linear regression model to predict home sale prices based on census data from King County, WA.

## Approach
Out of the popular data science processes, such as CRISP-DM or KDD, we have selected the OSEMN framework. Cleaning and analyzing the data set according to the guidelines defined in the OSEMN framework.

In addition, we will build two models, one with data transformation and one without.  The purpose of this step is to see if data transformation will result in a better regression model.

Lastly, perform model validation by splitting dataset into train and test sets.

## The OSEM Part
In the first 4 processes of the OSEMN framework, the following procedures are performed:
* Corrrection to data type in the dataframe.
* Handling of null values in the dataset.
* Studay continuous variables data distribution.
* Examine correlation among columns.
* Ensure the regression assumptions are not violated.

## To Log or not to Log
Due to the diversity in the home prices in the data set, Model A (without log transformation) could not afford to include the outliers, in order not to violate the normality assumption.

![Normality Test with Outlier](/img/qqplot_outlier_A.png?raw=true)

![Normality Test without Outlier](/img/qqplot_wo_outlier_A.png?raw=true)

In Model B, we log transform the target variable and we ended up with a normal distribution for the home prices.
![Normality Test without Outlier](/img/log_trans.png?raw=true)








