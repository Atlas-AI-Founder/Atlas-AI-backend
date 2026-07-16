from flask import Flask, request, Response, render_template
from twilio.twiml.messaging_response import MessagingResponse
from atlas_brain import ask_atlas

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/reply_whatsapp", methods=["POST"])
def reply_whatsapp():
    incoming = request.form.get("Body", "")

    reply = ask_atlas(incoming)

    resp = MessagingResponse()
    resp.message(reply)

    return Response(str(resp), mimetype="text/xml")

if __name__ == "__main__":
    app.run(debug=True)
