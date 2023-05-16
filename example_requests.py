import requests
def requests_1(query):
    json = {'word':f'{query}'}
    url = requests.post("http://127.0.0.1:5000/requests-1", json=json)
    r = url.text
    return r
def requests_2(query):
    headers = {'word':f'{query}'}
    url = requests.post("http://127.0.0.1:5000/requests-2", headers=headers)
    r = url.text
    return r
def requests_3(query):
    url = requests.get(f"http://127.0.0.1:5000/requests-3?word={query}")
    r = url.text
    return r
    
print(requests_1('hello'))
print(requests_3('world'))
print(requests_3('love'))
