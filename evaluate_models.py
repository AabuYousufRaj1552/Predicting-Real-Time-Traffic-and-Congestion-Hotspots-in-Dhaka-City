#!/usr/bin/env python3
"""
Model Evaluation Script for Traffic Prediction Models
Analyzes and compares results from all trained models.
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import numpy as np

class ModelEvaluator:
    def __init__(self, json_dir="JSON Files"):
        """Initialize the model evaluator with path to JSON results."""
        self.json_dir = Path(json_dir)
        self.models = ["CNN", "ResNet50", "MobileNetV2", "EfficientNetB0"]
        self.image_sizes = [128, 256, 512]
        self.results = {}
        
    def load_results(self):
        """Load all model results from JSON files."""
        for model in self.models:
            self.results[model] = {}
            for size in self.image_sizes:
                file_path = self.json_dir / f"{model}_Results_{size}.json"
                if file_path.exists():
                    with open(file_path, 'r') as f:
                        self.results[model][size] = json.load(f)
                else:
                    print(f"Warning: {file_path} not found")
    
    def get_summary_table(self):
        """Generate a summary table of all model results."""
        data = []
        for model in self.models:
            for size in self.image_sizes:
                if model in self.results and size in self.results[model]:
                    result = self.results[model][size]
                    data.append({
                        'Model': model,
                        'Image_Size': f"{size}x{size}",
                        'Accuracy': result['accuracy'],
                        'Training_Time': result['training_time'],
                        'Epochs': result['epochs'],
                        'AUC': result['roc_curve']['auc']
                    })
        
        return pd.DataFrame(data)
    
    def plot_model_comparison(self):
        """Create comparison plots for all models."""
        df = self.get_summary_table()
        
        # Set up the plotting style
        plt.style.use('default')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # Accuracy comparison
        accuracy_pivot = df.pivot(index='Model', columns='Image_Size', values='Accuracy')
        accuracy_pivot.plot(kind='bar', ax=axes[0,0], color=['skyblue', 'lightgreen', 'salmon'])
        axes[0,0].set_title('Model Accuracy by Image Size')
        axes[0,0].set_ylabel('Accuracy (%)')
        axes[0,0].legend(title='Image Size')
        axes[0,0].tick_params(axis='x', rotation=45)
        
        # Training time comparison
        time_pivot = df.pivot(index='Model', columns='Image_Size', values='Training_Time')
        time_pivot.plot(kind='bar', ax=axes[0,1], color=['skyblue', 'lightgreen', 'salmon'])
        axes[0,1].set_title('Training Time by Image Size')
        axes[0,1].set_ylabel('Training Time (seconds)')
        axes[0,1].legend(title='Image Size')
        axes[0,1].tick_params(axis='x', rotation=45)
        
        # AUC comparison
        auc_pivot = df.pivot(index='Model', columns='Image_Size', values='AUC')
        auc_pivot.plot(kind='bar', ax=axes[1,0], color=['skyblue', 'lightgreen', 'salmon'])
        axes[1,0].set_title('AUC Score by Image Size')
        axes[1,0].set_ylabel('AUC Score')
        axes[1,0].legend(title='Image Size')
        axes[1,0].tick_params(axis='x', rotation=45)
        
        # Accuracy vs Training Time scatter
        for size in self.image_sizes:
            size_data = df[df['Image_Size'] == f"{size}x{size}"]
            axes[1,1].scatter(size_data['Training_Time'], size_data['Accuracy'], 
                            label=f"{size}x{size}", s=100, alpha=0.7)
            
            # Add model labels
            for _, row in size_data.iterrows():
                axes[1,1].annotate(row['Model'], 
                                 (row['Training_Time'], row['Accuracy']),
                                 xytext=(5, 5), textcoords='offset points', fontsize=8)
        
        axes[1,1].set_title('Accuracy vs Training Time')
        axes[1,1].set_xlabel('Training Time (seconds)')
        axes[1,1].set_ylabel('Accuracy (%)')
        axes[1,1].legend(title='Image Size')
        axes[1,1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('model_comparison_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def get_best_models(self):
        """Identify the best performing models by different metrics."""
        df = self.get_summary_table()
        
        best_accuracy = df.loc[df['Accuracy'].idxmax()]
        best_efficiency = df.loc[df['Training_Time'].idxmin()]
        best_auc = df.loc[df['AUC'].idxmax()]
        
        # Calculate efficiency score (accuracy per training time)
        df['Efficiency_Score'] = df['Accuracy'] / df['Training_Time']
        best_efficiency_score = df.loc[df['Efficiency_Score'].idxmax()]
        
        print("=== BEST PERFORMING MODELS ===\n")
        print(f"🏆 Highest Accuracy: {best_accuracy['Model']} ({best_accuracy['Image_Size']}) - {best_accuracy['Accuracy']:.2f}%")
        print(f"⚡ Fastest Training: {best_efficiency['Model']} ({best_efficiency['Image_Size']}) - {best_efficiency['Training_Time']:.1f}s")
        print(f"📈 Highest AUC: {best_auc['Model']} ({best_auc['Image_Size']}) - {best_auc['AUC']:.3f}")
        print(f"🎯 Best Efficiency: {best_efficiency_score['Model']} ({best_efficiency_score['Image_Size']}) - {best_efficiency_score['Efficiency_Score']:.4f} acc/sec")
        
        return {
            'best_accuracy': best_accuracy,
            'fastest_training': best_efficiency,
            'best_auc': best_auc,
            'best_efficiency': best_efficiency_score
        }
    
    def export_results(self):
        """Export results to CSV for further analysis."""
        df = self.get_summary_table()
        df.to_csv('model_evaluation_results.csv', index=False)
        print("\n📊 Results exported to 'model_evaluation_results.csv'")

def main():
    """Main function to run model evaluation."""
    print("🚗 Traffic Prediction Model Evaluation")
    print("=" * 50)
    
    evaluator = ModelEvaluator()
    evaluator.load_results()
    
    # Generate summary
    df = evaluator.get_summary_table()
    print("\n📋 Model Results Summary:")
    print(df.to_string(index=False))
    
    # Find best models
    best_models = evaluator.get_best_models()
    
    # Create comparison plots
    print("\n📈 Generating comparison plots...")
    evaluator.plot_model_comparison()
    
    # Export results
    evaluator.export_results()
    
    print("\n✅ Evaluation complete!")

if __name__ == "__main__":
    main()
