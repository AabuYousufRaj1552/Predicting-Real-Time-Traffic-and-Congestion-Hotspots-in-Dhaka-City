#!/usr/bin/env python3
"""
Download and setup the Dhaka Traffic Dataset from Kaggle
"""

import os
import subprocess
import zipfile
from pathlib import Path

def download_dataset():
    """Download the dataset from Kaggle and extract it."""
    
    print("🚗 Dhaka Traffic Dataset Downloader")
    print("=" * 50)
    
    # Check if kaggle is installed
    try:
        import kaggle
        print("✅ Kaggle API found")
    except ImportError:
        print("❌ Kaggle API not found. Installing...")
        subprocess.run(["pip", "install", "kaggle"], check=True)
        print("✅ Kaggle API installed")
    
    # Check for Kaggle credentials
    kaggle_config = Path.home() / ".kaggle" / "kaggle.json"
    if not kaggle_config.exists():
        print("❌ Kaggle credentials not found!")
        print("Please follow these steps:")
        print("1. Go to https://www.kaggle.com/account")
        print("2. Click 'Create New API Token'")
        print("3. Save kaggle.json to ~/.kaggle/")
        print("4. Run: chmod 600 ~/.kaggle/kaggle.json")
        return False
    
    # Create data directory
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Download dataset
    dataset_name = "mdromanbinjalal/dhaka-traffic-classification-4-levels"
    print(f"📥 Downloading dataset: {dataset_name}")
    
    try:
        # Download using kaggle API
        os.chdir("data")
        subprocess.run([
            "kaggle", "datasets", "download", 
            "-d", dataset_name,
            "--unzip"
        ], check=True)
        
        print("✅ Dataset downloaded and extracted successfully!")
        print(f"📁 Dataset location: {data_dir.absolute()}")
        
        # List the contents
        print("\n📋 Dataset structure:")
        for item in sorted(data_dir.rglob("*")):
            if item.is_dir():
                print(f"📁 {item.relative_to(data_dir)}/")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error downloading dataset: {e}")
        print("Please check:")
        print("1. Dataset name is correct")
        print("2. You have access to the dataset")
        print("3. Kaggle credentials are properly configured")
        return False
    
    finally:
        # Return to original directory
        os.chdir("..")

def verify_dataset():
    """Verify the dataset structure is correct."""
    data_dir = Path("data")
    
    expected_structure = [
        "Train/no traffic",
        "Train/light traffic", 
        "Train/moderate traffic",
        "Train/heavy traffic",
        "Test/no traffic",
        "Test/light traffic",
        "Test/moderate traffic", 
        "Test/heavy traffic"
    ]
    
    print("\n🔍 Verifying dataset structure...")
    
    missing = []
    for path in expected_structure:
        if not (data_dir / path).exists():
            missing.append(path)
    
    if missing:
        print("❌ Missing directories:")
        for path in missing:
            print(f"   - {path}")
        return False
    else:
        print("✅ Dataset structure verified!")
        
        # Count images in each category
        print("\n📊 Image counts:")
        for split in ["Train", "Test"]:
            print(f"\n{split}:")
            for category in ["no traffic", "light traffic", "moderate traffic", "heavy traffic"]:
                path = data_dir / split / category
                if path.exists():
                    count = len(list(path.glob("*")))
                    print(f"  {category}: {count} images")
        
        return True

if __name__ == "__main__":
    success = download_dataset()
    if success:
        verify_dataset()
        print("\n🎉 Dataset setup complete! You can now run the model training notebooks.")
    else:
        print("\n💡 Tip: You can also manually download from Kaggle and extract to the 'data/' folder")
