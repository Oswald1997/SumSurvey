# SumSurvey: An Abstractive Dataset of Scientific Survey Papers for Long Document Summarization

This repository contains dataset and code for the paper 'SumSurvey: An Abstractive Dataset of Scientific Survey Papers for Long Document Summarization', which has been accepted by Findings of ACL 2024.

## Dataset

Please download the complete dataset from [here](https://drive.google.com/drive/folders/1Bhm15N3FQoq3_JtY8Q6HmFTNS74cCmdn?usp=sharing). There are six files in total:

* train.source  
* train.target  
* val.source  
* val.target  
* test.source  
* test.target

Each line contains the full text of a paper or its corresponding abstract.

## Code

Please run `main.py` to evaluate intrinsic characteristics of datasets. Four indicators will be calculated:

* **Coverage** measures the percentage of words in a summary that are part of an extractive fragment from the document.  
* **Density** is similar to coverage, where the sum of fragment lengths is changed to the sum of squares of lengths.  
* **Redundancy** is used to evaluate whether sentences in a summary are similar to each other.  
* **Uniformity** measures the degree to which salient information in a summary is evenly distributed throughout the document.

