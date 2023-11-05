##splitting the excel File in training and testing sets for the Model

import pandas as pd

# Load your Excel file
excel_file = 'your_data.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(excel_file)

# Split the data into training and testing datasets
# You can adjust the split ratio as needed (e.g., 0.8 for 80% training, 0.2 for 20% testing)
train_ratio = 0.8
test_ratio = 1 - train_ratio

# Randomly shuffle the data
df = df.sample(frac=1).reset_index(drop=True)

# Split the data
train_size = int(train_ratio * len(df))
train_data = df[:train_size]
test_data = df[train_size:]

# Save the training and testing datasets as CSV files
train_data.to_csv('train_data.csv', index=False)
test_data.to_csv('test_data.csv', index=False)

print("Training and testing datasets saved as 'train_data.csv' and 'test_data.csv'.")



#####################################
#########################################33

## Give the Output in the form of excel 


import pandas as pd

# Load your Excel file
excel_file = 'your_data.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(excel_file)

# Split the data into training and testing datasets
# You can adjust the split ratio as needed (e.g., 0.8 for 80% training, 0.2 for 20% testing)
train_ratio = 0.8
test_ratio = 1 - train_ratio

# Randomly shuffle the data
df = df.sample(frac=1).reset_index(drop=True)

# Split the data
train_size = int(train_ratio * len(df))
train_data = df[:train_size]
test_data = df[train_size:]

# Create an Excel writer object
excel_writer = pd.ExcelWriter('output_data.xlsx', engine='xlsxwriter')

# Save training and testing datasets as separate worksheets in the Excel file
train_data.to_excel(excel_writer, sheet_name='Train Data', index=False)
test_data.to_excel(excel_writer, sheet_name='Test Data', index=False)

# Save the Excel file
excel_writer.save()

print("Training and testing datasets saved in 'output_data.xlsx'.")
