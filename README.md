# Predicting Real-Time Traffic and Congestion Hotspots in Dhaka City Using Machine Learning

A comprehensive deep learning project that analyzes and predicts traffic patterns in Dhaka City using multiple state-of-the-art computer vision models.

> **📄 [Read the Complete Research Paper](Publication/compiled/Predicting%20Real-Time%20Traffic%20and%20Congestion%20Hotspots%20in%20Dhaka%20City.pdf)** - Comprehensive analysis of all models, methodologies, and results

## 🚗 Project Overview

This project implements and compares multiple deep learning architectures to classify traffic density levels in Dhaka City from street images. The system can predict traffic conditions in real-time, helping with urban planning and traffic management.

### Traffic Categories
- **No Traffic**: Free-flowing roads
- **Light Traffic**: Minimal congestion
- **Moderate Traffic**: Some congestion present
- **Heavy Traffic**: Significant congestion

## 🏗️ Architecture & Models

### Implemented Models
1. **Custom CNN**: Base convolutional neural network
2. **ResNet50**: Deep residual network with skip connections
3. **MobileNetV2**: Lightweight model optimized for mobile deployment
4. **EfficientNetB0**: Compound scaling method for optimal efficiency

### Image Sizes Tested
- 128x128 pixels
- 256x256 pixels  
- 512x512 pixels

## 📊 Results

### Model Performance Comparison

| Model | Best Accuracy | Optimal Image Size | Training Time | AUC Score |
|-------|---------------|-------------------|---------------|-----------|
| CNN | 35.83% | 128x128 | 25.8s | 0.626 |
| ResNet50 | 33.17% | 128x128 | 208.9s | 0.538 |
| MobileNetV2 | 45.50% | 128x128 | 226.5s | 0.519 |
| EfficientNetB0 | **54.17%** | 128x128 | 94.5s | **0.751** |

**Best Performing Model**: EfficientNetB0 achieves the highest accuracy of 54.17% with the best AUC score of 0.751, while maintaining reasonable training time.

### Key Insights
- Image size significantly impacts model performance and training time
- Different architectures show varying effectiveness for traffic classification
- Comprehensive confusion matrices and ROC curves available for detailed analysis

## 📁 Project Structure

```
├── All Models Combined/          # Comparative analysis and plots
├── CNN/                         # Custom CNN implementation and results
├── ResNet50/                    # ResNet50 implementation and results  
├── MobileNetV2/                 # MobileNetV2 implementation and results
├── EfficientNetB0/              # EfficientNetB0 implementation and results
├── JSON Files/                  # Model results and metrics in JSON format
├── Publication/                 # Research paper and documentation
│   ├── compiled/                # Final PDF document
│   ├── latex/                   # LaTeX source files
│   └── figures/                 # Paper figures and charts
└── README.md                    # Project documentation
```

## 📑 Research Paper

This project includes a comprehensive research paper documenting the methodology, experiments, and results of the traffic prediction system. The paper presents a detailed analysis of all four models and their performance across different image resolutions.

### 📄 **[📖 READ THE FULL PAPER (PDF)](Publication/compiled/Predicting%20Real-Time%20Traffic%20and%20Congestion%20Hotspots%20in%20Dhaka%20City.pdf)**

### Paper Highlights
- **Comprehensive Model Comparison**: Detailed analysis of CNN, ResNet50, MobileNetV2, and EfficientNetB0
- **Multi-Resolution Analysis**: Performance evaluation across 128×128, 256×256, and 512×512 image sizes  
- **Statistical Analysis**: ROC curves, confusion matrices, and accuracy metrics
- **Real-World Applications**: Practical implications for traffic management in Dhaka City

### Access the Paper
- **📄 PDF Document**: [Publication/compiled/Predicting Real-Time Traffic and Congestion Hotspots in Dhaka City.pdf](Publication/compiled/Predicting%20Real-Time%20Traffic%20and%20Congestion%20Hotspots%20in%20Dhaka%20City.pdf)
- **LaTeX Source**: Available in [`Publication/latex/`](Publication/latex/) directory
- **Figures**: High-quality visualizations in [`Publication/figures/`](Publication/figures/)
- **Documentation**: Complete paper information in [`Publication/README.md`](Publication/README.md)

The paper is formatted using IEEE conference template and includes all experimental results and analysis from this project.

## 🛠️ Technologies Used

- **Python**: Primary programming language
- **TensorFlow/Keras**: Deep learning framework
- **OpenCV**: Image processing
- **Matplotlib/Seaborn**: Data visualization
- **NumPy/Pandas**: Data manipulation
- **Scikit-learn**: Metrics and evaluation

## 📈 Visualization & Analysis

The project includes comprehensive visualizations:
- **Learning Curves**: Training and validation accuracy/loss over epochs
- **Confusion Matrices**: Detailed classification results
- **ROC Curves**: Model performance analysis
- **Accuracy vs Image Size**: Impact of input dimensions
- **Training Time Analysis**: Computational efficiency comparison

## 🚀 Getting Started

### Prerequisites
```bash
pip install tensorflow
pip install opencv-python
pip install matplotlib
pip install seaborn
pip install numpy
pip install pandas
pip install scikit-learn
```

### Usage
1. Clone the repository
2. Navigate to the specific model directory
3. Open the Jupyter notebook (e.g., `cnn-model-and-plot.ipynb`)
4. Run the cells to train and evaluate the model

## 📝 Datasets

The project uses a preprocessed traffic dataset based on DhakaAI's traffic detection dataset, specifically categorized for 4-level congestion classification.

**Dataset Source**: [Dhaka City Traffic Classification Dataset - 4-Level Congestion Analysis](https://www.kaggle.com/datasets/mdromanbinjalal/dhaka-traffic-classification-4-levels)

**Original Data**: Derived from [DhakaAI Traffic Detection Dataset](https://www.kaggle.com/datasets/rifat963/dhakaai-dhaka-based-traffic-detection-dataset)

**Categories**:
- **No Traffic**: Free-flowing roads
- **Light Traffic**: Minimal congestion  
- **Moderate Traffic**: Some congestion present
- **Heavy Traffic**: Significant congestion

### Getting the Dataset
```bash
# Install Kaggle API
pip install kaggle

# Download dataset (replace with your actual dataset name)
kaggle datasets download -d mdromanbinjalal/dhaka-traffic-classification-4-levels

# Extract to data folder
unzip dhaka-traffic-classification-4-levels.zip -d data/
```

## 🎯 Future Work

- [ ] Implement real-time video processing
- [ ] Deploy models for mobile applications
- [ ] Add temporal analysis for traffic pattern prediction
- [ ] Integrate with GPS data for location-specific predictions
- [ ] Implement ensemble methods for improved accuracy

## 👥 Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a feature branch
3. Making your changes
4. Submitting a pull request

## 📧 Contact

For questions or collaboration opportunities, please reach out through GitHub issues.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*This project was developed as part of traffic management research for urban planning in Dhaka City.*
