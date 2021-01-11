# THIS WILL PUSH IMAGES TO TWITTER
# HOSTED ON HEROKU SERVER

import base64
import tweepy
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler

client = MongoClient('''REDACTED''')
print("[MONGODB] Connection established")
db = client.meme_bot

# Check for a new image
def check_img():
    
    if db.images.count() != 0:

        for i in db.images.find():

            imgName = i["fileName"]
            imgContents = base64.b64decode(i["fileContents"])
            
            print("[MONGODB] Image recieved")

            post_img(imgName, imgContents)

            break


CONSUMER_KEY = '''REDACTED'''
CONSUMER_SECRET = '''REDACTED'''
ACCESS_TOKEN = '''REDACTED'''
ACCESS_SECRET = '''REDACTED'''

def post_img(imgName, imgContents):

    # FIXME Convert bytearray into PIL image file

    with open("image.jpg", "wb") as img:

        img.write(imgContents)

    def OAuth():

        try:

            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
            return auth
        
        except Exception as e:

            return None

    
    oauth = OAuth()
    api = tweepy.API(oauth)
    print("[TWITTER] Connection established")

    text = "#meme #memes #funny #smile #laugh #dankmemes #mymemebot"

    api.update_with_media("image.jpg", text)
    print("[TWITTER] Image posted")

    db.images.delete_one({"fileName": imgName})
    print("[MONGODB] Document deleted")
    

scheduler = BlockingScheduler()
scheduler.add_job(check_img, 'interval', hours=1)
scheduler.start()
