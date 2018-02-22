import requests.auth

def getRedditToken():
    client_auth = requests.auth.HTTPBasicAuth(Zm62_f7ttWEsxA,KSVkY7A4EmnGfQkDGcqsqQRXxM8)
    post_data = {"grant_type": "password:", "username": <bleblabla>, "password": <15900383a>}
    HEADERS = {"User-Agent": <MI 250 test>}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    return(response.json())
    
def getRedditUserDetails(token):
    url = "https://oauth.reddit.com/api/v1/me"
    headers = {"Authorization": "bearer "+token, "User-Agent": <MI 250 test>}
    response = requests.get(url,headers = headers)
    return(response.json())