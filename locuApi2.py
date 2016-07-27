import urllib2
import json

locu_api = '5e7405ac7b498c8bb0b0f854a022eb1c21b1f19e'

url = 'https://api.locu.com/v1_0/venue/search/?name=burgers&locality=florida&api_key=5e7405ac7b498c8bb0b0f854a022eb1c21b1f19e'
json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

for item in data['objects']:
    print item
    
    for item in data['objects']:
        print item['name']
        print item['phone']
