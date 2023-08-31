import requests

def get_categories():
    url = "https://api.escuelajs.co/api/v1/categories"
    response = requests.get(url)
    print('status code:',response.status_code)
    print('text:',response.text)
    categories = response.json()
    for category in categories:
        print(category['name'])
