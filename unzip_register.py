import tarfile
import glob
import os
import shutil

def copy_and_extract():
    source_dir = 's3mount/'
    dest_dir = 's3tmp/zips/'
    
    # Get a list of all .tar.gz files in the source directory
    files = glob.glob(os.path.join(source_dir, '*.tar.gz'))
    
    # Iterate over each file
    for file in files:
        # Copy the file to the destination directory
        shutil.copy(file, dest_dir)
    
    # Now, get a list of all .tar.gz files in the destination directory
    files = glob.glob(os.path.join(dest_dir, '*.tar.gz'))
    
    # Iterate over each file
    for file in files:
        # Open the tar file
        with tarfile.open(file, 'r:gz') as tar:
            # Extract all files into the destination directory
            tar.extractall(path='s3tmp/unzips/')

# usage
try:
    copy_and_extract()
except Exception as e:
    print(f"Error: {e}")
# source_dir = 's3tmp/zips/'
# dest_dir = 's3tmp/unzips/'

# # Get a list of all .tar.gz files in the source directory
# files = glob.glob(os.path.join(source_dir, '*.tar.gz'))

# # Iterate over each file
# for file in files:
#     # Open the tar file
#     with tarfile.open(file, 'r:gz') as tar:
#         # Extract all files into the destination directory
#         tar.extractall(path=dest_dir)