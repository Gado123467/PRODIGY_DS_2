# PRODIGY_DS_2


# Titanic Dataset Visualization: 

## Overview

This project demonstrates how to create **bar charts** and **histograms** to visualize the distribution of variables in the Titanic dataset. The Titanic dataset contains passenger information such as age, gender, class, and survival status.

## Objectives

* Explore the Titanic dataset to understand passenger demographics
* Visualize categorical variables (e.g., gender, passenger class) using bar charts
* Visualize continuous variables (e.g., age, fare) using histograms
* Gain insights into survival patterns and population characteristics

## Dataset

The dataset includes the following key columns:

* `Survived`: Survival status (0 = No, 1 = Yes)
* `Pclass`: Passenger class (1, 2, 3)
* `Sex`: Gender (male, female)
* `Age`: Age in years
* `SibSp`: Number of siblings/spouses aboard
* `Parch`: Number of parents/children aboard
* `Fare`: Ticket fare

## Tools & Libraries
python

pandas – Dataset handling and submission file creation

numpy – Data manipulation and logical operations


## Use Cases

* Understanding passenger demographics
* Exploring survival patterns
* Conducting exploratory data analysis (EDA) for machine learning or statistical studies



## Goal

Understand the Titanic dataset structure

Implement a simple rule-based classification model

Generate a valid Kaggle submission file

Establish a baseline accuracy for future improvements

## Methodology

Load training and test datasets

Apply a simple rule:

Female → Survived (1)

Male → Not Survived (0)

Generate predictions for the test set

Create the gender_submission.csv file

## Results

The gender-based approach provides a strong baseline accuracy

Demonstrates the importance of feature selection

Serves as a reference point for more advanced model
