"""
Demo script showing how to generate individual radar charts for each student.
"""

from radar_chart_generator import RadarChartGenerator

def main():
    # Create generator with sample data (or specify a CSV file)
    generator = RadarChartGenerator()  # Uses sample data
    # generator = RadarChartGenerator('your_data.csv')  # Or use your own CSV
    
    print("=== Individual Charts Demo ===")
    
    # Method 1: Generate all individual charts at once
    print("\n1. Generating all individual charts...")
    generator.generate_all_individual_charts(output_dir="demo_charts", show=False)
    
    # Method 2: Generate a chart for a specific student
    print("\n2. Generating chart for a specific student...")
    student_name = generator.students[0]  # Get first student
    generator.generate_individual_chart(
        student_name=student_name,
        save_path=f"{student_name}_special_chart.png",
        show=False
    )
    
    # Method 3: Generate combined chart for comparison
    print("\n3. Generating combined chart for comparison...")
    generator.generate_chart(
        title="All Students - Combined View",
        save_path="demo_combined_chart.png",
        show=False
    )
    
    print("\nDemo completed! Check the generated files:")
    print("- Individual charts in 'demo_charts/' directory")
    print("- Special chart: '{}_special_chart.png'".format(student_name))
    print("- Combined chart: 'demo_combined_chart.png'")

if __name__ == "__main__":
    main()
