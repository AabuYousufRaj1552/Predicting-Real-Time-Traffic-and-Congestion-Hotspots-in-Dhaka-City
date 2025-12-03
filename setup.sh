#!/bin/bash

# Setup script for Traffic Prediction Project
# This script installs all required dependencies and sets up the environment

echo "🚗 Setting up Traffic Prediction Project Environment"
echo "=================================================="

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "🐍 Python version:"
python --version

# Check if pip is available
if ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Please install pip first."
    exit 1
fi

echo "📦 Installing required packages..."

# Install dependencies
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ All packages installed successfully!"
else
    echo "❌ Failed to install some packages. Please check the error messages above."
    exit 1
fi

# Check if Jupyter is working
echo "🔧 Setting up Jupyter environment..."
python -c "import jupyter" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "✅ Jupyter is ready!"
else
    echo "⚠️  Jupyter installation may have issues. Try running: pip install jupyter"
fi

# Create results directory if it doesn't exist
if [ ! -d "results" ]; then
    mkdir results
    echo "📁 Created results directory"
fi

echo ""
echo "🎉 Setup complete! You can now:"
echo "   1. Download dataset: python download_dataset.py"
echo "   2. Open Jupyter notebooks: jupyter notebook"
echo "   3. Run model evaluation: python evaluate_models.py"
echo "   4. Explore individual model directories (CNN, ResNet50, MobileNetV2, EfficientNetB0)"
echo "   5. Read the research paper: Publication/compiled/Predicting*.pdf"
echo ""
echo "📊 Dataset: https://www.kaggle.com/datasets/mdromanbinjalal/dhaka-traffic-classification-4-levels"
echo "📚 To get started:"
echo "   - Check the README.md for detailed instructions"
echo "   - Read the research paper in Publication/ directory"
echo "   - Start with the 'All Models Combined' directory for overview"
echo "   - Run individual model notebooks in their respective directories"
echo "   - All models use the Dhaka traffic dataset with 4 congestion levels"
