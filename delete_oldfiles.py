import os

# get the amount of argument lines
with open(r"search_terms.csv", 'r') as fp:
    for count, line in enumerate(fp):
        pass
row_count = count + 1

# delete old files
# TODO make method of these deletetions
# 
def delete_files():
    print(f"Total number of keywords: {row_count}")
    range(row_count)
    for i in range(row_count):
        if os.path.exists(f"input_{i}.json"):
            os.remove(f"input_{i}.json")

    if os.path.exists("jobs.docx"):
        os.remove("jobs.docx")
    if os.path.exists("sorted.json"):
        os.remove("sorted.json")
    if os.path.exists("output.json"):
        os.remove("output.json")
    if os.path.exists("output_temp.json"):
        os.remove("output_temp.json")


