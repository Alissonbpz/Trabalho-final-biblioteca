import requests

URL = "http://127.0.0.1:8000/livros/"

r = requests.get(URL)
print(r.status_code, len(r.json()["livros"]))

novo = {"titulo": "Teste", "autor": "Fulano", "ano": 2020}
r = requests.post(URL, json=novo)
print(r.status_code, r.json())

r = requests.post(URL, json={"autor": "Fulano", "ano": 2020})
print(r.status_code, r.json())