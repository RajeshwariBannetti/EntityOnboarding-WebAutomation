import http.client
import json

conn = http.client.HTTPSConnection("auth.jai-kisan.com")
payload = 'username=rajeshwari.bannetti%40jai-kisan.com&password=rajeshwari%40123&grant_type=password&client_id=test' \
          '-lms '
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
conn.request("POST", "/auth/realms/test/protocol/openid-connect/token", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

conn = http.client.HTTPSConnection("test-entity.jai-kisan.com")
payload = json.dumps({
  "email": "rajeshwari@gmail.com"
})
headers = {
  'x-api-key': 'a3riN1g2iE5VjnirjVT1X4Nhtcr5H3r12eb2M9aQ',
  'Authorization': 'Bearer '
                   'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJzMGM0bmx2cndJd193Ymt4S2xqc2VXbW01RS1oTFNhWml5cDNaRW9vczl3In0.eyJleHAiOjE2MzE3ODg2MTUsImlhdCI6MTYzMTc4NjgxNSwianRpIjoiZGQyMDVmMmUtZjA2ZS00MDRjLWJkZDQtMzc3NDEyOTIzY2ViIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLmphaS1raXNhbi5jb20vYXV0aC9yZWFsbXMvdGVzdCIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiIyODg1NjA5MC0wNzUyLTQ4MTctOTQ5NS1iNDdjNTYyMjkyNzQiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ0ZXN0LWxtcyIsInNlc3Npb25fc3RhdGUiOiI5Y2ZmMjE3YS03NmUzLTQ5MDItYTE2OS1kMGZmYWY3NDgxMmQiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIioiLCJodHRwczovL3Rlc3QtbG1zLmphaS1raXNhbi5jb20iXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJKSyBTeXN0ZW0gVXNlciIsInByZWZlcnJlZF91c2VybmFtZSI6ImprLXN5c3RlbS11c2VyIiwiZ2l2ZW5fbmFtZSI6IkpLIFN5c3RlbSIsImZhbWlseV9uYW1lIjoiVXNlciIsImVtYWlsIjoiamstc3lzdGVtLXVzZXJAamFpLWtpc2FuLmNvbSJ9.bo3Lp4xjy2gVuJ56pp3U6uuQvgkpEhlm3tKXldn0QkBt8ua1PoCR8OqkYlEr8sQBs2-Gfcrjihc6d76oqNupoKaBFF5oaZlXCM_SqX45j9-Y-bJ7wGI2kFd7Gi8KmqJ2FqZrTFvCaWdqMmxnVQiqaCB6sVWNOHgaMQEFEfPgiULtu1RNx4_WZT8xdJq6CLacRRQ5Hr-AEc42xO-HaZYbD99RWxRVDIdZE8PqW-bdHeFwTUJFBLJ0aigGLNShDNuoExr0MPz6KeNH7igyiJKYCqWXLGURviouXui27J6pqTTzJ1UQy2825vauhOUgTGrHjxZsAlEEkvRCmTkLw8DLug',
  'Content-Type': 'application/json'
}
conn.request("PATCH", "/entities/v1/en-master/biz/cnf/en-cnf-company-information-tab-1/section/en-sec-firm-isGst"
                      "/verify/attrKey/61360b46f41a4d4577c8e206", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
