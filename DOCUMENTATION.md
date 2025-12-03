# Traffic Prediction Project Documentation

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Model Architecture Details](#model-architecture-details)
3. [Dataset Information](#dataset-information)
4. [Installation Guide](#installation-guide)
5. [Usage Instructions](#usage-instructions)
6. [Results Analysis](#results-analysis)
7. [Troubleshooting](#troubleshooting)

## Project Overview

This project implements multiple deep learning architectures to classify traffic density from street images in Dhaka City. The goal is to develop an automated system that can predict traffic conditions in real-time to assist with urban planning and traffic management.

### Problem Statement
Traffic congestion is a major issue in Dhaka City, affecting millions of commuters daily. Manual traffic monitoring is inefficient and doesn't provide real-time insights. This project aims to solve this by:
- Automatically classifying traffic density from images
- Comparing different deep learning approaches
- Providing insights for traffic management systems

## Model Architecture Details

### 1. Custom CNN
- **Architecture**: Sequential CNN with multiple conv-pool layers
- **Layers**: 4 convolutional blocks + 2 fully connected layers
- **Parameters**: ~2.3M parameters
- **Activation**: ReLU activation with softmax output
- **Regularization**: Dropout layers to prevent overfitting

### 2. ResNet50
- **Architecture**: Residual network with skip connections
- **Pre-training**: ImageNet pre-trained weights
- **Fine-tuning**: Last layers adapted for 4-class traffic classification
- **Parameters**: ~25.6M parameters
- **Advantage**: Solves vanishing gradient problem with residual connections

### 3. MobileNetV2
- **Architecture**: Inverted residual blocks with depthwise separable convolutions
- **Design Goal**: Optimized for mobile deployment
- **Parameters**: ~3.5M parameters
- **Efficiency**: High accuracy with low computational cost
- **Innovation**: Inverted bottleneck design

### 4. EfficientNetB0
- **Architecture**: Compound scaling of depth, width, and resolution
- **Neural Architecture Search**: Optimized through automated search
- **Parameters**: ~5.3M parameters
- **Performance**: Best accuracy-efficiency trade-off
- **Scaling**: Systematic scaling methodology

## Dataset Information

### Classes
1. **No Traffic**: Free-flowing roads with minimal vehicles
2. **Light Traffic**: Some vehicles present, smooth flow
3. **Moderate Traffic**: Noticeable congestion, slower movement
4. **Heavy Traffic**: Significant congestion, stop-and-go traffic

### Data Structure
```
Train/
├── no traffic/
├── light traffic/
├── moderate traffic/
└── heavy traffic/

Test/
├── no traffic/
├── light traffic/
├── moderate traffic/
└── heavy traffic/
```

### Image Specifications
- **Formats**: JPEG/PNG images
- **Sizes Tested**: 128x128, 256x256, 512x512 pixels
- **Color Space**: RGB
- **Source**: Street cameras in Dhaka City

## Installation Guide

### Prerequisites
- Python 3.8 or higher
- pip package manager
- 8GB+ RAM recommended
- GPU optional (for faster training)

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/mdromanbinjalal/Predicting-Real-Time-Traffic-and-Congestion-Hotspots-in-Dhaka-City-Using-Machine-Learning.git
cd Predicting-Real-Time-Traffic-and-Congestion-Hotspots-in-Dhaka-City-Using-Machine-Learning

# Run setup script (Linux/Mac)
chmod +x setup.sh
./setup.sh

# OR install manually
pip install -r requirements.txt
```

### Manual Installation
```bash
pip install tensorflow>=2.8.0
pip install opencv-python>=4.5.0
pip install matplotlib>=3.5.0
pip install seaborn>=0.11.0
pip install numpy>=1.21.0
pip install pandas>=1.3.0
pip install scikit-learn>=1.0.0
pip install jupyter>=1.0.0
```

## Usage Instructions

### 1. Quick Start
```bash
# Run model evaluation
python evaluate_models.py

# Start Jupyter notebook
jupyter notebook
```

### 2. Running Individual Models
Navigate to each model directory and open the respective notebook:
- `CNN/cnn-model-and-plot.ipynb`
- `ResNet50/resnet50-model-and-plot.ipynb`
- `MobileNetV2/mobilenetv2-model-and-plot.ipynb`
- `EfficientNetB0/efficientnetb0-model-and-plot.ipynb`

### 3. Comparative Analysis
Open `All Models Combined/all-models-combined-plots.ipynb` for comprehensive comparison.

### 4. Custom Training
To train with your own data:
1. Organize data in the required directory structure
2. Update data paths in the notebooks
3. Adjust hyperparameters as needed
4. Run the training cells

## Results Analysis

### Key Findings
1. **EfficientNetB0** achieved the best overall performance (54.17% accuracy)
2. **Image size 128x128** was optimal for most models
3. **Training time** varied significantly across architectures
4. **AUC scores** showed EfficientNetB0's superior discrimination ability

### Performance Metrics
- **Accuracy**: Classification accuracy on test set
- **Training Time**: Time to complete training epochs
- **AUC**: Area Under ROC Curve for model discrimination
- **Confusion Matrix**: Detailed classification breakdown

### Model Recommendations
- **Production Use**: EfficientNetB0 for best accuracy
- **Real-time Applications**: CNN for fastest inference
- **Mobile Deployment**: MobileNetV2 for resource constraints
- **Research**: ResNet50 for baseline comparisons

## Troubleshooting

### Common Issues

#### 1. Memory Errors
```bash
# Reduce batch size in notebooks
batch_size = 16  # instead of 32

# Or use smaller image size
img_size = 128  # instead of 256
```

#### 2. GPU Not Detected
```python
# Check GPU availability
import tensorflow as tf
print("GPU Available: ", tf.config.list_physical_devices('GPU'))

# Force CPU usage if needed
tf.config.set_visible_devices([], 'GPU')
```

#### 3. Package Import Errors
```bash
# Reinstall packages
pip uninstall tensorflow
pip install tensorflow

# Check versions
pip list | grep tensorflow
```

#### 4. Jupyter Kernel Issues
```bash
# Install kernel
python -m ipykernel install --user --name traffic_env

# Or restart kernel in Jupyter
# Kernel -> Restart & Clear Output
```

### Performance Tips

1. **Use GPU**: Significantly faster training
2. **Batch Size**: Adjust based on available memory
3. **Early Stopping**: Prevent overfitting
4. **Data Augmentation**: Improve generalization

### Getting Help

1. Check existing issues in the repository
2. Review error messages carefully
3. Verify all dependencies are installed
4. Try running on a smaller dataset first

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Code style
- Pull request process
- Testing requirements
- Documentation standards

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.
