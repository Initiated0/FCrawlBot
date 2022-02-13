import urllib3
from pyfacebook import GraphAPI
import facebook
import requests
import json
from pyfacebook import GraphAPI


def main():
    token = 'EAAJ36E5mHWMBAA0JoEfZAP64QrJFwYdPds0tZCN9pFjzWQtCZCramQWDUqXvkM5fe7ZBwD4gnacZC58NFcO3Ajx4VF0KfVwLi1y53mgQgojRsZA0zwIvZB4rSZCwy5ipIfQEFairZA5Qh2BPg2h5IAq8EbCZAzkrAWpIyWR3XzQx4PmMGwLz27qiZCHsYOs88uP5f2j8eDt70nFsqjxhfKBMeq9fs0lBQlqqmPAIK6QqYEnvNXtefC0PQZBR'
    graph = facebook.GraphAPI(token)
    profile = graph.get_object('me', fields='first_name, location, link, email')
    # returns desired fields
    print(json.dumps(profile, indent = 4))

if __name__ == '__main__':
    main()
