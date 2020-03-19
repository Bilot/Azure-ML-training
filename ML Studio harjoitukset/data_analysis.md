---
Date: "2019-09-18"
Step: 'Data analysis'
Description: Data inspection & manipulation exercise, using the diabetes data.
---

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe28kRsvMfHCz-rQz5oZgtVJhks1S6_W5W0WRcudlJf3_WVS5J" width="150" style="float:right;"/>

# Data Analysis
<br>

## 1. Import Data

- __Source__: Azure Blob

- __SAS__: ask for this

- __File has header__: TRUE

- __Use cached results__: TRUE

## 2. Convert to CSV
<p>After adding this operator, connecting it to the <b>Import Data</b> operator, and running the experiment, open the converted data in a new <b>R</b> Notebook.</p>

<p>This opens a new Azure (Jupyter) Notebook, using R-language.

## 3. R Notebook
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1200px-Jupyter_logo.svg.png" 
width="150"
style="float:right;"/>

After running the first two cells, in the next empty cell, 
type:

```r
summary(dat) 
```

<p>
and press <code>shift+enter</code>. This will print out the basic 
statistical summary of each variable. In the next cell, type two 
commands:</p>

```r
prop_zero = colSums(dat==0)/nrow(dat)
round(prop_zero,2)
```

<p>The first line calculates the proportion of zeros in each column,
while the second simply rounds the result to precision of two signigicant numbers. </p>

<p>From the result it is clear that there are many missing values in the data; zero-values do not make any sense, except for <code>Pregnancies</code> and <code>Outcome</code>. Try to see how the number of remaining rows changes when you drop all missing values. Does it make sence?</p>

### Replace zeros with missing values
<p>To replace zeros with missing (<code>NA</code>), run the following commands:

```r
# make copy of data:
df = dat
# select columns to modify:
cols = setdiff(names(df),
               c('Pregnancies', 'Outcome'))
# make replacement:
df[,cols] = sapply(
  df[,cols], 
  function(x) ifelse(x==0,NA,x)
)
```

<p>Next, inspect the distribution of features, with 
respect to the <code>Outcome</code>.</p> 

### Visualise distributions

<p>The following code will display how the different
features are distributed and whether there is a 
difference between Outcomes:</p> 

```r
# Adjust figure options:
library(repr)
options(repr.plot.width = 10, 
        repr.plot.height = 6)

# Load requirted libraries:
library(ggplot2)
library(tidyr)

# Make data tidy:
x = gather(df,key = 'variable',
           value = 'value', 
           -Outcome)
x$Outcome = factor(x$Outcome)

# Draw graph:
ggplot(x, aes(value, fill = Outcome)) + 
    geom_histogram(position = 'dodge',
                   alpha = 0.8) +
    facet_wrap(~variable, 
               scales = 'free',
               ncol = 3)
```

## 4. Execute R Script
<p>To fix the data, such that zeros are coded to missing values,
the best way is to execute a script, either using <b>R</b> or <b>Python</b>. This example uses <b>R</b>. Posting the following code <i>R cript</i> section of the operator and runnig the experiment will produce the desired outcome:
</p>

```r
# Get data from input port:
dataset1 <- maml.mapInputPort(1) # class: data.frame

# select columns to be modified:
cols = setdiff(names(dataset1),
               c('Pregnancies', 'Outcome'))
for(i in cols){
    # select rows to be affected:
    rows = dataset1[,i] == 0
    # make replacement: 
    dataset1[rows,i] = NA
}

# Send data to the output Dataset port:
maml.mapOutputPort("dataset1");
```

<p>This script uses lower lower level programming to achieve the 
same outcome as that used above. Feel free to use either version.</p>

## 5. Select Column in Dataset

<p>Connect the <b>Execute R Script</b> operator to a 
<b>Select Column in Dataset</b> operator. Using this operator,
drop <code>Insulin</code> from the data. This could ofcourse also 
be done using a script. </p>

Save data as Dataset for later use.

## 6. Split Data

<p>Before doing any further manipulations to the data, we need
to split it to training and testing parts. This is done to be able
to evaluate the effect of the manipulations.</p>

<p>To achive this, add a <b>Split Data</b> operator, where you need to specify the split ratio. By default, <i>Stratified split</i> is set to false, but it is good practice to set this to true to make sure the 
samples are representative.</p>

## 7. Clean Missing Data

<p>Next, add an operator to impute (replace) missing values: 
<b>Clean Missing Data</b>. This operator offers several 
alternative methods that can be used for missing value replacement.
It is recommended to compare how the imputation affects any modeling 
results. Again, this step could also be done using a script.</p>

## 8. Convert to CSV

<p>To properly inspect the imputed data, first convert the 
data to csv-format. Next, from the <b>Convert to CSV</b>
operator, get <i>Generate Data Access Code</i>, 
which can be used in the previously created Notebook.</p>