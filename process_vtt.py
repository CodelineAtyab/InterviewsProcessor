def process_vtt_files(dir_containing_vtt_files):
    """
    Placeholder function to process .vtt files in vtt_input directory.
    This function should be implemented to convert .vtt files to interview Q/A txt files.
    """
    print(f"Processing .vtt files in {dir_containing_vtt_files}... (functionality to be implemented)")


if __name__ == "__main__":
    process_vtt_files("./vtt_input")

    from openai import OpenAI
    client = OpenAI()

    response = client.responses.create(
        model="gpt-5",
        input="Write a one-sentence bedtime story about a unicorn."
    )

    print(response.output_text)