text_file = open(r"C:\Users\daniel.chancir\Desktop\Autoestudio\codember\challenge03\colors.txt")
colors = text_file.read()[1:-1].split(', ')
colors = [element.replace('\n  ', '').replace('\n', '').replace('"', '') for element in colors]

'''Variables'''
maxZebraCount = 0
maxZebraColor = ''

lastColor = ''
nextColor = colors[0]
currentZebraCount = 1

for color in colors:
    if (color != nextColor or color == lastColor):
        currentZebraCount = 1
    currentZebraCount+= 1
    nextColor = lastColor
    lastColor = color
    if (currentZebraCount >= maxZebraCount):
        maxZebraCount = currentZebraCount
        maxZebraColor = lastColor
print(maxZebraColor, maxZebraCount)
