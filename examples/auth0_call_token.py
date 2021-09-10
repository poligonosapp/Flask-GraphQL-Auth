# https://auth0.com/docs/quickstart/backend/python/02-using#calling-the-api-from-your-application

import http.client

conn = http.client.HTTPConnection("localhost:3010")

headers = { 'authorization': "Bearer YOUR_ACCESS_TOKEN" }

conn.request("GET", "/api/private", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))