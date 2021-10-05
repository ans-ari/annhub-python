import requests
def download():
    URL = "https://github.com/ans-ari/annhub-python/raw/update-library/annhub_python/ml_lib/annhub.pyd"
    
    response = requests.get(url=URL,allow_redirects=True)
    file_name = "annhub.pyd"
    with open(file_name,'wb') as f:
        f.write(response.content)
        
# As the .pyd can not be uploaded into PyPi, we need to download it first before it can be
# injected to our project        
download()

from . import annhub as annhub



