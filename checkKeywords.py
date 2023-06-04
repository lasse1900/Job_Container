import pandas
import csv

def checkKeywords():
    # To double check that search terms are read correct to docx files 
    file_params = pandas.read_csv('search_terms.csv')
    keywords = []
    for index, row in file_params.iterrows():
        keyword = row['keyword']
        print(f"keyword: {keyword}")
        keywords.append(keyword)

    # Open the CSV file in write mode & write the keyword(s)
    filename = 'keywords.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([keyword]) 
    print(f"Keywords: ------> {keywords}")
    return keywords

if __name__ == '__main__':
    checkKeywords()