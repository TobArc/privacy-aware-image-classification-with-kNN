# ISBI2024: Integrating kNN with Foundation Models for Adaptable and Privacy-Aware Image Classification
Official code repository for the ISBI 2024 paper: "Integrating kNN with Foundation Models for Adaptable and Privacy-Aware Image Classification"

## News:
- Paper is accepted for IEEE ISIB 2024 🎉
- Code will be released soon 🛠️🔜
  
## Overview 🧠
Traditional deep learning models encode knowledge within their parameters, limiting transparency and adaptability to data changes. This poses challenges for addressing user data privacy concerns. To overcome this limitation, we propose to store embeddings of the training data independently of the model weights. This enables dynamic data modifications without retraining. Our approach integrates the k-Nearest Neighbor (k-NN) classifier with a vision-based foundation model pre-trained on natural images in a self-supervised manner. This integration enhances interpretability and adaptability while addressing privacy concerns.

![method_300dpi](https://github.com/TobArc/ISBI2024_knn-image-classification/assets/98497332/07f80739-62ab-4285-bf02-aa8b800dba8b)

## Key Features
- Open-source implementation including a previously unpublished baseline method and performance-improving contributions
- Integration of k-NN classifier with recent vision-based foundation models
- Flexible data storage system for dynamic data modifications without retraining
- Evaluation of method's performance across established benchmark datasets and medical image classification tasks
- Assessment of method's robustness in continual learning and data removal scenarios

## Results
- Improved classification accuracy demonstrated across established benchmark datasets

\begin{table}
\caption{Classification accuracy of our \ac{kNN} approach for different backbone choices.}
\label{tab:classification}
    \centering
    \begin{tabular}{l c c c}
        \toprule
        Accuracy [\%] & CIFAR-10 & CIFAR-100 & STL-10 \\
        \midrule
        % $\text{ResNet-50}$ & $82.8$ & $55.7$ & $96.8$ \\
        $\text{ResNet-101}$ & $87.3$ & $63.6$ & $98.1$ \\
        $\text{CLIP ViT-B/16}$ & $92.4$ & $68.0$ & $98.5$ \\
        $\text{CLIP ViT-L/14}$ & $95.5$ & $74.2$ & $99.4$ \\
        $\text{DINOv2 ViT-B/14}$ & $98.0$ & $87.2$ & $99.4$ \\
        $\text{DINOv2 ViT-L/14}$ & $\mathbf{98.5}$ & $\mathbf{88.3}$ & $\mathbf{99.5}$ \\
        \bottomrule
    \end{tabular}
\end{table}
  
- Applicability of the method to distinct medical image classification tasks confirmed
- Robustness in continual learning and data removal scenarios demonstrated

## Getting Started
To get started with using our method, follow these steps:
TODO

## Acknowledgements 👏
TODO: Add links
- Chroma
- pytorch
- timm
- pandas
- scikit-learn
- Nakara et al.

# Citation 📖
If you find this work useful in your research, please consider citing our paper:
- [Publication](...)
- [Preprint](...)

```
@InProceedings{doerrich2023unoranic,
   author="Doerrich, Sebastian and Archut, Tobias and Di Salvo, Francesco and Ledig, Christian",
   title="Integrating kNN with Foundation Models for Adaptable and Privacy-Aware Image Classification",
   booktitle="2024 IEEE 21th International Symposium on Biomedical Imaging (ISBI)",
   year="2024",
}
```
