# Interviews Processor

An automated tool that processes VTT subtitle files from interviews and converts them into structured question/answer text files.

## Python Version Used
### 3.11.9

## Overview

This application helps you convert interview transcripts in VTT format (WebVTT subtitle files) into organized, easy-to-read question and answer text files. It automates the tedious process of manually extracting interview content from video transcripts.

## How It Works

1. The application scans a designated source directory for new VTT files
2. It copies these files to a processing queue
3. The VTT files are processed to identify questions and answers
4. Structured Q&A text files are generated as output

## How to Run

1. Make sure Python 3.11.9 is installed on your system
2. Install required dependencies (if any):
   ```
   pip install -r requirements.txt
   ```
3. Run the main application:
   ```
   python main_app.py
   ```

## Benefits

- **Time-saving**: Automatically extracts Q&A content from interview transcripts
- **Consistency**: Creates uniformly formatted interview text files
- **Batch processing**: Handles multiple VTT files in a single run
- **Easy workflow**: Just add new VTT files to the source directory and run the app

## Directory Structure

- Source VTT files are picked up from the configured source directory
- Processed files are stored in a designated output directory
- Logs and temporary files are managed automatically

## Configuration

The application uses default paths for input and output. To modify these settings, please adjust the constants in the respective modules.

## Troubleshooting

If you encounter any issues:
1. Ensure your VTT files are properly formatted
2. Check that you have read/write permissions to all directories
3. Verify Python 3.11.9 is correctly installed
