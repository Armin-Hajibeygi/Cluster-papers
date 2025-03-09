import os
from create_folders import create_folders
from extract_abstracts import save_abstracts_to_file
from cluster_papers import cluster_papers

folder_path = "/Users/armin/Desktop/HEC/Research/Data Analytics Group/LLM fairness"
max_num_folders = 4

os.system("clear")

print("Extracting abstracts from folder...")
save_abstracts_to_file(folder_path)

print("Clustering papers...")
cluster_papers(max_num_folders)

print("Creating folders...")
create_folders(folder_path)

print("Done!")
