import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def process_files(folder_path, folder_path_destination , n):
    outputMap = {
        "0": "0.txt",
        "1": "1.txt",
        "2": "2.txt",
        "3": "3.txt",
        "4": "4.txt",
        "5": "5.txt",
        "6": "6.txt",
        "7": "7.txt",
    }

    if not os.path.exists(folder_path):
        print("Folder path does not exist.")
        return

    create_directory(folder_path_destination)


    for root, dirs, files in os.walk(folder_path):

        for folder in dirs:

            if(n==0):
                break

            n = n-1
            folder_name = os.path.join(root, folder)

            for filename in os.listdir(folder_name):

                if filename == ".DS_Store":
                    continue
                
                print("Processing file:", filename + " in folder:", folder)
                
                with open(os.path.join(folder_name, filename), 'r') as file:
                    for line in file:
                        line = line.strip()
                        class_name = line[-1]
                        output_file = ""

                        if class_name in outputMap:
                            output_file = outputMap[class_name]


                            create_directory(os.path.join(folder_path_destination,folder, "DataFor1"))
                            create_directory(os.path.join(folder_path_destination,folder, "DataFor2"))

                            output_location = ""
                            if filename.startswith("1"):
                                output_location = os.path.join(folder_path_destination, folder , "DataFor1", output_file)
                            elif filename.startswith("2"):
                                output_location = os.path.join(folder_path_destination, folder , "DataFor2", output_file)

                            if output_location:
                                with open(output_location, 'a') as f:
                                    f.write(line + "\n")

    print("Data sorted successfully.")



# TODO: Change the folder path
folder_path = "/Users/ajiteshkumarsingh/Documents/Semester 4/Signal Processing/Project/EMG_data_for_gestures-master"
folder_path_destination = "/Users/ajiteshkumarsingh/Documents/Semester 4/Signal Processing/Project/Output"

n = int(input("Enter the number of folders you want sammple of : "))

process_files(folder_path, folder_path_destination,n)
