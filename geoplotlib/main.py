import requests
import csv

## step 1 get locations
locations_list = []
with open('haltestellen.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        locations_list.append(row['CHSTNAME'])
        line_count += 1
    print(f'Processed {line_count} lines.')

# Needs valid api key (billed)
key = 'XXX'

## step 2: locations to lat/long via google api
locations_final_list = []
i, s = 0, 0

for loc in locations_list:
    query = {'address': loc, 'key': key}
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?', params=query)
    response_json = response.json()

    if response_json.get('results'):
        location_data = response.json()['results'][0]['geometry']['location']
        print("processed: " + str(i))
        i += 1
        locations_final_list.append([loc, location_data['lat'], location_data['lng']])
    else:
        print("skipped: " + str(s))

print(locations_final_list)
## step 3: create csv
with open('prepared_locations.csv', mode='w') as f:
    writer = csv.writer(f)
    header = ['name', 'lat', 'lon']
    writer.writerow(header)

    for lfl in locations_final_list:
        writer.writerow(lfl)

print("finished")