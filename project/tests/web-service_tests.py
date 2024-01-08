import requests

def test_get():
    res = requests.get("http://localhost:5000")
    if res.status_code != 200 or res.text != "Hello, World!":
        print("Web page / not working properly")
        exit(1)
    else:
        print("All good!")
        exit(0)


test_get()
