# Integrating kNN with Foundation Models for Adaptable and Privacy-Aware Image Classification
Official code repository for the paper: "Integrating kNN with Foundation Models for Adaptable and Privacy-Aware Image Classification" (ISBI 2024)

## News 🎉
- Paper is accepted for IEEE ISBI 2024 🎉
<p align="middle">
  <img src="https://github.com/TobArc/ISBI2024_knn-image-classification/assets/98497332/e95d8c9f-0671-463f-a074-75756175d4a2" width="500" />
</p>
  
- Code will be released soon 🛠️🔜
  
## Overview 🧠
Traditional deep learning models encode knowledge within their parameters, limiting transparency and adaptability to data changes. This poses challenges for addressing user data privacy concerns. To overcome this limitation, we propose to store embeddings of the training data independently of the model weights. This enables dynamic data modifications without retraining. Our approach integrates the k-Nearest Neighbor (k-NN) classifier with a vision-based foundation model pre-trained on natural images in a self-supervised manner. This integration enhances interpretability and adaptability while addressing privacy concerns.

![method_300dpi](https://github.com/TobArc/ISBI2024_knn-image-classification/assets/98497332/07f80739-62ab-4285-bf02-aa8b800dba8b)

## Key Features 🔑
- Open-source implementation including a previously unpublished baseline method and performance-improving contributions
- Integration of k-NN classifier with recent vision-based foundation models
- Flexible data storage system for dynamic data modifications without retraining
- Evaluation of method's performance across established benchmark datasets and medical image classification tasks
- Assessment of method's robustness in continual learning and data removal scenarios

## Results 📊
### 1. Improved classification accuracy demonstrated across established benchmark datasets

| Accuracy [\%]          | CIFAR-10 | CIFAR-100 | STL-10  |
|------------------------|----------|-----------|-------- |
| ResNet-101             | 87.3     | 63.6      | 98.1    |
| CLIP ViT-B/16          | 92.4     | 68.0      | 98.5    |
| CLIP ViT-L/14          | 95.5     | 74.2      | 99.4    |
| DINOv2 ViT-B/14        | 98.0     | 87.2      | 99.4    |
| DINOv2 ViT-L/14        | **98.5** | **88.3**  | **99.5**|

Table 1: Classification accuracy of our k-NN approach for different backbone choices.
  
### 2. Applicability of the method to distinct medical image classification tasks confirmed

| Accuracy [\%]                          | Pneumonia | Melanoma |
|----------------------------------------|-----------|----------|
| CovXNet† (Mahmud et al. 2020)          | **98.1**  | ---      |
| EfficientNetB0† (Cassidy et al. 2022)  | ---       | 62.1     |
| Ours (DINOv2 ViT-B/14)                 | 88.1      | 68.5     |
| Ours (DINOv2 ViT-L/14)                 | 89.9      | **69.8** |

Table 2: Comparison of our approach’s strong transfer learning ability for medical image analysis († refers to fully supervised, end-to-end models).

### 3. Robustness in continual learning and data removal scenarios demonstrated

<p align="middle">
  <img src="https://github.com/TobArc/ISBI2024_knn-image-classification/assets/98497332/4ed7a6cd-6079-4377-aac7-3ef031daa7fd" width="350" />
  <img src="https://github.com/TobArc/ISBI2024_knn-image-classification/assets/98497332/2d8a88c0-34ee-4e8b-931f-309acfff26f1" width="350" /> 
</p>

Figure 1: Visualization of the method’s ability for diverse continual learning tasks (left: class incremental learning, right: sample incremental learning).

<p align="middle">
  <img src="https://github.com/TobArc/ISBI2024_knn-image-classification/assets/98497332/83d325c2-bc70-4eb1-ac44-44d670f76edf" width="350" />
  <img src="https://github.com/TobArc/ISBI2024_knn-image-classification/assets/98497332/c326c177-270b-4d88-ab0e-31a7d8693fa0" width="350" /> 
</p>

Figure 2: Illustration of our method’s classification consistency despite the continuous diminishing of the support set (left: Pneumonia, right: Melanoma).

## Getting Started 🚀
To get started with using our method, follow these steps:
TODO

## Acknowledgements 👏
- [Chroma](https://www.trychroma.com) (The AI-native open-source embedding database")
- [PyTorch](https://pytorch.org) 
- [timm](https://github.com/huggingface/pytorch-image-models) (Ross Wightman - PyTorch Image Models)
- [pandas](https://pandas.pydata.org)
- [scikit-learn](https://scikit-learn.org/stable/)
- Nakata, Kengo, et al. "Revisiting a knn-based image classification system with high-capacity storage." European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2022. [doi](https://doi.org/10.1007/978-3-031-19836-6_26)

# Citation 📖
If you find this work useful in your research, please consider citing our paper:
- [Publication](...)
- [Preprint](https://arxiv.org/abs/2402.12500)

```
@InProceedings{doerricharchut2024kNNIntegration,
   author="Doerrich, Sebastian and Archut, Tobias and Di Salvo, Francesco and Ledig, Christian",
   title="Integrating kNN with Foundation Models for Adaptable and Privacy-Aware Image Classification",
   booktitle="2024 IEEE 21th International Symposium on Biomedical Imaging (ISBI)",
   year="2024",
}
```
