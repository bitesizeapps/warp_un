from datetime import datetime, timedelta

def getTime():
    return datetime.now()


def getFutureTime(minutes):
    current_time = datetime.now()
    future_time = current_time + timedelta(minutes=minutes)
    return future_time
