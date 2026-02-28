# KNN From Scratch (Basic)

This repository contains a simple implementation of the K-Nearest Neighbors (KNN) algorithm
written using basic Python only. No machine learning libraries are used.

## Description 
The KNN algorithm classifies a test point by calculating distances from known points
and assigning the label that appears most among the nearest neighbors.

## How to Run
1. Make sure Python is installed.
2. Open the file `knn.py`.
3. Run the program using:
   python knn.py

## Sample Output
Distances: [[1.0, 'A'], [1.41, 'A'], [4.47, 'B'], ...]
Sorted Distances: [[1.0, 'A'], [1.41, 'A'], ...]
Predicted label: A

## Key Learnings
- Understood how Euclidean distance is used in distance-based classifiers.
- Learned how the value of k affects prediction stability.
- Implemented majority voting logic manually.
- Observed limitations of KNN such as dependency on dataset size and distance computation cost.

## Language used
Python.

