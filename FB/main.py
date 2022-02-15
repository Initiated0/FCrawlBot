from fileinput import filename
from attr import field
import urllib3
from pyfacebook import GraphAPI
import facebook
import requests
import json
from pyfacebook import GraphAPI
import datetime

# token will expire after april 14
token = '''EAAJ36E5mHWMBADGHbJIp7S9oN8HSp4VjC2SGIQrR1RM4ZCtqehdIbtZAiD5SQZCTdn9veolpJD862ZBfjF7jXKTgNlczsuO2N0AMdolJyta24BxU7TkW1JZCzG2GICtQlH6owZAxs1Osjkr634wpX7oXUZCKS6Fieigo4Ww5WgNlAZDZD'''

#   need to improvise and get all the liked pages that are in liked section

def get_likes_api():
    try:
        graph = facebook.GraphAPI(access_token=token)
        likes = graph.request('me/likes')['data']
        user = graph.request('/me?fields=name')

        next_page = graph.request('me/likes')['paging']
        nxt = next_page['next']
        next_ext = next_page['cursors']['after']
        print(type(nxt))



        newlist = []
        for dic in likes:
            newlist.append(dic['name'])
        
        if newlist != []:
            now = datetime.datetime.now()
            filename = str(user['name']) + '-likes-on' + now.strftime('-%y-%m-%d-' + '@-%H-%M')

            with open(filename + '.txt', 'w') as f:
                for item in newlist:
                    f.write('%s\n' % item)

                f.write('%s\n' % nxt)
                f.write('%s\n' % next_ext)      
            

            print('likes successfully retrieved.')

        else:
            print("there were no likes.")
            
    except Exception as e:
        print(e)



def get_likes_request():
    try:
        fields_likes, fields_user = 'https://graph.facebook.com/v12.0/4941549742532535/likes?access_token=' + token, 'https://graph.facebook.com/me?access_token=' + token
        likes = json.loads(requests.get(fields_likes).text)['data']
        user = json.loads(requests.get(fields_user).text)['name']

        newlist = []
        for dic in likes:
            newlist.append(dic['name'])

        if newlist != []:
            now = datetime.datetime.now()
            filename = user + '-Likes-on' + now.strftime('-%y-%m-%d-' + '@-%H-%M')

            with open(filename + '.txt', 'w') as f:
                for item in newlist:
                    f.write('%s\n' % item)
        else:
            print('There is no likes.')


    except Exception as e:
        print(e)

def main():
    graph = facebook.GraphAPI(token)
    profile = graph.get_object('me', fields='first_name, location, link, email')
    # returns desired fields
    print(json.dumps(profile, indent = 4))

if __name__ == '__main__':
    #main()
    get_likes_api()
    # get_likes_request()
