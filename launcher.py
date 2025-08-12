"""
Simple launcher script for the Radar Chart Generator.
Run this script to interactively create radar charts.
"""

import os
import sys
from radar_chart_generator import RadarChartGenerator


def main():
    """Interactive launcher for the radar chart generator."""
    print("🎯 Radar Chart Generator")
    print("=" * 50)
    print("This tool creates radar charts from CSV data where:")
    print("• Each row = student (different colored lines)")
    print("• Each column = subject (angles on the radar)")
    print()
    
    while True:
        print("Options:")
        print("1. Use sample data")
        print("2. Load from CSV file")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            # Use sample data
            print("\n📊 Using sample data...")
            generator = RadarChartGenerator()
            generator.print_data_summary()
            
            title = input("\nEnter chart title (or press Enter for default): ").strip()
            if not title:
                title = "Student Performance Radar Chart"
            
            filename = input("Enter output filename (or press Enter for 'radar_chart.png'): ").strip()
            if not filename:
                filename = "radar_chart.png"
            
            generator.generate_chart(title=title, save_path=filename, show=True)
            print(f"✅ Chart saved as '{filename}'")
            
        elif choice == "2":
            # Load from CSV
            csv_file = input("\n📁 Enter CSV file path: ").strip()
            
            if not os.path.exists(csv_file):
                print(f"❌ Error: File '{csv_file}' not found.")
                continue
            
            try:
                generator = RadarChartGenerator(csv_file)
                generator.print_data_summary()
                
                title = input("\nEnter chart title (or press Enter for default): ").strip()
                if not title:
                    title = "Student Performance Radar Chart"
                
                filename = input("Enter output filename (or press Enter for 'radar_chart.png'): ").strip()
                if not filename:
                    filename = "radar_chart.png"
                
                generator.generate_chart(title=title, save_path=filename, show=True)
                print(f"✅ Chart saved as '{filename}'")
                
            except Exception as e:
                print(f"❌ Error processing file: {e}")
                
        elif choice == "3":
            print("\n👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
        
        print("\n" + "-" * 50)


if __name__ == "__main__":
    main()
