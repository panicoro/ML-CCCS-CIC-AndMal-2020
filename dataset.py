import zipfile
import os
import glob
import pandas as pd

def merge_csv_files(input_folder, output_file):
    # List all CSV files in the input folder
    csv_files = glob.glob(os.path.join(input_folder, '*.csv'))
    #print(csv_files)
    # Initialize an empty DataFrame to store the merged data
    all_data = []
    
    # Read each CSV file and append its data to the merged DataFrame
    for csv_file in csv_files:
        data = pd.read_csv(csv_file)
        all_data.append(data)
    
    # Concatenate all DataFrames in the list into one DataFrame
    merged_data = pd.concat(all_data)
    
    # Write the merged data to a single CSV file
    merged_data.to_csv(output_file, index=False)
    print(f'Merged data saved to {output_file}')


def extract_zip(archivo_zip):
    # Extract the zip file
    with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
        # Extract all contents
        zip_ref.extractall()
        # List all the .csv files in the 
        input_folder = zip_ref.namelist()[0]
        csv_files = sorted([name for name in zip_ref.namelist() if '.csv' in name])
        print("The following files were extracted:\n")
        for file in csv_files:
            # Print the name of the csv files
            filename = file.split('/', 1)[1]
            print("\t*", filename)
        
        # Output file path for the merged CSV
        output_file = 'full-dataset-CCCS-CIC-AndMal-2020.csv'

        # Call the function to merge CSV files
        merge_csv_files(input_folder, output_file)            
          

def main():
  # Name of .zip file
  archivo_zip = 'AndMal2020-Dynamic-BeforeAndAfterReboot.zip'
  # extrar
  extract_zip(archivo_zip)
  
if __name__ == "__main__":
    main()
