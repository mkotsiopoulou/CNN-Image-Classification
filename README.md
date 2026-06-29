# CNN Image Classification
## Project Overview
This project implements an image classification pipeline using a Convolutional Neural Network (CNN) based on the pre-trained AlexNet architecture. The workflow includes dataset preparation, preprocessing, model training, and performance evaluation on the Caltech-101 image dataset. The project demonstrates practical applications of deep learning, transfer learning, computer vision, and image classification using PyTorch.

---

## Methodology
The workflow includes:
1. Loading the Caltech-101 image dataset and annotation files
2. Exploring the available object categories
3. Splitting the dataset into training and testing sets
4. Applying image preprocessing and transformations
5. Loading a pre-trained AlexNet model (Transfer Learning)
6. Fine-tuning the classifier for 102 object categories
7. Training the CNN using PyTorch
8. Evaluating classification performance
9. Visualizing the results with a confusion matrix

---

## Sample Results
### Confusion Matrix
The confusion matrix summarizes the classification performance of the trained AlexNet model across all object categories, highlighting correctly classified samples as well as common misclassifications.
![Confusion Matrix](results/Confusion_Matrix.png)

## Technologies Used
- Python
- Jupyter Notebook
- PyTorch
- Torchvision
- NumPy
- Matplotlib
- AlexNet
- Convolutional Neural Networks (CNNs)
- Transfer Learning
- Deep Learning

## Dataset
The project uses the Caltech-101 image dataset, which containts 102 object categories commonly used for image classification research.
[Caltech Vision Datasetes](https://www.vision.caltech.edu/datasets/).
