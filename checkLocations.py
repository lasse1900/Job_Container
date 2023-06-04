import pandas
import csv

def checkLocations():
    # To double check that search terms are read correct to docx files 
    file_params = pandas.read_csv('search_terms.csv')
    locations = []
    for index, row in file_params.iterrows():
        location = row['location']
        print(f"location: {location}")
        locations.append(location)

    # Open the CSV file in write mode & write the keyword(s)
    filename = 'locations.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([location]) 
    print(f"Locations: ------> {locations}")
    return locations

if __name__ == '__main__':
    checkLocations()