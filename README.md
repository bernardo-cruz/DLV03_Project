# DLV03_Project
 [Deep Learning in Vision course | HSLU](https://elearning.hslu.ch/ilias/ilias.php?ref_id=5074857&cmdClass=ilrepositorygui&cmdNode=10d&baseClass=ilrepositorygui)

# Introduction
The aim of this repository is to create a bucket for all activities around semester project. 
The [report](./data/report.md) is a living-document and is subject to change.

## Automatic detection and description of the performance of financial instruments 
The information will be extracted from graphs of factsheets, of by own creation. The captions shall describe the movements etc. of a title. 
![Automatic analysis of graphs and description](data/img/ishares_smi.png)  
__Dataset - scrapping Google / Yahoo Finance API__  
[Image Captioning](https://towardsdatascience.com/a-guide-to-image-captioning-e9fd5517f350)

The aim is to achieve the following:
- Identify time axis values and monetary values.
- Identify the performance of financial title.
- Describe the performance of financial title with typical values such as the average, the standard deviation, the minimum and the maximum, correlation, covariance etc. 

## Models
- **VGG**  
  The runner-up in ILSVRC 2014 was the network from Karen Simonyan and Andrew Zisserman that became known as the VGGNet. Its main contri- bution was in showing that the depth of the network is a critical component for good performance. Their final best network contains 16 CONV/FC layers and, appealingly, features an extremely homogeneous architecture that only per- forms 3 × 3 convolutions and 2 × 2 pooling from the beginning to the end. Their pretrained model is available for plug and play use in Caffe. A downside of the VGGNet is that it is more expensive to evaluate and uses a lot more memory and parameters (140M). Most of these parameters are in the first fully connected layer, and it was since found that these FC layers can be removed with no perfor- mance downgrade, significantly reducing the number of necessary parameters.  

- **ResNet**
  Residual Network developed by Kaiming He et al. was the winner of ILSVRC 2015. It features special skip connections and a heavy use of batch nor- malization. The architecture is also missing fully connected layers at the end of the network. The reader is also referred to Kaiming’s presentation (video, slides), and some recent experiments that reproduce these networks in Torch. ResNets are currently by far state of the art Convolutional Neural Network models and are the default choice for using ConvNets in practice (as of May 10, 2016). In particular, also see more recent developments that tweak the orig- inal architecture from Kaiming He et al. Identity Mappings in Deep Residual Networks (published March 2016).  

# Technical Information
The [requirements.txt](./requirement.txt) describes the needed installation on your local machine.  
This repository can also be downloaded and used via Docker. 

# Important Links
- [Learning Rate Finder](https://medium.com/analytics-vidhya/the-learning-rate-finder-9203fdc67c92)  
- [Data Augmentation](https://towardsdatascience.com/complete-guide-to-data-augmentation-for-computer-vision-1abe4063ad07)
- [CNN](https://towardsdatascience.com/a-conceptual-explanation-of-convolutional-neural-networks-cnns-ccd2e62f213b)
- [CNN ELI5](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53) 
