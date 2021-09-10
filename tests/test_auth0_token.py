# https://auth0.com/docs/quickstart/backend/python/02-using
import http.client

conn = http.client.HTTPSConnection("")

payload = "grant_type=client_credentials&client_id=%24%7Baccount.clientId%7D&client_secret=YOUR_CLIENT_SECRET&audience=YOUR_API_IDENTIFIER"

headers = { 'content-type': "application/x-www-form-urlencoded" }

conn.request("POST", "/YOUR_DOMAIN/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))