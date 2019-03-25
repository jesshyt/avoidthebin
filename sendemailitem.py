import requests

def send_simple_message(emailto, emailfrom, nameto, name, foodgone):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxa708cb3a5f024af794f25dceaeab0341.mailgun.org/messages",
        auth=("api", "51d3883f8dd9b3ec895a727675968f07-7caa9475-c2293525"),
        data={"from": "Avoid The Bin <mailgun@sandboxa708cb3a5f024af794f25dceaeab0341.mailgun.org>",
              "to": emailto,
              "cc": emailfrom,
              "subject": name + " wants your " + foodgone,
              "text": "Please reply to " + name + " to arrange the pick up of your " + foodgone})
    
