import os
import shutil

# Get the directory where the Python script is running
current_dir = os.getcwd()

# Define source and destination directories relative to the current directory
source_dir = os.path.join(current_dir, 'Original Images')
destination_dir = os.path.join(current_dir, 'Sorted Images')

# Create destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Get a sorted list of all files in the source directory
files = sorted([f for f in os.listdir(source_dir) if f.endswith('.bmp') and os.path.isfile(os.path.join(source_dir, f))])

# Loop over the files, separating them into folders of 10 files each
for i in range(0, len(files), 10):
    # Create a new folder named "..." followed by the iteration number
    folder_name = f'palm{i // 10 + 1}'
    folder_path = os.path.join(destination_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    # Move the 10 files to the new folder
    for file in files[i:i + 10]:
        src_file_path = os.path.join(source_dir, file)
        dst_file_path = os.path.join(folder_path, file)
        shutil.move(src_file_path, dst_file_path)

print('Files have been successfully organized into folders.')