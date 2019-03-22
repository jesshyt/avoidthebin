import requests

def send_simple_message(emailto, emailfrom, nameto, name, foodgone):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox07f026dd58cc48ce9ad4b6b2698ee188.mailgun.org/messages",
        auth=("api", "b589d84067bad1f769e5bb4d90002d25-7caa9475-cc069245"),
        data={"from": "Avoid The Bin <mailgun@sandbox07f026dd58cc48ce9ad4b6b2698ee188.mailgun.org>",
              "to": emailto,
              "cc": emailfrom,
              "subject": name + " wants your " + foodgone,
              "text": "Please reply to " + name + " to arrange the pick up of your " + foodgone})
    
