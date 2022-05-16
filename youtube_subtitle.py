from youtube_transcript_api import YouTubeTranscriptApi
import json

def getYouTubeTranscript(url):
    srt = YouTubeTranscriptApi.get_transcript(url)
    subTitle = ""
    for x in srt:
        # convert dict to str
        js = json.dumps(x)
        # convert str to json
        js = json.loads(js)
        subTitle +=  js["text"] + " "     
    
    return subTitle