import os
import glob
import shutil

from process_vtt import process_vtt_files


VTT_DIR = "./vtt_input"


def copy_new_vtt_files():    
    """
    Copy new .vtt files from input directory to vtt_input directory with modified names.
    If a file with the same modified name already exists in vtt_input, it will be skipped.
    """
    # Create directory if it doesn't exist
    os.makedirs(VTT_DIR, exist_ok=True)

    existing_files = set([f"{os.path.basename(file)}" for file in os.listdir(VTT_DIR) if file.endswith(".vtt")])
    print(f"Existing files: {existing_files}")


    # Recursively find all .vtt files in input directory and its subdirectories
    vtt_files = glob.glob("./input/**/*.vtt", recursive=True)

    for file in vtt_files:
        # Get parent directory name and base file name
        parent_dir = os.path.basename(os.path.dirname(file))
        base_name = os.path.basename(file)
        file_to_copy = f"{parent_dir}_{base_name}"

        if file_to_copy not in existing_files:
            shutil.copy(file, f"./vtt_input/{parent_dir}_{base_name}")
            print(f"Copied: {parent_dir}_{base_name}")
        else:
            print(f"Skipped (already exists): {parent_dir}_{base_name}")


if __name__ == "__main__":
    # Step 1 (Copy relevant files)
    copy_new_vtt_files()

    # Step 2 (Process files to convert it to an interview Q/A txt file)
    process_vtt_files(dir_containing_vtt_files=VTT_DIR)

