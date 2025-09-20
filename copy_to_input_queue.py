import os
import glob
import shutil


ORIGINAL_VTT_FILES_DIR = "./input"
VTT_TO_PROCESS_DIR = "./vtt_files_to_process"


def copy_new_vtt_files_for_processing():    
    """
    Copy new .vtt files from input directory to VTT_TO_PROCESS_DIR directory with modified names.
    If a file with the same modified name already exists in VTT_TO_PROCESS_DIR, it will be skipped.
    """
    # Create directory if it doesn't exist
    os.makedirs(VTT_TO_PROCESS_DIR, exist_ok=True)

    existing_files = set([f"{os.path.basename(file)}" for file in os.listdir(VTT_TO_PROCESS_DIR) if file.endswith(".vtt")])
    print(f"Existing files: {existing_files}")


    # Recursively find all .vtt files in input directory and its subdirectories
    vtt_files = glob.glob(os.path.join(ORIGINAL_VTT_FILES_DIR, "**", "*.vtt"), recursive=True)

    for file in vtt_files:
        # Get parent directory name and base file name
        parent_dir = os.path.basename(os.path.dirname(file))
        base_name = os.path.basename(file)
        file_to_copy = f"{parent_dir}_{base_name}"

        if file_to_copy not in existing_files:
            destination_file_path = os.path.join(VTT_TO_PROCESS_DIR, file_to_copy)
            shutil.copy(file, destination_file_path)
            print(f"Copied: {parent_dir}_{base_name}")
        else:
            print(f"Skipped (already exists): {parent_dir}_{base_name}")