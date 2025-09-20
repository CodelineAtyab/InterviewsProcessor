import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROCESSED_VTT_DIR = "./processed_vtt_files"


def get_input_prompt(interviewer_name, interviewee_name, content):
    input_prompt = f"""
        Act as an interview analyser between two people. The interview is taken by {interviewer_name} and the interviewee name is {interviewee_name}.
        All questions will be asked by {interviewer_name} and all answers will be given by {interviewee_name}.
        Convert the following interview transcription into a Q/A format.
        Provide the output in the following format:
        [time] Q: Question 1?
        [time] A: Answer 1.
        Result: Based on the Question and the Answer select one of "Correct", "Partially Correct" or "Incorrect"

        [time] Q: Question 2?
        [time] A: Answer 2.
        Result: <put result here>
        etc ...

        Answers can be wrong so don't assume they are correct.
        Identify all questions and answers, and format them accordingly.
        Question and Answers can be summarized without missing important information and without correcting the answers.
        Here is the transcription:
        {content}
    """
    return input_prompt


def process_vtt_files(dir_containing_vtt_files):
    """
    Placeholder function to process .vtt files in vtt_input directory.
    This function should be implemented to convert .vtt files to interview Q/A txt files.
    """
    os.makedirs(PROCESSED_VTT_DIR, exist_ok=True)
    print(f"Processing .vtt files in {dir_containing_vtt_files}.")
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    print(f"OpenAI client initialized...")

    # Loop through all .vtt files in the specified directory
    for file_name in os.listdir(dir_containing_vtt_files):
        if file_name.endswith(".vtt"):
            file_path = os.path.join(dir_containing_vtt_files, file_name)
            print(f"Processing file: {file_path}")
            # Here you would add the logic to process the .vtt file
            # For demonstration, we'll just read and print the first few lines
            content_of_current_file = None
            with open(file_path, "r", encoding="utf-8") as file:
                content_of_current_file = file.read()
            
            if content_of_current_file:
                interviewee_name = file_name.split("_")[0]  # Extract name before the first underscore
                interviewer_name = "Atyab"
                print(f"Interviewee: {interviewee_name}, Interviewer: {interviewer_name}")

                input_prompt = get_input_prompt(interviewer_name, interviewee_name, content_of_current_file)

                response = client.responses.create(
                    model="gpt-5-mini",
                    input=input_prompt
                )
                
                output_text = response.output_text
                print(f"Output for {file_name}:\n{output_text[:50]}...")  # Print first 50 characters

                with open(os.path.join(PROCESSED_VTT_DIR, f"{interviewee_name}_interview.txt"), "w", encoding="utf-8") as out_file:
                    out_file.write(output_text)
                print(f"Processed {file_name} and saved to {interviewee_name}_interview.txt\n\n")


if __name__ == "__main__":
    # import os
    # from copy_to_input_queue import VTT_TO_PROCESS_DIR

    # os.makedirs(PROCESSED_VTT_DIR, exist_ok=True)

    # example_file_name = "Ahmed_video1836466372.vtt"
    # example_file_to_process = os.path.join(VTT_TO_PROCESS_DIR, example_file_name)
    # interviewee_name = example_file_name.split("_")[0]  # Extract name before the first underscore
    # interviewer_name = "Atyab"

    # content = None
    # with open(example_file_to_process, "r", encoding="utf-8") as file:
    #     content = file.read()
    
    # if content:
    #     print(f"Content of {example_file_to_process}:\n{content[:500]}...")  # Print first 500 characters
    #     input_prompt = f"""
    #     Act as an interview analyser between two people. The interview is taken by {interviewer_name} and the interviewee name is {interviewee_name}.
    #     All questions will be asked by {interviewer_name} and all answers will be given by {interviewee_name}.
    #     Convert the following interview transcription into a Q/A format.
    #     Provide the output in the following format:
    #     [time] Q: Question 1?
    #     [time] A: Answer 1.
    #     Result: Based on the Question and the Answer select one of "Correct", "Partially Correct" or "Incorrect"

    #     [time] Q: Question 2?
    #     [time] A: Answer 2.
    #     Result: <put result here>
    #     etc ...

    #     Answers can be wrong so don't assume they are correct.
    #     Identify all questions and answers, and format them accordingly.
    #     Question and Answers can be summarized without missing important information and without correcting the answers.
    #     Here is the transcription:
    #     {content}
    #     """
    #     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    #     response = client.responses.create(
    #         model="gpt-5-mini",
    #         input=input_prompt
    #     )
        
    #     output_text = response.output_text
    #     print(output_text)

    #     with open(os.path.join(PROCESSED_VTT_DIR, f"{interviewee_name}_interview.txt"), "w", encoding="utf-8") as out_file:
    #         out_file.write(output_text)
    from copy_to_input_queue import VTT_TO_PROCESS_DIR
    process_vtt_files(dir_containing_vtt_files=VTT_TO_PROCESS_DIR)