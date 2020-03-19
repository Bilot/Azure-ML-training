---
Date: "2019-09-18"
Step: 'Model training'
Description: Modeling & evaluation exercise, using car price data.
---

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe28kRsvMfHCz-rQz5oZgtVJhks1S6_W5W0WRcudlJf3_WVS5J" width="150" style="float:right;"/>

# Regression

## 1. Import Data

- __Source__: Azure Blob

- __SAS__: ask for this

- __File has header__: TRUE

- __Use cached results__: TRUE

## 2. Data analysis

<p>Again, it is important to carefully inspect the data to see 
whether there are errors, missing values, or other issues that 
need attention.</p>

<p>The first issue is that the file separator is not OK, at 
least for the <b>Import Data</b> operator. To solve this,
use a <b>Execute Python Script</b> operator. Paste the following
code to the executable part (make sure the intendation in correct):</p>

```python
# Split the data into columns:
tmp = dataframe1.iloc[:,0].str.replace(pat='"',repl='')
tmp = tmp.str.split(pat=";", n=-1, expand=True)

# Replace column names:
names = dataframe1.columns.str\
        .replace(pat='"',repl='').str\
        .split(pat=";", n=-1)[0]
tmp.columns = names

# Change data types:
nums = ['vm','km','hinta','moottori','co2','kulyhd']
for x in nums:
    tmp[x] = tmp[x].astype('float')

return tmp
```

<p>From the output port you will get the fixed data, which
can be sent to <b>Summarize Data</b> operator.</p>

## 3. Data preparation
<p>Some of the features have classes that are very small.
What shoud be done with those?</p>

Other steps to be done: 

- set label with <b>Edit Metadata</b> operator 

- drop correlated columns with <b>Select Columns in Dataset</b> operator

## 4. Split data
<p>Here it is important to make sure the random sampling of 
data is representative. This can be achieved by doing stratified
sampling. But which variable should be used to define the 
stratification? The label is no good here.</p>

## 5. Train model
Steps to needed:

- Model to be trained (choose operator)

- <b>Train model</b> operator

## 6. Evaluate model
Finally, add these operators to get an idea how well the model(s) performs

- <b>Score model</b> operator

- <b>Evaluate model</b> operator

<p>The <b>Evaluate model</b> operator gives performance metrics 
for the model, against the testing data that should be connected 
to the <b>Score model</b> operator. </p>

Try different models and compare their performance.

## 7. Create Web Service
<p>When the experiment has been completed (run), it is possible to 
publish the model as a predictive web service. Doing this is
fairly simple in ML Studio:</p> 

- First, click the "SET UP WEB SERVICE" button. This will open a new tab: Predictive experiment.

- Next, run the <i>Predictive experiment</i>. This will serialise the model and store it under "Trained models" menu.

- Then, click the "DEPLOY WEB SERVICE" button and you're done! The deployed web service will appear under the "Web services" menu.
