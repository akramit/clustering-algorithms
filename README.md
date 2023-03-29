# clustering-algorithms

The problem of clustering data in a similar group is one of the most studied problem in Computer Science. It has found applications in various areas such as data mining, information retrieval, image processing, protein sequencing, NLP(auto correction) etc. 

## Problem Definition
Given a set of input points (data) we would like to form a cluster based on their similarity. We can define similarity based on various metrics. One such metric is euclidean distance between the two input points on the Real plane. There are 3 main kind of clustering problems - k-center, k-means and k-median. 
### k-center 
In this problem, for a given set of inputs we want to form k clusters of data such that maximum radius of each cluster is minimized.

### k-means
In this problem, for a given set of inputs we want to form k clusters of data such that sum of the square of the distances of a point to the nearest center is minimized.

### k-median
In this problem, for a given set of inputs we want to form k clusters of data such that sum of the distance of a point its nearest center is minimized. Note that this problem is similar to the k-facility location problem where we set k-facilities such that sum of the distance of the node from the facilities is minimized.

## Computational Complexity
All these problems are NP-Hard. There are no polynomial time algorithm known for these problems. Hence, we try to provide polynomial time apporoximate solution to these problems. 

## Study on k-median
We study particularly the k-median problem here. The input data points are Boolean strings and the distance used for similarity is Hamming Distance. For two given Boolean strings x and y, the hamming distance, d(x,y) is the number of coordinates where the two inputs differ. For example, the distance between 
"00101" and "10001" is 2. Below are some notations. 

n - Total number of strings in the input
d - Length of each string
k - Number of Clusters
Med - Median Objective Value which is sum of distance of each points to its centre.

### Some Results
1-Median is very easy to compute. The coordinate wise majority is the median of the set. 
For k>=2, the problem is NP-Hard. There are polynomial time (1+\epsilon) approximation known for this problem. 

### Strategy 1 - Approximation Algorithm
We look at an approximation algorithm for k=2. 
1. Initialization - Find two points x and y such that distance between them is highest. 
2. Put x into Cluster C1 and y into Cluster C2. 
3. For each of the input points z do - 
4. Compute distance of z to both centers C1 and C2. 
5. Put z into the closest center and update C1 or C2 respectively. 
6. Return the objective value in the end for C1 and C2

### Running Time
The running time complexity is O(n^2. d) 
### Approximation Guarantees
