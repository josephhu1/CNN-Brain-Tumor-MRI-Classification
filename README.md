# Brain Tumor Detection in MRI Scan Images

This repository contains the trained machine learning model and a prediction script for brain tumor detection, which earned 2nd Place and an Honorable Mention for Most Impactful Potential at the InT BioHackathon Competition @ UCLA, May 2024.

## Overview

The model is a Convolutional Neural Network (CNN) designed to classify MRI scans into four categories:
- Glioma
- Meningioma
- No Tumor
- Pituitary Tumor

Performance Metrics
- Accuracy: 99.85%
- Precision: 99.95%
- Recall: 99.94%

## Usage

I provided a script to predict and classify brain tumors from MRI scan images. The script will output the classification result to the console.

To perform a prediction, run the following command:

```
$ python predict.py <img_path>
```

## Note

I only included the source code for the model, training script, and the prediction script. The source code for the full-stack web application is not included in this repository because I plan to continue developing this project in the future.

If you have any inquiries or are interested in collaboration opportunities, please contact me at:

📧 Email: joehu@ucla.edu

## Technologies and Tools
- Front-end: JavaScript, React.js
- Back-end: Flask (Python)
- Machine Learning Framework: Keras with TensorFlow backend
- Python Libraries: TensorFlow, NumPy, Pandas, Matplotlib, Seaborn, PIL, Scikit-learn
