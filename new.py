import os

# Function to combine data from Excel files and write to text files
def combine_data(source_dir, dest_dir):
    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    
    for i in range(7):  # Assuming 7 files: 0.xlsx to 6.xlsx
        data_for1 = ""
        data_for2 = ""
        
        for folder_name in range(25, 37):  # Folders 25 to 36
            folder_path = os.path.join(source_dir, str(folder_name))
            data_for1_file = os.path.join(folder_path, "DataFor1", f"{i}.txt")
            data_for2_file = os.path.join(folder_path, "DataFor2", f"{i}.txt")
            print(f"Reading data from: {data_for1_file} and {data_for2_file}")
            
            # Read data from Excel files and append to respective variables
            with open(data_for1_file, 'r') as file:
                data_for1 += file.read()

            with open(data_for2_file, 'r') as file:
                data_for2 += file.read()

        
        # Write combined data to text files
        with open(os.path.join(dest_dir, "DataFor1", f"{i}.txt"), "a") as f:
            f.write(data_for1)
        with open(os.path.join(dest_dir, "DataFor2", f"{i}.txt"), "a") as f:
            f.write(data_for2)

# Example usage:
source_directory = "/Users/ajiteshkumarsingh/Documents/Semester 4/Signal Processing/Project/Output"
destination_directory = "/Users/ajiteshkumarsingh/Documents/Semester 4/Signal Processing/Project/CombinedData"
combine_data(source_directory, destination_directory)
