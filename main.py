import requests
import json
from time import time
import jwt
from pprint import pprint
from send import send

zoom_api_key = "1KNPJihvR3Sy-XMErnaBPg"
zoom_api_secret = "zVRnpE3bsoghOjMlZahEP872cBygrjJeKz8J"
token = jwt.encode(
        {'iss': zoom_api_key, 'exp': time() + 5000},
        zoom_api_secret,
        algorithm='HS256'
)
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}
meeting_details = {
                  "topic": "Test",
                  "type": 2,
                  "start_time": "2019-06-14T10: 21: 57",
                  "duration": "45",
                  "timezone": "Europe/Moscow",
                  "agenda": "Test",

                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                                "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "False",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
}
url_start_confa = f'https://api.zoom.us/v2/users/me/meetings'
response = requests.post(url_start_confa, headers=headers, data=json.dumps(meeting_details))
response.raise_for_status()

print(response.json()["password"], response.json()["join_url"])
email_send = ["xuxlaevoleg@yandex.ru", "ezabid@yandex.ru"]
for email in email_send:
    slova = f" Вы риглашены на конференцию зум.Вот ссылка {response.json()['join_url']} Пароль {response.json()['password']}"
    send("gogikorotkov@yandex.ru", email_send, slova, "Dmitri77")
print(slova)
