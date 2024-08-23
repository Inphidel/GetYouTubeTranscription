# YouTube Video Transcription Exporter

A simple Python script to fetch and export YouTube video transcripts if available.

## Requirements

- Python 3.8 or higher
- `pytube` for YouTube video information
- `youtube-transcript-api` for fetching video transcripts

## Installation

1. **Install Python:**
   Ensure you have Python 3.8 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Set Up a Virtual Environment:**
   - Open your command prompt or terminal.
   - Navigate to your project directory:
     ```sh
     cd path/to/your/project
     ```
   - Create a virtual environment:
     ```sh
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows:**
       ```sh
       venv\Scripts\activate
       ```
     - **Mac/Linux:**
       ```sh
       source venv/bin/activate
       ```

3. **Install Dependencies:**
   With your virtual environment activated, install the required packages:
   ```sh
   pip install pytube youtube-transcript-api
