# Made by Niko
# https://twitter.com/niko_abyss
import openai
import json
from PIL import Image
import os

# Insert your API key here
openai.api_key = 'YOUR-API-KEY-HERE'

# Get phrase
phrase = input("Word: ")
phrase = phrase.replace(" ", "_").lower()

# Get completion
response = openai.Completion.create(model="text-davinci-002", prompt="# Pride flag dataset, contains lists with hex codes of colors on each pride flag\n\nlgbt = ['#E50000', '#FF8D00', '#FFEE00', '#008121', '#004CFF, '#760088']\ntransgender = ['#5CCEFA', '#F4A9B7', '#FFFFFF', '#F4A9B7', '#5CCEFA']\n" + phrase + " =", temperature=0.5, max_tokens=700, stop="\n")

# Turn completion into list
result = json.loads(str(response))
colors = eval(result['choices'][0]['text'])

print('Completion recieved')

# Turn list into flag
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


lc = len(colors)
image = Image.new('RGB', (lc*14, lc*10), 'white')
x = 0
for color in colors:
    rgb = hex_to_rgb(color)
    rgb = (rgb[0], rgb[1], rgb[2])
    for h in range(0,10):
        for i in range(0, lc*14):
            image.putpixel((i, x*10 + h), rgb)
    x += 1

print(colors)
image.save('flags/' + phrase + '.png')
os.startfile('flags\\' + phrase + '.png')