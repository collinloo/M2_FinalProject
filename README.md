## Table of contents
* [Repo Structure](#Repo-Structure)
* [How to Run the Codes](#How-to-Run-the-Codes)
* [Introduction](#Introduction)
* [Approach](#Approach)
* [The OSEM Part](#The-OSEM-Part)
* [To Log or not to Log](#To-Log-or-not-to-Log) 
* [Interpretaions](#Interpretations)
* [Conclusions](#Conclusions)

## Repo Structure
* Root of the repo contains the main jupyter notebook and a python file of my fuctions
* A PDF file delivers the presentation of this project
* img folder holds all the images for the repo README.md
* csv_files folder house the data source and mapping of cities to zip code file.

## How to Run the Codes
<ul>
    <li>Use git clone to create a local repo.  URL is: https://github.com/collinloo/M2_FinalProject.git</li>
    <li>Required Libraries:
        <ul>
            <li>pandas</li>
            <li>numpy</li>
            <li>matplotlib.pyplot</li>
            <li>seaborn</li>
            <li>statsmodels</li>
            <li>sklearn</li>
            <li>myFunc.py</li>
        </ul>
    </li>
<ul>

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

![](/img/qqplot_outlier_A.png?raw=true)

![](/img/qqplot_wo_outlier_A.png?raw=true)

In Model B, we log transform the target variable and we ended up with a normal distribution for the home prices.  As a result, we are able to work with a large sample size.
![](/img/log_trans.png?raw=true)

## Interpretations
With the help of log transformation, Model B produces a higher $R^{2}$ than Model A, 0.705 vs A 0.685.  Out of the 12 predictors, the following five rank the top:
* City (zipcode)
* Grade
* Waterfront
* floors
* Age (yr_built)

Take the independent variable City for instance, the model reports that Medina, WA has a coefficent of 1.2919.  What does that mean?  Since we log transform the dependent variable price, the interpretation is not as straight forward.  To produce a meaningful explanation, we will need to reverse the log transformation.  In short, after the computation, it translates to 263.97% (np.exp(1.2919)-1)x100).  In other words, houses in Medina generally cost about 263.97% more than the houses in Aubrun, our reference dummy variable.

![](/img/cities_ranked.png?raw=true)

## Conclusions
All the assumptions for a regression model have been checked and verified.  Therefore, we are quite confident with the 70% predicting power of the model.  Futhermore the model performs well with the train and test data sets, signaling that it should be adequate to predict new data.

One caveat is that the model will not perform well for predicting houses over 2.0 million dollars, because we did not account for such variation in our model.  Perhaps, a separate model tailored to predicting expensive houses might be warranted.







