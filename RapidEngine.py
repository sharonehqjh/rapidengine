import os
import shutil
from filecmp import dircmp

def synchronize_folders(source, destination):
    """Synchronize two folders to maintain consistency."""
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    # Compare the directories
    comparison = dircmp(source, destination)
    
    # Copy new and updated files from source to destination
    for file_name in comparison.left_only + comparison.diff_files:
        source_file = os.path.join(source, file_name)
        destination_file = os.path.join(destination, file_name)
        
        if os.path.isfile(source_file):
            shutil.copy2(source_file, destination_file)
            print(f"Copied {source_file} to {destination_file}")
        elif os.path.isdir(source_file):
            synchronize_folders(source_file, destination_file)
    
    # Remove files from destination that are not present in source
    for file_name in comparison.right_only:
        destination_file = os.path.join(destination, file_name)
        if os.path.isfile(destination_file):
            os.remove(destination_file)
            print(f"Removed {destination_file}")
        elif os.path.isdir(destination_file):
            shutil.rmtree(destination_file)
            print(f"Removed directory {destination_file}")

def main():
    source_folder = input("Enter the path of the source folder: ").strip()
    destination_folder = input("Enter the path of the destination folder: ").strip()
    
    if not os.path.exists(source_folder):
        print("Source folder does not exist. Please check the path and try again.")
        return
    
    synchronize_folders(source_folder, destination_folder)
    print("Synchronization complete.")

if __name__ == "__main__":
    main()