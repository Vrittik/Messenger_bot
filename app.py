from flask import Flask,request
from pymessenger.bot import Bot
app=Flask(__name__)
bot=Bot("EAACzAIK1v8QBACSAtcIa43MsDE2ZAqwXZBb2ZCoRZCCW9Gw8weHP6PndUPh1ALtU7lY0sJpp0dFCexeW2IxZB1onZAAgEMb8C723Iq0d5SSdFtNSr5XW7LMxdJ9D4JGzlJTnCtlnqPNIhQZAqR04Cjj8ZAIDQvcKOsqMqt8swnDyI6GZCXn3h3GZAO")
@app.route("/",methods=["GET"])
def verify():
    if request.args.get("hub.challenge"):
        return request.args.get("hub.challenge")
    else:
        return "Please run it on facebook dev"

@app.route("/",methods=["POST"])
def message():
    data=request.get_json()
    print(data)
    if data["entry"]:
        for entry in data["entry"]:
            if entry["messaging"]:
                for messaging in entry["messaging"]:
                    if messaging["sender"]["id"]:
                        user=(messaging["sender"]["id"])
                    if messaging["message"]:
                        mes=messaging["message"]
                        text=(messaging["message"]["text"])+" by bot"
                        bot.send_text_message(user,text)

    return "verified"
@app.after_request
def add_header(response):

    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

app.run()