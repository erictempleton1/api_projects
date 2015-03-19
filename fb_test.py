import requests
import json
import config

base_url = 'https://graph.facebook.com/me'

fields = 'id,name,favorite_teams'
fields2 = ''


url = '%s?fields=%s&access_token=%s' % (base_url, fields, ACCESS_TOKEN)

print url

content = requests.get(url).json()

# narrow down to name of favorite team
print json.dumps(content['favorite_teams'][0]['name'], indent=4)

"""
while friends['data']:
    try:
        for friends in friend['data']:
            allfriends.append(friend['name'])
        friends=request.get(friends['paging']['next']).json()
    except KeyError:
        print 'Key Error'

print allfriends
"""