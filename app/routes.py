from app import app, models
from flask import request
from twilio.twiml.messaging_response import MessagingResponse


@app.route('/', methods=['POST'])
def start():
    guess = request.values.get('Body')
    answer = ''
    data = models.Device.query.all()
    for movie in data:
        if movie.title.lower() == guess.lower():
            answer += f"Yeah, we have show of {movie.title} on Saturday in 15:00"

    if len(answer) == 0:
        answer = "Oops, there is no shows today, better go for a walk to the beach"
    response = MessagingResponse()
    response.message(answer)
    return str(response)
