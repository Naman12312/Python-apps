import http.client

conn = http.client.HTTPSConnection("chatgpt-4-bing-ai-chat-api.p.rapidapi.com")

payload = "bing_u_cookie=%3C1HiutJwqPjTWW2VAwwvkqGeglRp4_oG7_YMcRR44O0HBE-Z6xpAnC6fz8EPimOn8RtlDw6H0I9Rk1fTh5gJI1V4aewyP0olBpBED0upuOVaLwDvr70WOQRQ4aJPIz6O1xFYui8pACa39dwupZpH_P_1S5H6XA-QKR3uM2dr4-pgFVCYcyD9KvVImdnqFHhDjKAPnkIdY0dkdwpnyPTGOCYg%3E&question=Give%20me%203%20examples%20of%20how%20I%20can%20use%20you."

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'X-RapidAPI-Key': "28290b323fmshe033439f8e21c87p1d253cjsn9438d52a3d39",
    'X-RapidAPI-Host': "chatgpt-4-bing-ai-chat-api.p.rapidapi.com"
}

conn.request("POST", "/chatgpt-4-bing-ai-chat-api/0.2/send-message/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))