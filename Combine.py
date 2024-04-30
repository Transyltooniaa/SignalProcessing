import os
import pandas as pd

# Define the absolute path of the Excl folder
excl_folder = "/Users/ajiteshkumarsingh/Documents/Semester 4/Signal Processing/Project/Output"

# Define the folder structure
folders = ["25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]
sub_folders = ["DataFor1", "DataFor2"]

# Create a new folder for combined data
new_folder = "/Users/ajiteshkumarsingh/Documents/Semester 4/Signal Processing/Project/CombinedData"
os.makedirs(new_folder, exist_ok=True)

# Iterate through each sub-folder
for sub_folder in sub_folders:
    sub_folder_path = os.path.join(new_folder, sub_folder)
    os.makedirs(sub_folder_path, exist_ok=True)
    
    # Iterate through each file index
    for i in range(7):
        combined_data = pd.DataFrame()  # Initialize an empty DataFrame for combining data
        
        # Iterate through each folder
        for folder in folders:
            folder_path = os.path.join(excl_folder, folder, sub_folder)
            file_path = os.path.join(folder_path, f"{i}.txt")
            
            # Check if file exists
            if os.path.exists(file_path):
                print(f"Reading data from: {file_path}")
                # Read Excel file and append to combined data
                data = pd.read_excel(file_path)
                print("Data read successfully:")
                print(data.head())  # Print the first few rows of data for verification
                combined_data = pd.concat([combined_data, data], ignore_index=True)
        
       
        # Save combined data to a new text file
        combined_file_path = os.path.join(sub_folder_path, f"{i}.txt")
        try:
            combined_data.to_csv(combined_file_path, sep='\t', index=False)
            print(f"Combined data saved to: {combined_file_path}")
        except Exception as e:
            print(f"Error occurred while saving combined data: {e}")
            
print("Combined data creation completed successfully!")
