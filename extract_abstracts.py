import os
from pypdf import PdfReader
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
llm = OpenAI(api_key=API_KEY)


def extract_first_page_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    text += reader.pages[0].extract_text() + "\n"
    text += reader.pages[1].extract_text() + "\n"
    return text


def get_abstract_from_chatgpt(text):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI assistant. Read and only exactly write the abstract of the paper."
            ),
        },
        {"role": "user", "content": text},
    ]

    completion = llm.chat.completions.create(model="gpt-4o-mini", messages=messages)
    abstract = completion.choices[0].message.content.strip()
    return abstract


def extract_abstracts_from_folder(folder_path):
    texts = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            print(filename)
            file_path = os.path.join(folder_path, filename)
            text = extract_first_page_text(file_path)
            abstract = get_abstract_from_chatgpt(text)
            texts += f"{filename}\n{abstract}\n---\n"
    return texts


def save_abstracts_to_file(path):
    results = extract_abstracts_from_folder(path)
    with open("results.txt", "w") as file:
        file.write(results)


if __name__ == "__main__":
    os.system("clear")
    folder_path = "/Users/armin/Desktop/HEC/Research/Data Analytics Gorup/LLM fairness"
    save_abstracts_to_file(folder_path)
