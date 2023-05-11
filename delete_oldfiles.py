import os
import pandas

# get the amount of argument lines, takes only valid lines (not CRs)
file_params = pandas.read_csv('search_terms.csv')
for row_count, row in file_params.iterrows():
    pass

print(f"delete method row_count: {row_count+1}")
row_count += 1

# delete old files
# TODO make method of these deletetions
def delete_files():
    # print(f"Total number of keywords:---> {row_count}")
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


