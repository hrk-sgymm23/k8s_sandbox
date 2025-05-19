import csv
import time
import random
import modules.storage_fetcher

def read_csv(file_path):
   with open(file_path, 'r') as f:
       reader = csv.reader(f)
       data = [row for row in reader]
   return data

def write_csv(file_path, data):
   with open(file_path, 'w', newline='') as f:
       writer = csv.writer(f)
       writer.writerows(data)

def process_data(data):
   processed_data = [["ID", "Value", "ProcessedValue"]]
   for row in data[1:]:
       id, value = row
       processed_value = float(value) * random.uniform(0.8, 1.2)
       processed_data.append([id, value, processed_value])
   return processed_data

def batch_task():
   print("Starting batch task...")
  
   # Read data from CSV
   input_data = read_csv('input.csv')
  
   # Process data
   processed_data = process_data(input_data)
  
   # Write processed data to CSV
   write_csv('output.csv', processed_data)
  
   print("Batch task completed.")

if __name__ == "__main__":
   batch_task()