import pandas as pd
import os

# Current folder where this Python file is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# CSV file path
csv_path = os.path.join(current_folder, "student_dataset.csv")

print("Current Folder :", current_folder)
print("Looking for    :", csv_path)

# Check if the file exists
if not os.path.exists(csv_path):
    print("\nERROR: student_dataset.csv was not found.")
    print("Make sure the file is inside the same folder as data_processing.py")
    exit()

# Read the CSV file
data = pd.read_csv(csv_path)

# Display original dataset
print("\n========== ORIGINAL DATASET ==========")
print(data)

# Remove null values
clean_data = data.dropna()

# Display cleaned dataset
print("\n========== DATASET AFTER REMOVING NULL VALUES ==========")
print(clean_data)

# Count records
print("\n========== RECORD COUNT ==========")
print("Records before cleaning:", len(data))
print("Records after cleaning :", len(clean_data))

# Summary statistics
print("\n========== SUMMARY STATISTICS ==========")
print(clean_data.describe())

# Save cleaned dataset
clean_data.to_csv(os.path.join(current_folder, "cleaned_student_dataset.csv"), index=False)

print("\nCleaned dataset saved successfully!")