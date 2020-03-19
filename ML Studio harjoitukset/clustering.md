---
Date: "2019-09-18"
Step: 'Data analysis'
Description: Data manipulation & clustering exercise, using the Steel Plates data.
---
  
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe28kRsvMfHCz-rQz5oZgtVJhks1S6_W5W0WRcudlJf3_WVS5J" width="150" style="float:right;"/>

# Clustering
<br>

## 1. Import Data

- __Source__: Azure Blob

- __SAS__: ask for this

- __File has header__: TRUE

- __Use cached results__: TRUE

## 2. Edit Metadata
<p>Change the role of the <code>Fault</code> column to "Label",
to separate it from the rest of the features later on.</p>

## 3. Select Columns in Dataset
<p>This operator is used next to drop features that have 
been used to generate the Label. Save as Dataset for later use.</p>

## 4. Summarize Data
<p>Connect <b>Summarize Data</b> operator to the 
<b>Select Columns in Dataset</b> operator to get 
statistical summary of the data.</p>

## 5. Normalize Data
<p>To perform a clustering, the features need to be taken to 
the same scale. Othervise features with greater variance will 
dominate the analysis. For this purpose, connect a 
<b>Normalize Data</b> operator to the <b>Select Columns in Dataset</b>
operator. Use "MinMax" scaling (try also different alternatives).</p>

## 6. Principal Component Analysis
<p>For visualisation purposes, perform a <b>Principal Component Analysis</b> (reducing to 2 dimensions) on the normalized data.</p>

## 7. Execute R Script
<p>Finally, connect an <b>Execute R Script</b> operator to the
<b>Normalize Data</b> and <b>Principal Component Analysis</b>
operators (in this order; this is assumed in the code). Next, 
add the following to the script-field:</p>
  
```r
# Map 1-based optional input ports to variables
df <- maml.mapInputPort(1) # class: data.frame
pca <- maml.mapInputPort(2) # class: data.frame

cols = setdiff(names(df),'Fault')
x = df[,cols]
n = length(unique(df$Fault))
result = kmeans(x = x, centers = n)

df$clusters = result$cluster
pca$clusters = factor(result$cluster)

# Output to GR-device:
library(ggplot2)
ggplot(pca,aes(Col1,Col2,
       col = clusters, 
       shape = Fault)) + 
    geom_point()

# Select data.frame to be sent to the output Dataset port
maml.mapOutputPort("df");
```

<p>This script combines the normalised data as well as the PCA
axes (which could also be calculated in this script). As an output
you get a visualisation of the clustering as well as a dataset that
has the cluster assignments included.</p>

## 8. Optimize Clustering
<p>As an alternative to manual tuning of the cluster number, one
can also automatically find an optimal clustering, based on some 
criterion. This can be done either with a script, or by using 
operators. The later method is used here.</p>

<p>Add a <b>K-Means Clustering</b> operator and a 
<b>Sweep Clustering</b> operator and connect these as required.
In the <b>K-Means Clustering</b> operator, specify a 
<i>Parameter range</i>, say 2, 3, 4, 5, 6, and 7. In the
<b>Sweep Clustering</b> operator, set Sweep mode to "Entire grid". 
After running the clustering sweep, inspect the Result dataset to see
how the assignment was made. Does the evaluation Metric affect
the clustering?</p>

<p>The most convenient way to analyse the clustering result
against the data is to use a Notebook.</p>

