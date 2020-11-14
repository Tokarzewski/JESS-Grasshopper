import requests
import fire

def cookie(user_email, password):
    """
    returns cookie
    :param user_email: user_email for jea
    :param password: password
    :return: cookie
    """
    # API endpoint URL
    ApiBase = 'https://api.ensims.com/'
    UserApi = ApiBase + 'users/api/'

    # Set header and body of the POST request
    headers = {'Content-Type': 'application/json'}
    body = {"email": user_email, "password": password}

    # Post request
    r = requests.post(UserApi + "auth", headers=headers, json=body)
    #r = requests.post(UserApi + 'checkin', cookies=r.cookies)
    return dict(r.cookies)["session_token"]

def get(cookie, url):
    """
    returns request get method
    :param cookie: cookie
    :param url: base with url
    :return: request response 
    """
    #Update cookie
    ApiBase = 'https://api.ensims.com/'
    UserApi = ApiBase + 'users/api/'
    r = requests.get(UserApi + 'info')
    r.cookies.update({"session_token":cookie})

    #get request
    r = requests.get(url)
    return r.text

def post(cookie, url):
    """
    returns request post method
    :param cookie: cookie
    :param url: base with url
    :return: request response
    """
    #Update cookie
    ApiBase = 'https://api.ensims.com/'
    UserApi = ApiBase + 'users/api/'
    r = requests.get(UserApi + 'info')
    r.cookies.update({"session_token":cookie})
    
    r = requests.post(url, cookies = r.cookies)
    return r.text

if __name__ == "__main__":
    fire.Fire({
        "get": get,
        "cookie": cookie,
        "post": post
    })