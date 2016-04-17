import json
import requests

uri = "http://data.okfn.org/data/core/language-codes/r/language-codes.json"
response = requests.get(uri)


for lang in response.json():
    print "Language : %s" %lang["English"]
    url = "http://localhost:8000/api/languages/"
    headers = {
        'content-type': "application/json",
    }
    content = {
        "name": lang["English"],
        "code": lang["alpha2"],
    }
    r = requests.request("POST", url, data=json.dumps(content), headers=headers)
    print "Response from DB write : %s" %r