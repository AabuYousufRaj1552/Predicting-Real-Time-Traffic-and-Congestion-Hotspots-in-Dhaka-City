# Research Paper: Predicting Real-Time Traffic and Congestion Hotspots in Dhaka City Using Machine Learning

## 📄 **[READ THE PAPER](compiled/Predicting%20Real-Time%20Traffic%20and%20Congestion%20Hotspots%20in%20Dhaka%20City.pdf)** 

## Overview
This directory contains the complete research paper documenting the traffic congestion prediction system for Dhaka City. The paper presents a comprehensive analysis of four deep learning models (CNN, ResNet50, MobileNetV2, and EfficientNetB0) for real-time traffic classification.

## 📁 Directory Structure

```
Publication/
├── README.md                    # This file - Paper documentation
├── compiled/                    # Final PDF document
│   └── Predicting Real-Time Traffic and Congestion Hotspots in Dhaka City.pdf  # **📄 MAIN PAPER**
├── latex/                       # LaTeX source files
│   ├── conference.tex          # Main paper source
│   ├── IEEEtran.cls           # IEEE conference template
│   └── IEEEtran_HOWTO.pdf     # IEEE template documentation
└── figures/                     # All paper figures
    ├── best_combined_confusion_matrices.png
    ├── f1_score_plot.png
    ├── fig1.png
    ├── Final_Accuracy_Comparison_with_Image_Size.png
    ├── Number of Images per Labels in Train and Test Set.png
│   └── ROC_Curve.png
└── compiled/                    # Compiled PDF versions
    └── Predicting Real-Time Traffic and Congestion Hotspots in Dhaka City.pdf  # **📄 MAIN PAPER**
```

## 📊 Paper Abstract
*This research presents a comprehensive machine learning approach to predict real-time traffic conditions and identify congestion hotspots in Dhaka City. Four state-of-the-art deep learning models were evaluated: CNN, ResNet50, MobileNetV2, and EfficientNetB0, trained on a custom dataset of traffic images with four congestion levels (no traffic, light traffic, moderate traffic, heavy traffic).*

## 🔬 Key Contributions
- **Novel Dataset**: Custom traffic classification dataset for Dhaka City with 4-level congestion analysis
- **Comprehensive Model Comparison**: Evaluation of 4 different deep learning architectures
- **Multi-Resolution Analysis**: Performance analysis across different image sizes (128×128, 256×256, 512×512)
- **Real-World Application**: Practical system for traffic management in urban environments

## 📈 Key Results
- **Best Performance**: EfficientNetB0 achieved the highest accuracy across multiple image resolutions
- **Optimal Image Size**: 256×256 pixels provided the best balance between accuracy and computational efficiency
- **Robust Classification**: All models demonstrated strong performance in distinguishing between traffic congestion levels
- **Practical Deployment**: Real-time inference capabilities suitable for traffic monitoring systems

## 🛠️ How to Compile the Paper

### Prerequisites
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- IEEE conference template support

### Compilation Steps
```bash
cd Publication/latex/
pdflatex conference.tex
bibtex conference     # If using bibliography
pdflatex conference.tex
pdflatex conference.tex
```

### Alternative: Online Compilation
You can also compile the paper using online LaTeX editors like:
- [Overleaf](https://www.overleaf.com/)
- [ShareLaTeX](https://www.sharelatex.com/)

Simply upload the contents of the `latex/` directory.

## 📷 Figures Description

| Figure | Description |
|--------|-------------|
| `fig1.png` | System architecture overview |
| `Number of Images per Labels in Train and Test Set.png` | Dataset distribution visualization |
| `Final_Accuracy_Comparison_with_Image_Size.png` | Model accuracy comparison across image sizes |
| `best_combined_confusion_matrices.png` | Confusion matrices for all models |
| `f1_score_plot.png` | F1-score comparison across models |
| `ROC_Curve.png` | ROC curves for model performance evaluation |

## 📝 Citation
If you use this work in your research, please cite:

```bibtex
@article{traffic_prediction_dhaka2025,
  title={Predicting Real-Time Traffic and Congestion Hotspots in Dhaka City Using Machine Learning},
  author={[Your Name]},
  journal={[Journal/Conference Name]},
  year={2025},
  url={https://github.com/[username]/Predicting-Real-Time-Traffic-and-Congestion-Hotspots-in-Dhaka-City-Using-Machine-Learning}
}
```

## 🔗 Related Resources
- **Main Repository**: [../README.md](../README.md)
- **Dataset**: [Dhaka Traffic Classification Dataset](https://www.kaggle.com/datasets/mdromanbinjalal/dhaka-traffic-classification-4-levels)
- **Model Implementations**: 
  - [CNN Model](../CNN/)
  - [ResNet50 Model](../ResNet50/)
  - [MobileNetV2 Model](../MobileNetV2/)
  - [EfficientNetB0 Model](../EfficientNetB0/)

## 📧 Contact
For questions about the research or collaboration opportunities, please refer to the main repository's contact information.

## 📄 License
This research paper is part of the larger project and is subject to the same MIT License as specified in the [main repository](../LICENSE).

---
*This paper represents unpublished research conducted as part of the traffic prediction system development for Dhaka City.*
