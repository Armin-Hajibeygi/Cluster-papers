import os
import shutil
import re
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
llm = OpenAI(api_key=API_KEY)


def read_results_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def call_chatgpt_api(content, max_num_folders):
    prompt = f"""
            I have a text file with the content of several research papers. I need to organize these papers into different categories (folders). Each category should represent a unique subject or theme based on the content of the papers. Please help me by:

            1. Identifying the main themes or topics from the content of the papers.
            2. Providing a list of folder names that correspond to each theme.
            3. Assigning each paper to its appropriate folder based on its content. All papers should be assigned to a folder.
            4. The maximum number of folders is {max_num_folders}, but you can use less if the themes are not distinct.

            The structure of the text file is as follows:

            - Each paper's content is separated by a line with the paper's title followed by a blank line.
            - Below is a sample of the format:

                Title 1

                [Content of paper 1]

                Title 2

                [Content of paper 2]

            **Response Format:**
            1. **FOLDER LIST:**  
            - Begin the folder list with `### FOLDERS:`
            - List folders using the format: `folder_name`  
            - Folder names **must not contain special characters**, only letters, numbers, and spaces.

            2. **PAPER-FOLDER MAPPING:**
            - Begin with `### PAPER_FOLDER_MAPPING:`
            - Use a JSON format enclosed within triple backticks (` ```json ... ``` `).
            - The JSON should map `"paper title.pdf"` → `"folder_name"`.
            - Use the exact paper title as it is in the text file.
            """

    messages = [
        {
            "role": "system",
            "content": prompt,
        },
        {"role": "user", "content": content},
    ]

    completion = llm.chat.completions.create(model="gpt-4o-mini", messages=messages)
    cluster_assignments = completion.choices[0].message.content.strip()

    return cluster_assignments


def cluster_papers(max_num_folders=10):
    results_file = "results.txt"
    content = read_results_file(results_file)
    folder_assignments_text = call_chatgpt_api(content, max_num_folders)

    folders_section = re.search(
        r"### FOLDERS:\n(.*?)\n### PAPER_FOLDER_MAPPING:",
        folder_assignments_text,
        re.DOTALL,
    )
    if folders_section:
        folder_names = re.findall(r"\d+\.\s(.+)", folders_section.group(1))
    else:
        print("No folder section found.")

    json_match = re.search(r"```json\n({.*?})\n```", folder_assignments_text, re.DOTALL)
    if json_match:
        json_content = json_match.group(1)
        try:
            paper_folder_mapping = json.loads(json_content)
            with open("paper_folder_mapping.json", "w", encoding="utf-8") as f:
                json.dump(paper_folder_mapping, f, indent=4, ensure_ascii=False)

            print(
                "JSON successfully extracted and saved as 'paper_folder_mapping.json'."
            )

        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        print("JSON part not found in the text.")


if __name__ == "__main__":
    os.system("clear")
    max_num_folders = 20
    cluster_papers(max_num_folders)
