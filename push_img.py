# THIS WILL BE RUN ON MY PC

import os
import base64
from pymongo import MongoClient

imgFolder = '''REDACTED'''

client = MongoClient('''REDACTED''')
db = client.meme_bot

for i in os.listdir(imgFolder):

    with open(str(os.path.join(imgFolder, i)), "rb") as img:

        imgByte = base64.b64encode(img.read())

        newImg = {"fileName": str(i), "fileContents": imgByte}

        if i[-3:].lower() == "png":

            db.images.insert_one(newImg)

    os.remove(os.path.join(imgFolder, i))
