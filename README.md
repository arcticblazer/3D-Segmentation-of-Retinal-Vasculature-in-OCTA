# 3D-Segmentation-of-Retinal-Vasculature-in-OCTA
Code written as part of my thesis "3D Segmentation of Retinal Vasculature in OCTA"

This repository contains all code that was used for performing 3D segmentation on retinal OCTA images from the dataset OCTA500. First preprocessing is performed on the images using median filtering and CLAHE after which 3 different segmentation algorithms are implemented and executed:
 - Active Contour Model
 - Local Adaptive Thresholding
 - Optimally Oriented Flux

Following is the order of application of scripts and their usage - 

### 1) extract_frames.py - 
  Takes in all individual frames for a single patient that is given as .bmp files and makes a single .bmp file with each frame addpended at the bottom of the image.
  This has been done to standardize the input and output formats for the rest of pipeline.
  
  Input Directory : ./Data/Raw/
  
  Output Directory : ./Data/Compiled/
  
### 2) preprocess_median_filter.m - 
  Takes the compiled images as inputs and performs 3D Median Filtering on them before storing the result again. MATLAB's implementation has been used.
  
  Input Directory : ./Data/Compiled/
  
  Output Directory : ./Data/Filtered/

### 3) preprocess_clahe.py - 
  Takes the filtered images and uses MCLAHE to perform 3D CLAHE on the filtered images. 
  
  Input Directory : ./Data/Filtered/
  
  Output Directory : ./Data/Preprocessed/
  
### 4a) adaptive_threshold.py - 
  Applies 3D LAT on the preprocessed images.
  
  Output Directory : ./Data/LAT/
  
### 4b) acm.m - 
  Applies ACM on the preprocessed images. MATLAB's inbuilt function has been used.
  
  Output Directory : ./Data/ACM/
  
### 4c) oof_segment.m - 
  Calls the files oof3response.m and eigenvaluefield33.m given as part of the paper to obtain the OOF response matrix and apply thresholding on the same to obtain the segmented image.
  
  Output Directory : ./Data/OOF/
  
### 5) compare.py - 
  Takes the outputs from the 3 segmentation algorithms and outputs pair-wise DICE Coefficient. 
  Stores the results in results.csv for each image
  
Dependencies - 

MCLAHE (python)

Image Processing Toolkit (MATLAB)
