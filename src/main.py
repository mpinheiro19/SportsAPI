import requests
from dotenv import load_dotenv
import os

# Get the path to the directory this file is in
#BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Connect the path with your '.env' file name
#load_dotenv(os.path.join(BASEDIR, '.env'))

load_dotenv()

def main():

    url = os.getenv('SPORTS_API_URL')

    payload={}
    
    headers = {
    'x-rapidapi-key': os.getenv('api-key'),
    'x-rapidapi-host': os.getenv('SPORTS_API_HOST')
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

main()


#4163 id2