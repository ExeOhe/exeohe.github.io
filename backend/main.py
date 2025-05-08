#Define Emotions for Greeting to Response
goodfeel = ["good", "excited", "great", "happy", "fantastic", "amazing"]
badfeel = ["bad", "sad", "upset", "angry","tired","exausted","depressed","mad"]

def feeling_response(feeling: str):
    for word in goodfeel:
        if word in feeling:
        print("Hurray ! Im stoked that youre feeling", feeling)
    else:
        for word in badfeel:
        if word in feeling:
        print("I'm so sorry you're going through this", feeling)
        