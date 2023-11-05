import pandas as pd

# Load your Excel file
excel_file = 'your_data.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(excel_file)

# Split the data into training, testing, and validation datasets
# You can adjust the split ratios as needed (e.g., 0.6 for 60% training, 0.2 for 20% testing, 0.2 for 20% validation)
train_ratio = 0.6
test_ratio = 0.2
valid_ratio = 0.2

# Randomly shuffle the data
df = df.sample(frac=1).reset_index(drop=True)

# Split the data
train_size = int(train_ratio * len(df))
test_size = int(test_ratio * len(df))
valid_size = int(valid_ratio * len(df))

train_data = df[:train_size]
test_data = df[train_size:(train_size + test_size)]
valid_data = df[(train_size + test_size):(train_size + test_size + valid_size)]

# Create an Excel writer object
excel_writer = pd.ExcelWriter('output_data.xlsx', engine='xlsxwriter')

# Save training, testing, and validation datasets as separate worksheets in the Excel file
train_data.to_excel(excel_writer, sheet_name='Train Data', index=False)
test_data.to_excel(excel_writer, sheet_name='Test Data', index=False)
valid_data.to_excel(excel_writer, sheet_name='Validation Data', index=False)

# Save the Excel file
excel_writer.save()

print("Training, testing, and validation datasets saved in 'output_data.xlsx'.")
##########################################################################################
##########################################################################################

import os
import random
import shutil

# Define the paths
input_folder = 'your_image_folder'  # Replace with the path to your image folder
output_folder = 'output_image_folder'  # Replace with the path where you want to save the split datasets
train_ratio = 0.8  # Adjust the training set ratio (e.g., 0.8 for 80% training, 0.2 for 20% testing)

# Create the output folders for train and test datasets
os.makedirs(os.path.join(output_folder, 'train'), exist_ok=True)
os.makedirs(os.path.join(output_folder, 'test'), exist_ok=True)

# List all image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.png', '.jpeg', '.gif'))]

# Shuffle the list of image files randomly
random.shuffle(image_files)

# Calculate the number of files for each set
num_images = len(image_files)
train_size = int(num_images * train_ratio)

# Copy files to the respective sets
for i, file in enumerate(image_files):
    if i < train_size:
        shutil.copy(os.path.join(input_folder, file), os.path.join(output_folder, 'train', file))
    else:
        shutil.copy(os.path.join(input_folder, file), os.path.join(output_folder, 'test', file))

print("Image dataset split into training and testing sets.")
