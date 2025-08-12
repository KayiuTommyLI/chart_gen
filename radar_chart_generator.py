"""
Radar Chart Generator
====================

This script generates radar charts from CSV data where:
- Columns represent subjects (angles on the radar chart)
- Rows represent students (different colored lines)

Usage:
    python radar_chart_generator.py [csv_file]

If no CSV file is provided, it will use the sample data.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from math import pi


class RadarChartGenerator:
    def __init__(self, csv_file=None):
        """Initialize the radar chart generator with data from CSV file."""
        if csv_file and os.path.exists(csv_file):
            self.data = pd.read_csv(csv_file, index_col=0)
        else:
            # Use sample data if no file provided
            self.data = self._create_sample_data()
        
        self.subjects = list(self.data.columns)
        self.students = list(self.data.index)
        
    def _create_sample_data(self):
        """Create sample student performance data."""
        subjects = ['Math', 'English', 'Chinese', 'Science', 'History', 'Art']
        students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
        
        # Generate sample scores (0-100)
        np.random.seed(42)  # For reproducible results
        data = np.random.randint(60, 100, size=(len(students), len(subjects)))
        
        return pd.DataFrame(data, index=students, columns=subjects)
    
    def generate_chart(self, title="Student Performance Radar Chart", 
                      save_path=None, show=True, figsize=(10, 8)):
        """
        Generate and display/save the radar chart.
        
        Args:
            title (str): Chart title
            save_path (str): Path to save the chart (optional)
            show (bool): Whether to display the chart
            figsize (tuple): Figure size (width, height)
        """
        # Number of variables (subjects)
        num_vars = len(self.subjects)
        
        # Calculate angles for each subject
        angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
        angles += angles[:1]  # Complete the circle
        
        # Create the plot
        fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(projection='polar'))
        
        # Colors for different students
        colors = plt.cm.Set3(np.linspace(0, 1, len(self.students)))
        
        # Plot data for each student
        for i, student in enumerate(self.students):
            values = self.data.loc[student].tolist()
            values += values[:1]  # Complete the circle
            
            ax.plot(angles, values, 'o-', linewidth=2, 
                   label=student, color=colors[i])
            ax.fill(angles, values, alpha=0.25, color=colors[i])
        
        # Customize the chart
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(self.subjects)
        ax.set_ylim(0, 100)
        
        # Add grid lines
        ax.set_yticks([20, 40, 60, 80, 100])
        ax.set_yticklabels(['20', '40', '60', '80', '100'])
        ax.grid(True)
        
        # Add title and legend
        plt.title(title, size=16, fontweight='bold', pad=20)
        plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
        
        # Adjust layout
        plt.tight_layout()
        
        # Save if path provided
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Chart saved to: {save_path}")
        
        # Display if requested
        if show:
            plt.show()
        
        return fig, ax
    
    def print_data_summary(self):
        """Print a summary of the loaded data."""
        print("Data Summary:")
        print("=" * 50)
        print(f"Number of students: {len(self.students)}")
        print(f"Number of subjects: {len(self.subjects)}")
        print(f"Subjects: {', '.join(self.subjects)}")
        print(f"Students: {', '.join(self.students)}")
        print("\nData preview:")
        print(self.data.head())
        print("\nData statistics:")
        print(self.data.describe())


def main():
    """Main function to run the radar chart generator."""
    # Check for command line arguments
    csv_file = None
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
        if not os.path.exists(csv_file):
            print(f"Error: File '{csv_file}' not found.")
            return
    
    # Create the radar chart generator
    generator = RadarChartGenerator(csv_file)
    
    # Print data summary
    generator.print_data_summary()
    
    # Generate and display the chart
    print("\nGenerating radar chart...")
    generator.generate_chart(
        title="Student Performance Radar Chart",
        save_path="radar_chart.png"
    )


if __name__ == "__main__":
    main()
