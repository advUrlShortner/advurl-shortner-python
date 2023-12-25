import requests

def short(url, password=None, second_url=None, ttl=None, weights=None):
    data = {"url": url}
    if password:
        data["pass"]=password
    if second_url:
        data["second_url"]=second_url
    if ttl:
        data["ttl"]=ttl
    if weights:
        data["weights"]=weights
    response = requests.post('https://advurlshortner.top/api/newurl/', json=data)

    if response.status_code == 200:
        output = response.json()
    else:
        return response.status_code
    return output

def stat(url,password):
    response = requests.post("https://advurlshortner.top/api/stat/", json= {"short_url":url,"pass":password})
    if response.status_code == 200:
        output = response.json()
    else:
        return response.status_code
    return output
