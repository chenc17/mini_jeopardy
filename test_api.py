import requests
from datetime import datetime

#testing out accessing the API

#Based on http://www.jservice.io/search?query=science, "science" corresponds to 25
#Also, there are 20 "science" clues in 1996 and one clue does not have an value

min_date = datetime.strptime('01/01/1996,00:00:00,UTC', '%m/%d/%Y,%H:%M:%S,%Z')
max_date = datetime.strptime('12/31/1996,23:59:59,UTC', '%m/%d/%Y,%H:%M:%S,%Z')


parameters = {
    'category':25,
    'min_date':min_date,
    'max_date':max_date
}

response = requests.get('http://www.jservice.io/api/clues', params=parameters)
print(response.status_code)
#will want error handling code here

#there should be 20 clues
json = response.json()
counter = 0
valid_to_display = 0
invalid_to_display = 0
for item in json:
    counter = counter + 1
    if (item['invalid_count']!=None or item['value']!=None):
        print('OK', item, '\n')
        valid_to_display = valid_to_display+1
    else:
        print('NOT OK', item, '\n')
        invalid_to_display = invalid_to_display+1

print(counter,' clues in total')
print(valid_to_display,' valid to display')
print(invalid_to_display, ' invalid to display')
