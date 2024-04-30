import os

def extract_mean(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
      
        val1 = float(lines[16])
        val2 = float(lines[17])
        val3 = float(lines[18])
        val4 = float(lines[19])

    return [val1, val2, val3, val4]

def main():
    folder_path = "/Users/ajiteshkumarsingh/Documents/Semester 4/Signal Processing/Project/25-36 plot and stat/OutputResults_6-9"
    data_folders1 = []
    data_folders2 = []

    # Search for folders containing "DataFor1" and "DataFor2" in their names
    for folder_name in os.listdir(folder_path):
        if "DataFor1" in folder_name:
            data_folders1.append(folder_name)
        elif "DataFor2" in folder_name:
            data_folders2.append(folder_name)
            

    className1 = [[], [], [], [] , [], [], []]


    for folder in data_folders1:
        output_file = os.path.join(folder_path, f'{folder}_mean_time_domain.txt')
        
        

        for i in range(7):
            file_path = os.path.join(folder_path, folder, f'Results_{i}.txt')
            val = extract_mean(file_path)
            className1[i].append(val)


    className2 = [[], [], [], [] , [], [], []]
    for folder in data_folders2:
        output_file = os.path.join(folder_path, f'{folder}_mean_time_domain.txt')   
        for i in range(7):
            file_path = os.path.join(folder_path, folder, f'Results_{i}.txt')
            val = extract_mean(file_path)
            className2[i].append(val)
        
    
    MeanClass1 = []

    for i in className1:
        means = [sum(col) / len(col) for col in zip(*i)]
        MeanClass1.append(means)

    MeanClass2 = []

    for i in className2:
        means = [sum(col) / len(col) for col in zip(*i)]
        MeanClass2.append(means)


    with open('MeanClass1.txt', 'w') as file:
        file.write('DATA FOR CLASS 1\n')

        num = 0
        for i in MeanClass1:
            file.write(f'class {num}:')
            file.write(f'{i}\n\n')
            num += 1



    with open('MeanClass2.txt', 'w') as file:
        file.write('DATA FOR CLASS 2\n')
        
        num = 0
        for i in MeanClass2:
            file.write(f'class {num}:')
            file.write(f'{i}\n\n')
            num += 1




if __name__ == "__main__":
    main()
