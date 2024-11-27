'''
Nick DeMaestri
11/27/2024
CS-391

Gemini Zebra Counter
Based on code provided from: https://github.com/gnolankettering/lecture13/blob/main/gemini/app1.py
'''

import google.generativeai as genai
import config
import PIL.Image

genai.configure(api_key=config.GEMINI_API_KEY)

img = PIL.Image.open('zebras.jpg')
model = genai.GenerativeModel('gemini-1.5-flash')
#response = model.generate_content(img)

response = model.generate_content(["Please identify how many zebras are in the image attached. \
                                   Along with identifying a count of how many there are, please \
                                   inform the user of the location of each zebra.", img], stream=True)
response.resolve()

print(response.text)



