
# Data Flags
flags = {
    "class_0": 0,
    "class_1": 0,
    "class_2": 0,
    "class_3": 0,
    "class_4": 0,
    "class_5": 0,
    "class_6": 0
}


TestCase = 9
movement = 5


if(TestCase <= 12):
    subfolder = "1_12"

elif(TestCase >= 13 and TestCase <= 24):
    subfolder = "13_24"

elif(TestCase >= 25 and TestCase <= 36):
    subfolder = "25_36"



# Path to the folder containing the data
folderPath = f"/Users/ajiteshkumarsingh/Documents/Semester 4/Signal Processing/Project/PlotAndStats/{subfolder}/OutputResults_2-5/DataFor{TestCase}_DataFor1_Results"
folderPath2 = f"/Users/ajiteshkumarsingh/Documents/Semester 4/Signal Processing/Project/PlotAndStats/{subfolder}/OutputResults_6-9/DataFor{TestCase}_DataFor1_Results"

# Load the data
f = open(f"{folderPath}/Results_{movement}.txt", "r")
data1 = f.read().split("\n")

f = open(f"{folderPath2}/Results_{movement}.txt", "r")
data2 = f.read().split("\n")

# Extract the required data


amplitude_spectrum1 = int (data1.index("Mean of amplitude spectrum: "))
amplitude_spectrum2 = int (data2.index("Mean of amplitude spectrum: "))

amplitude_spectrum2_5 = [float(data1[amplitude_spectrum1 + i]) for i in range(1, 5)]
amplitude_spectrum6_9 = [float(data2[amplitude_spectrum2 + i]) for i in range(1, 5)]

amplitude_spectrum = amplitude_spectrum2_5 + amplitude_spectrum6_9



kurtIndex1 = int(data1.index("Kurtosis in time domain: "))
kurtIndex2 = int(data2.index("Kurtosis in time domain: "))

Kurtosis2_5 = [float(data1[kurtIndex1 + i]) for i in range(1, 5)]
Kurtosis6_9 = [float(data2[kurtIndex2 + i]) for i in range(1, 5)]

Kurtosis = Kurtosis2_5 + Kurtosis6_9



peak_freq1 = int(data1.index("Peak frequency (excluding 0 frequency component): "))
peak_freq2 = int(data2.index("Peak frequency (excluding 0 frequency component): "))

peak_freq2_5 = [float(data1[peak_freq1 + i]) for i in range(1, 5)]
peak_freq6_9 = [float(data2[peak_freq2 + i]) for i in range(1, 5)]

peak_freq = peak_freq2_5 + peak_freq6_9



# Flag 0: Highest probability
if all(i > 6 for i in Kurtosis):
    flags["class_0"] += 1

# Flag 1: Condition based on amplitude spectrum
if abs(amplitude_spectrum[-2] * 1e6) < 1000:
    flags["class_1"] += 1

# Flag 5: Multiple conditions
if all(abs(amplitude_spectrum[i] - 0.002) < 0.002 for i in range(4)):
    flags["class_5"] += 1

# Flag 5: Another condition
if sum(Kurtosis[i] - [4, 3, 4, 5][i] for i in range(-1, -5, -1)) < 2.4:
    flags["class_5"] += 1

# Flag 4: Condition based on peak frequency
if sum(i >= 10 or abs(i - 10) < 0.5 for i in peak_freq) > 5:
    flags["class_4"] += 1


# Flag 4: Another condition based on peak frequency
if amplitude_spectrum.index(max(amplitude_spectrum[:4])) == 3 and amplitude_spectrum.index(min(amplitude_spectrum[4:8])) == 4:
    flags["class_4"] += 1 


# Flag 2: Condition based on amplitude spectrum
if amplitude_spectrum.index(max(amplitude_spectrum[:4])) in [0, 3]:
    flags["class_2"] += 1


# Flag 6: Condition based on amplitude spectrum
if amplitude_spectrum.index(min(amplitude_spectrum[:4])) in [1, 2]:
    flags["class_6"] += 1


if amplitude_spectrum.index(max(amplitude_spectrum[:4])) != 3 and amplitude_spectrum.index(min(amplitude_spectrum[4:8])) != 6:
    flags["class_3"] += 1 

# Define flag priority according to the specified order
flag_priority = [
    ("class_0", 0),
    ("class_1", 1),
    ("class_5", 3),
    ("class_4", 5),
    ["class_3", 2],
    ("class_6", 4),
    ("class_2", 6)
]

# Sort the flag_priority list based on the specified order
flag_priority.sort(key=lambda x: x[1])


# Define flag names
flag_names = {
    "class_0": "Class 0",
    "class_1": "Class 1",
    "class_2": "Class 2",
    "class_3": "Class 3",
    "class_4": "Class 4",
    "class_5": "Class 5",
    "class_6": "Class 6"
}

print("\n")
print("The predicted order of their priority is : ")

l = []
for flag_name, _ in flag_priority:
    if flags[flag_name] == 1:
        l.append(flag_names[flag_name])


names = list(flag_names.values())
if len(l) == 2 and l[0] == names[6] and l[1] == names[2]:
    l.clear()
    l.append(names[5])
    l.append(names[6])

        

final_priority = []
for i in l:
    final_priority.append(i)
    print(i," > " ,end = " ")



print("\n")
