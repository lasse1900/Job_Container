import os
import pandas

# get the amount of argument lines, takes only valid lines (not CRs)
file_params = pandas.read_csv('search_terms.csv')
for row_count, row in file_params.iterrows():
    pass

# delete old files, also with extra index in case
row_count += 5
def delete_files():
    # print(f"Total number of keywords:---> {row_count}")
    range(row_count)
    for i in range(row_count):
        if os.path.exists(f"input_{i}.json"):
            os.remove(f"input_{i}.json")

    if os.path.exists("jobs.docx"):
        os.remove("jobs.docx")
    if os.path.exists("jobs2.docx"):
        os.remove("jobs2.docx")
    if os.path.exists("sorted.json"):
        os.remove("sorted.json")         
    if os.path.exists("output.json"):
        os.remove("output.json")
    if os.path.exists("output_temp.json"):
        os.remove("output_temp.json")
    if os.path.exists("filtered.json"):
        os.remove("filtered.json")    
    if os.path.exists("filtered_with_header.json"):
        os.remove("filtered_with_header.json")       
    if os.path.exists("formated.md"):
        os.remove("formated.md")
    if os.path.exists("temp.csv"):
        os.remove("temp.csv")
        