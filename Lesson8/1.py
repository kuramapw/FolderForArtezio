import requests


def pageSize(url: str) -> int:
    res = requests.post("http://httpbin.org/post")
    return res.headers["Content-Length"]


print(pageSize("https://google.com"))
