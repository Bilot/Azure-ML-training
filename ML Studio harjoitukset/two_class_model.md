---
Date: "2019-09-18"
Step: 'Model training'
Description: Modeling & evaluation exercise, using the diabetes data.
---

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe28kRsvMfHCz-rQz5oZgtVJhks1S6_W5W0WRcudlJf3_WVS5J" width="150" style="float:right;"/>

# Two-class classification
<br>

## 1. Import Data

Load saved Dataset for diabetes. <br />
This can be found under the *Saved Datasets* section in the operator menu.

## 2. Split Data

<p>Before doing any further manipulations to the data, we need
to split it to training and testing parts. This is done to be able
to evaluate the effect of the manipulations.</p>

<p>To achive this, add a <b>Split Data</b> operator, where you need to specify the split ratio. By default, <i>Stratified split</i> is set to false, but it is good practice to set this to true to make sure the 
samples are representative.</p>

## 3. Clean Missing Data

<p>Next, add an operator to impute (replace) missing values: 
<b>Clean Missing Data</b>. This operator offers several 
alternative methods that can be used for missing value replacement.
It is recommended to compare how the imputation affects any modeling 
results.</p>

## 4. Train model

<p> Add a <b>Train Model</b> operator and a modeling operator
for two-class classification, for example
<b>Two-Class Bayes Point Machine</b>, which is connected to the
<b>Train Model</b> operator. Also connect the <b>Clean Missing Data</b>
operator. </p>

<p> Next, connect the <b>Train Model</b> operator to a 
<b>Score Model</b> operator, which also needs input from the
<b>Clean Missing Data</b> operator. </p>

<p>Finally, connect the <b>Score Model</b> operator, which outputs
the date with model predictions added, to a <b>Evaluate Model</b>
operator. Run and see how the model performs on the training data.</p>

## 5. Evaluate model
<p>To see how the model (given the data imputation) performs on the 
testing data, one first needs to <b>Apply Transformation</b> to the data
using the transformation outputted by the <b>Clean Missing Data</b> 
operator.</p>

<p>Connect the result to a new <b>Score Model</b> operator, along 
with the trained model and finally connect the output to the
<b>Evaluate Model</b> operator. See how the two results differ.</p>

<p>As this is a classification problem, the ROC-curve provides a good
method for model comparison (below image from www.wikipedia.org):</p>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Roccurves.png/440px-Roccurves.png" width="300"/>