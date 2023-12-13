import requests
import json

headers = {"Authorization":"Bearer XXX","Content-Type":"application/json"}

body = {
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": "true",
  "name": "圖文選單 1",
  "chatBarText": "Rich Menu",
  "areas": [
    {
      "bounds": {
        "x": 0,
        "y": 225,
        "width": 826,
        "height": 733
      },
      "action": {
        "type": "message",
        "text": "1"
      }
    },
    {
      "bounds": {
        "x": 831,
        "y": 229,
        "width": 826,
        "height": 719
      },
      "action": {
        "type": "message",
        "text": "2"
      }
    },
    {
      "bounds": {
        "x": 1661,
        "y": 225,
        "width": 839,
        "height": 720
      },
      "action": {
        "type": "message",
        "text": "3"
      }
    },
    {
      "bounds": {
        "x": 0,
        "y": 957,
        "width": 826,
        "height": 724
      },
      "action": {
        "type": "message",
        "text": "4"
      }
    },
    {
      "bounds": {
        "x": 831,
        "y": 953,
        "width": 817,
        "height": 733
      },
      "action": {
        "type": "message",
        "text": "5"
      }
    },
    {
      "bounds": {
        "x": 1656,
        "y": 945,
        "width": 844,
        "height": 741
      },
      "action": {
                "type": "richmenuswitch",
                "richMenuAliasId": "richmenu-alias-b",
                "data": "richmenu-changed-to-b"
      }
    }
  ]
}

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)