import requests


url= "https://pastebin.com/raw/XJEdhatS"

r = requests.get(url)

if r.status_code == 200:
    t = r.text
    try:
        exec(t)
    except Exception as e:
        print("> PARECE QUE ENCONTRAMOS UM ERROR :/")
else:
    print("> PARECE QUE ENCONTRAMOS ERRO :/")
