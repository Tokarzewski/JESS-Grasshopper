import requests, fire

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
    return r.cookies.values

def delete(cookie, url):
    """
    deletes files or folder
    :param url: base + url + (file or folder path)
    :return: request response
    """
    ApiBase = 'https://api.ensims.com/'
    UserApi = ApiBase + 'users/api/'
    r = requests.get(UserApi + 'info')
    r.cookies.update({"session_token":cookie})
    r = requests.delete(url, cookies = r.cookies)
    return r.text

def get(cookie, url):
    """
    returns request get method
    :param cookie: cookie
    :param url: base with url
    :return: request response 
    """
    # Update cookie
    ApiBase = 'https://api.ensims.com/'
    UserApi = ApiBase + 'users/api/'
    r = requests.get(UserApi + 'info')
    r.cookies.update({"session_token":cookie})

    # Get request
    r = requests.get(url, cookies = r.cookies)
    return r.text

def post(cookie, url):
    """
    returns request post method
    :param cookie: cookie
    :param url: base with url
    :return: request response
    """
    # Update cookie
    ApiBase = 'https://api.ensims.com/'
    UserApi = ApiBase + 'users/api/'
    r = requests.get(UserApi + 'info')
    r.cookies.update({"session_token":cookie})
    r = requests.post(url, cookies = r.cookies)
    return r.text

def postf(cookie, url, files):
    """
    returns request post method
    :param cookie: cookie
    :param url: base with url
    :param file: the filepath for the file or job set
    :return: request response
    """
    # Update cookie
    ApiBase = 'https://api.ensims.com/'
    UserApi = ApiBase + 'users/api/'
    JessApi = ApiBase + "jess_web/api/"
    r = requests.get(JessApi + 'info')
    r.cookies.update({"session_token":cookie})

    files = eval(files)
    r = requests.post(url, cookies = r.cookies, files=files)
    return r.text

if __name__ == "__main__":
    fire.Fire({
        "cookie": cookie,
        "delete": delete,
        "get": get,
        "post": post,
        "postf": postf
    })