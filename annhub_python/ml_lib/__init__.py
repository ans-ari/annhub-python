import requests
def download():
    URL = "https://github.com/ans-ari/annhub-python/raw/update-library/annhub_python/ml_lib/annhub.pyd"
    
    response = requests.get(url=URL,allow_redirects=True)
    file_name = "annhub.pyd"
    with open(file_name,'wb') as f:
        f.write(response.content)
download()

from . import annhub as annhub



