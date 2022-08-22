from flask import jsonify
from datetime import datetime, date, timedelta
import time
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd


def exceptionAsAJson(cause, e):
    return jsonify({
        "caused at": str(cause),
        "error": str(e)
    })


def successAsJson():
    return jsonify({
        "status": "success"
    })


def successAsJsonWithObj(obj):
    return jsonify({
        "status": "success",
        "object": obj
    })


def getDateTimeInMillis():
    return round(time.time() * 1000)


def getDateTimeInTimestamp(millis):
    date_time_obj = datetime.fromtimestamp(millis / 1000)
    returnable = date_time_obj.strftime("%m/%d/%Y, %H:%M:%S")
    return returnable


def getTodayDate():
    return date.today()


def getTomorrowDate():
    return date.today() + timedelta(days=1)


def checkTwoDateMatch(d1, d2):
    return d1 == d2


def extract_text_from_pdf():
    pass


def sentiment_analysis(text):
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob')
    doc = nlp(text)
    sentiment = doc._.blob.polarity
    print(sentiment)
