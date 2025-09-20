import copy_to_input_queue
from process_vtt import process_vtt_files





if __name__ == "__main__":
    # Step 1 (Copy relevant files)
    copy_to_input_queue.copy_new_vtt_files_for_processing()

    # Step 2 (Process files to convert it to an interview Q/A txt file)
    process_vtt_files(dir_containing_vtt_files=copy_to_input_queue.VTT_TO_PROCESS_DIR)

