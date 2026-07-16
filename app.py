from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/reply_whatsapp", methods=["POST"])
def reply_whatsapp():
    incoming = request.form.get("Body", "")

    resp = MessagingResponse()
    resp.message(f"Atlas AI received: {incoming}")

    return Response(str(resp), mimetype="text/xml")

if __name__ == "__main__":
    app.run(debug=True)