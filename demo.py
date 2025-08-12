"""
Demo script showing how to use the RadarChartGenerator programmatically.
"""

from radar_chart_generator import RadarChartGenerator
import pandas as pd

def demo_with_sample_data():
    """Demo using the built-in sample data."""
    print("=== Demo 1: Using Sample Data ===")
    
    # Create generator with sample data
    generator = RadarChartGenerator()
    
    # Show data summary
    generator.print_data_summary()
    
    # Generate chart
    generator.generate_chart(
        title="Sample Student Performance",
        save_path="demo_sample.png",
        show=False  # Don't show to avoid blocking in demos
    )
    
    print("Sample data chart saved as 'demo_sample.png'\n")


def demo_with_csv_data():
    """Demo using the provided CSV file."""
    print("=== Demo 2: Using CSV Data ===")
    
    # Create generator with CSV file
    generator = RadarChartGenerator("sample_data.csv")
    
    # Show data summary
    generator.print_data_summary()
    
    # Generate chart
    generator.generate_chart(
        title="Student Performance from CSV",
        save_path="demo_csv.png",
        show=False
    )
    
    print("CSV data chart saved as 'demo_csv.png'\n")


def demo_custom_data():
    """Demo creating custom data and generating chart."""
    print("=== Demo 3: Creating Custom Data ===")
    
    # Create custom data
    subjects = ['Programming', 'Algorithms', 'Databases', 'Web Dev', 'Mobile', 'AI/ML']
    students = ['John', 'Sarah', 'Mike', 'Lisa']
    
    # Custom scores
    data = [
        [90, 85, 80, 95, 70, 88],  # John
        [85, 92, 90, 85, 88, 95],  # Sarah
        [88, 80, 95, 90, 85, 82],  # Mike
        [92, 88, 85, 88, 90, 90]   # Lisa
    ]
    
    # Create DataFrame
    df = pd.DataFrame(data, index=students, columns=subjects)
    
    # Save as CSV for the generator
    df.to_csv("custom_data.csv")
    
    # Create generator with custom data
    generator = RadarChartGenerator("custom_data.csv")
    
    # Show data summary
    generator.print_data_summary()
    
    # Generate chart with custom styling
    generator.generate_chart(
        title="Programming Skills Assessment",
        save_path="demo_custom.png",
        show=False,
        figsize=(12, 10)
    )
    
    print("Custom data chart saved as 'demo_custom.png'\n")


def main():
    """Run all demos."""
    print("Radar Chart Generator - Demo Scripts")
    print("=" * 50)
    
    try:
        demo_with_sample_data()
        demo_with_csv_data()
        demo_custom_data()
        
        print("All demos completed successfully!")
        print("Check the generated PNG files to see the results.")
        
    except Exception as e:
        print(f"Demo failed with error: {e}")


if __name__ == "__main__":
    main()
