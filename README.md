In this python project, KMeans clustering is used for compressing a given image. DIfferent values of K can be used like 2,5,10,15,20. Till it reaches value of K=20, the picture almost looks like the original image. In this way, the size of the image is reduced and also the compressed image looks almost like the original image.

To compile and run
python3 kMeans_compression.py <image path> <K> <number of iterations>

Arguments
1)  image path --> The path to the image Eg. 'images/Koala.jpg'
2)  K --> The number of colours in the compressed image (K-NN)
3)  number of iterations --> The number of times to update the centroid and run K-NN.
