import urllib2
import json
import locuApiKey

searchfor = "locality=Chicago"

def locu_search(query):
    searchfor = query.replace(' ', '%20')
    url = "https://api.locu.com/v1_0/venue/search/?api_key=5e7405ac7b498c8bb0b0f854a022eb1c21b1f19e" + locuApiKey.apiKey + "&" + searchFor
    json_obj = urllib2.urlopen(url)
    
    data = json.load(json_obj)
    
    returnData = data['objects']
    
    return returnData
    
for item in locu_search(searchFor):
    print item['name']








#url = 'https://api.locu.com/v1_0/venue/search/?name=restaurants&locality=chicago&api_key=5e7405ac7b498c8bb0b0f854a022eb1c21b1f19e'
#json_obj = urllib2.urlopen(url)

#data = json.load(json_obj)

for item in data['objects']:
    print item
    
    for item in data['objects']:
        print item['country']
        print item['website_url']
        

locality=name=restaurants&locality=chicago&

def locu_search(query):
    api_key = locu_api
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    locality = query.replace('', '%20')
    final_url = url + "&locality=" + locality + "&category=restaurant"
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    
    for item in data['objecs']:
        print item['name'], item['phone']