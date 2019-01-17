# -*- coding: utf-8 -*-
"""

Author : Diksha Chhabra
Date:11/10/2018
"""

#from google.colab import drive
#drive.mount("/content/drive")

from skimage import io
import random
import numpy as np
import math
import sys

def calculate_dist(image1, centroids):
  pixel_assign_cluster = []
  print(centroids)

  for rgb in image1:

    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    len_centroids = len(centroids)
    min_dist = 10000
    min_center = 1
    for i in range(len_centroids):
      r_c = centroids[i][0]
      g_c = centroids[i][1]
      b_c = centroids[i][2]


      dist = math.sqrt(pow((int(r) - int(r_c)), 2) + pow((int(g) - int(g_c)), 2) + pow((int(b) - int(b_c)), 2))
      if dist < min_dist:
        min_dist = dist
        min_center = i



    pixel_assign_cluster.append(min_center)

  return pixel_assign_cluster

def update_centroid(image1, centroids, pixel_assign_cluster, k):
  
   # change the centroid
  len_pixel_assign_cluster = len(pixel_assign_cluster)
  
  for i in range(k):
    #find all those points belonging to centroid number i
    sum_r = 0
    sum_g = 0
    sum_b = 0
    total_pixel = 0

    for pixel_num in range(len_pixel_assign_cluster):
      if pixel_assign_cluster[pixel_num] == i:
        rgb = image1[pixel_num]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]

        sum_r = sum_r + r
        sum_g = sum_g + g
        sum_b = sum_b + b
        total_pixel = total_pixel + 1

    # handling points not assigned to this cluster at all
    if total_pixel != 0:
      new_r = sum_r/total_pixel
      new_g = sum_g/total_pixel
      new_b = sum_b/total_pixel


      centroids[i] = np.asarray([new_r, new_g, new_b])
  
  return centroids

#reshaped image is taken here
def k_means(image1, k, num_iterations):
  len_image1 = len(image1)
  a = random.sample(range(0,len_image1), k)

  # get the pixel rgb values from these random indices 
  ## getting k-means initial values

  centroids = []
  for i in a:
    centroids.append(image1[i])
  count = 0
  for loop in range(num_iterations):
    #calculate euclidean dist
    pixel_assign_cluster = calculate_dist(image1, centroids)


    # update centroids
    
    centroids = update_centroid(image1, centroids, pixel_assign_cluster, k)
    
  
  len_pixel_assign_cluster = len(pixel_assign_cluster)
  
  # after doing it for n number of iterations, change the values of pixels to its nearest mean
  for pixel_num in range(len_pixel_assign_cluster):
    cluster = pixel_assign_cluster[pixel_num]
    rgb = centroids[cluster]
    image1[pixel_num] = rgb
  
  return [image1,count]



###### main function ######

image1 = sys.argv[1]
k = sys.argv[2]
num_iterations = sys.argv[3]

image1 = io.imread(image1)

rows1 = image1.shape[0]
cols1 = image1.shape[1]

image1 = image1.reshape(rows1 * cols1, 3)
len_image1 = len(image1)

k = int(k)
num_iterations = int(num_iterations)

[i1,iteration] = k_means(image1, k, num_iterations)

labels1 = i1.reshape(rows1,cols1,3)
io.imshow(labels1)





