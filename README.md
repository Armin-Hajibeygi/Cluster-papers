# Cluster-Papers

A tool for automatically organizing research papers into thematic folders using AI.

## Overview

This project helps researchers organize their PDF papers by:
1. Extracting abstracts from PDF files
2. Using OpenAI's GPT models to identify thematic clusters
3. Automatically creating folders and organizing papers based on their content

## Features

- Extract abstracts from PDF papers
- Automatically identify research themes using AI
- Create thematic folders
- Organize papers into appropriate folders
- Customizable number of thematic clusters

## Requirements

- Python 3.8+
- OpenAI API key
- PDF research papers

## Installation

1. Clone this repository

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your OpenAI API key:
   ```
   API_KEY = "your-openai-api-key"
   ```

## Usage

1. Update the `folder_path` in `user_interface.py` to point to your folder containing PDF papers.

2. Set the desired number of thematic clusters by modifying `max_num_folders` in `user_interface.py`.

3. Run the application:
   ```
   python user_interface.py
   ```

4. The script will:
   - Extract abstracts from all PDFs in the specified folder
   - Cluster papers based on their content
   - Create thematic folders
   - Move papers to their respective folders

## Project Structure

- `extract_abstracts.py`: Extracts text from PDFs and uses GPT to identify abstracts
- `cluster_papers.py`: Uses GPT to identify themes and assign papers to clusters
- `create_folders.py`: Creates folders and moves papers based on clustering results
- `user_interface.py`: Main script that orchestrates the entire process
- `paper_folder_mapping.json`: Generated mapping of papers to their assigned folders
- `results.txt`: Extracted abstracts from papers

## Customization

You can customize the clustering by:
- Changing the `max_num_folders` parameter to control the number of thematic clusters
- Modifying the prompt in `cluster_papers.py` to adjust how papers are categorized