import requests

params = {"q": "pizza"}
r = requests.get("http://bing.com/search", params = params)
print("Status: " + str(r.status_code))

print(r.text)

f = open("./page.html", "w+")
f.write(r.text)
