import csv
import time 
import os

# Local Testing -> True
# Build for Docker -> False
is_dev = False

DEV_CONFIG_FOLDER = "~/config_dockerized-python-with-cron-and-volume"
DOCKER_CONFIG_FOLDER = "/config"

if is_dev:
    DATA_FOLDER = DEV_CONFIG_FOLDER
else:
    DATA_FOLDER = DOCKER_CONFIG_FOLDER

def perform_action_that_requires_package():
    import numpy as np
    return np.random.random()

def get_current_time_formatted():
    return time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

def save_data_to_file(path, data_array):
    with open(path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data_array)

def create_file_if_not_exist(filename):
    if not os.path.exists(filename):
        with open(filename, 'a') as opened_file:
            pass
        print(f"Created empty file: {filename}")
    
if __name__ == "__main__":
    print(f"Starting script")

    csv_file = f'{DATA_FOLDER}/data.csv'
    try:
        create_file_if_not_exist(csv_file)
        current_time = get_current_time_formatted()
        random_number = perform_action_that_requires_package()
        save_data_to_file(csv_file, [current_time, random_number])
        print(f"Script completed successfully, with data saved to {csv_file}")
    except Exception as e:
        print("Error:", e)
    
    
    