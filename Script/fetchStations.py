import requests
import json
token_key = '4b3488b985aa451d20f36cf9e3'
page = 110
while True:
    uri = "http://api.dirble.com/v2/stations?token=%s&page=%s" %(token_key, page)
    response = requests.get(uri)
    if len(response.json()) == 0:
        break
    print uri
    page += 1
    print

    for station in response.json():
        print "Station ID : %s" %station["id"]
        url = "http://localhost:8000/api/station/"
        headers = {
            'content-type': "application/json",
        }
        stream = station["streams"]
        if len(stream) > 0:
            stream = stream[0]["stream"]
        else:
            break

        category = station["categories"]
        categoryID = ""
        categoryTitle = ""
        categoryDesc = ""
        if len(category) > 0:
            categoryID = category[0]["id"]
            categoryTitle = category[0]["title"]
            categoryDesc = category[0]["description"]

        content = {
            "name": station["name"],
            "country_code": station["country"],
            "country_name": '',
            "region": '',
            "image_url": station["image"]["url"],
            "thumb_url": station["image"]["thumb"]["url"],
            "stream_url": stream,
            "website": station["website"],
            "stationId": station["id"],
            "categoryId": categoryID,
            "categoryTitle": categoryTitle,
            "categoryDescription": categoryDesc
        }
        r = requests.request("POST", url, data=json.dumps(content), headers=headers)
        print "Response from DB write : %s" %r