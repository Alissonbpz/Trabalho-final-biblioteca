import requests

URL = "http://127.0.0.1:8000/livros/"

r = requests.get(URL)
print(r.status_code, len(r.json()["livros"]))

novo = {"titulo": "Teste", "autor": "Fulano", "ano": 2020}
r = requests.post(URL, json=novo)
print(r.status_code, r.json())

r = requests.post(URL, json={"autor": "Fulano", "ano": 2020})
print(r.status_code, r.json())

r = requests.post(URL, json={"titulo": "Teste", "autor": "Fulano", "ano": 2020})
novo_id = r.json()["id"]

alterado = {"titulo": "Teste 2", "autor": "Fulano", "ano": 2021}
r = requests.put(URL + f"{novo_id}/", json=alterado)
print(r.status_code, r.json())

r = requests.put(URL + f"{novo_id}/", json={"autor": "Fulano", "ano": 2021})
print(r.status_code, r.json())

r = requests.delete(URL + f"{novo_id}/")
print(r.status_code, repr(r.text))

r = requests.delete(URL + f"{novo_id}/")
print(r.status_code, r.json())