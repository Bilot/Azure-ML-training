---
Date: "2019-09-18"
Step: 'Model tuning'
Description: Model train & optimisation exercise, using the Steel Plates data.
---
  
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe28kRsvMfHCz-rQz5oZgtVJhks1S6_W5W0WRcudlJf3_WVS5J" width="150" style="float:right;"/>

# Model Optimisation
  
## 1. Import Data

Load saved Dataset for steel plates. <br />
This can be found under the *Saved Datasets* section in the operator menu.

## 2. Compute Linear Correlation
<p>Connect <b>Compute Linear Correlation</b> operator to the 
<b>Import data</b> operator to get Pearson correlation coefficients between features. It should become clear that there are strong correlations in the data.</p>

## 3. Remove correlated features
<p>Drop features that are highly redundant. This can be 
done in three different ways:</p>

-  manually

- using an operator

- programmatically with R/Python

Here's one example how to achieve this with Python code:

```python
# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# imports up here can be used to 
import pandas as pd
import numpy as np

# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1 = None, dataframe2 = None):

    # Create correlation matrix
    corr_matrix = dataframe1.corr().abs()

    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

    # Find index of feature columns with correlation greater than 0.95
    to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]
    
    # Drop features 
    dataframe1.drop(to_drop, axis=1, inplace = True)
    
    # Return value must be of a sequence of pandas.DataFrame
    return dataframe1,
```

## 4. Split data
<p>Make sure the random sampling of data is representative. 
This can be achieved by doing stratified sampling, within 
the classes of the Label.</p>

## 5. Model optimisation
<p>This step requires two operators; a trainable model and
<b>Tune Model Hyperparameters</b>. Remember that the the tuning 
is to be done on the <i>training</i> data.</p>

- <b>Model</b>: train mode needs to be set to <i>Parameter Range</i>

- <b>Tuning</b>: here ione needs to configure the (1) sweeping mode, (2) number of runs, (3) the label, and (4) the metric for evaluating model performance.

<p>As this is a multi-class classification problem, 
the evaluation metrics that are easiest to interpret are 
Accuracy and Average Log Loss.</p>

## 6. Model evaluation
Finally, add these operators to get an idea how well the model(s) performs

- <b>Score model</b> operator

- <b>Evaluate model</b> operator

<p>In the <b>Evaluate model</b> operator, one can compare the
performance between two different models.</p>