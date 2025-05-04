'''Book name should definitly be determined by the Topic, and modified by the scope and complexity. Also perhaps Age. Volumes will perhaps be named individually.

Sample of Complexity Names:
.75
An Introduction to...
The Art of...
1
The history of...
2
An In-depth exploration of...
3
The Compleat treatise on...
4
The Intersection of Life, Consciousness, and...
5
Mystery and Enlightenment: this being the supreme elucidation of
6
Unique name
7
Can this even exist?


Sample of Scope names:
1
...in Zhelasier
2
...of the ancients
3
...within the Empire
4
...of the known world
'''


import random as random

book_topic_roll = random.randint(1,1000)

''' there should be general book titles, or beginning/endings, that are also selected from when it comes to the specific book title
general_book_topic_cores
'''

if book_topic_roll >= 1 and book_topic_roll <= 5:
    book_topic = 'Acrobatics'
    book_title_core = random.choice([
    'Jumping',
    'Acrobatics',
    'An Acrobat'
    ])
elif book_topic_roll >= 6 and book_topic_roll <= 15:
    book_topic = 'Alchemy'
    book_title_core = random.choice([
    'The Transmutation of the Self',
    'Alchemical Processes',
    'An Alchemist'
    ])
elif book_topic_roll >= 16 and book_topic_roll <= 20:
    book_topic = 'Alertness'
elif book_topic_roll >= 21 and book_topic_roll <= 25:
    book_topic = 'Ambushing'
elif book_topic_roll >= 26 and book_topic_roll <= 30:
    book_topic = 'Animal Husbandry'
elif book_topic_roll >= 31 and book_topic_roll <= 35:
    book_topic = 'Animal Training (dogs)'
elif book_topic_roll >= 36 and book_topic_roll <= 40:
    book_topic = 'Animal Training (horses)'
elif book_topic_roll >= 41 and book_topic_roll <= 45:
    book_topic = 'Animal Training (falcons)'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 51 and book_topic_roll <= 55:
    book_topic = 'Arcane Dabbling'
elif book_topic_roll >= 56 and book_topic_roll <= 60:
    book_topic = 'Art (calligraphy)'
elif book_topic_roll >= 61 and book_topic_roll <= 65:
    book_topic = 'Art (drawing)'
elif book_topic_roll >= 66 and book_topic_roll <= 70:
    book_topic = 'Art (illumination)'
elif book_topic_roll >= 71 and book_topic_roll <= 80:
    book_topic = 'Art (mosaic)'
elif book_topic_roll >= 81 and book_topic_roll <= 85:
    book_topic = 'Art (painting)'
elif book_topic_roll >= 86 and book_topic_roll <= 90:
    book_topic = 'Art (sculpture)'
elif book_topic_roll >= 91 and book_topic_roll <= 95:
    book_topic = 'Art (stained glass)'
elif book_topic_roll >= 96 and book_topic_roll <= 100:
    book_topic = 'Bargaining'
elif book_topic_roll >= 101 and book_topic_roll <= 110:
    book_topic = 'Battle Magic'
elif book_topic_roll >= 111 and book_topic_roll <= 115:
    book_topic = 'Beast Friendship'
elif book_topic_roll >= 116 and book_topic_roll <= 120:
    book_topic = 'Berserkergang'
elif book_topic_roll >= 121 and book_topic_roll <= 130:
    book_topic = 'Black Lore of Zahar'
elif book_topic_roll >= 131 and book_topic_roll <= 135:
    book_topic = 'Blind Fighting'
elif book_topic_roll >= 136 and book_topic_roll <= 140:
    book_topic = 'Bribery'
elif book_topic_roll >= 141 and book_topic_roll <= 145:
    book_topic = 'Caving'
elif book_topic_roll >= 146 and book_topic_roll <= 150:
    book_topic = 'Cat Burglary'
elif book_topic_roll >= 151 and book_topic_roll <= 155:
    book_topic = 'Climbing'
elif book_topic_roll >= 156 and book_topic_roll <= 165:
    book_topic = 'Collegiate Wizardry'
elif book_topic_roll >= 166 and book_topic_roll <= 170:
    book_topic = 'Combat Reflexes'
elif book_topic_roll >= 171 and book_topic_roll <= 180:
    book_topic = 'Combat Trickery'
elif book_topic_roll >= 181 and book_topic_roll <= 185:
    book_topic = 'Command'
elif book_topic_roll >= 186 and book_topic_roll <= 190:
    book_topic = 'Contemplation'
elif book_topic_roll >= 191 and book_topic_roll <= 195:
    book_topic = 'Contortionism'
elif book_topic_roll >= 196 and book_topic_roll <= 200:
    book_topic = 'Craft (armor-making)'
elif book_topic_roll >= 201 and book_topic_roll <= 205:
    book_topic = 'Craft (baking)'
elif book_topic_roll >= 206 and book_topic_roll <= 210:
    book_topic = 'Craft (basket-making)'
elif book_topic_roll >= 211 and book_topic_roll <= 215:
    book_topic = 'Craft (blacksmithing)'
elif book_topic_roll >= 216 and book_topic_roll <= 220:
    book_topic = 'Craft (book-binding)'
elif book_topic_roll >= 221 and book_topic_roll <= 225:
    book_topic = 'Craft (bow-making)'
elif book_topic_roll >= 226 and book_topic_roll <= 230:
    book_topic = 'Craft (brewing)'
elif book_topic_roll >= 231 and book_topic_roll <= 235:
    book_topic = 'Craft (candle-making)'
elif book_topic_roll >= 236 and book_topic_roll <= 240:
    book_topic = 'Craft (carpentry)'
elif book_topic_roll >= 241 and book_topic_roll <= 245:
    book_topic = 'Craft (cobbling)'
elif book_topic_roll >= 246 and book_topic_roll <= 250:
    book_topic = 'Craft (cooking)'
elif book_topic_roll >= 251 and book_topic_roll <= 255:
    book_topic = 'Craft (doll-making)'
elif book_topic_roll >= 256 and book_topic_roll <= 260:
    book_topic = 'Craft (dying)'
elif book_topic_roll >= 261 and book_topic_roll <= 265:
    book_topic = 'Craft (embroidery)'
elif book_topic_roll >= 266 and book_topic_roll <= 270:
    book_topic = 'Craft (fletching)'
elif book_topic_roll >= 271 and book_topic_roll <= 280:
    book_topic = 'Craft (leatherworking)'
elif book_topic_roll >= 281 and book_topic_roll <= 285:
    book_topic = 'Craft (lock-smithing)'
elif book_topic_roll >= 286 and book_topic_roll <= 290:
    book_topic = 'Craft (rune-carving)'
elif book_topic_roll >= 291 and book_topic_roll <= 295:
    book_topic = 'Craft (saddlery)'
elif book_topic_roll >= 296 and book_topic_roll <= 300:
    book_topic = 'Craft (scribing)'
elif book_topic_roll >= 301 and book_topic_roll <= 305:
    book_topic = 'Craft (scrivening)'
elif book_topic_roll >= 306 and book_topic_roll <= 310:
    book_topic = 'Craft (stonemason)'
elif book_topic_roll >= 311 and book_topic_roll <= 315:
    book_topic = 'Craft (tanning)'
elif book_topic_roll >= 316 and book_topic_roll <= 320:
    book_topic = 'Craft (tinkering)'
elif book_topic_roll >= 321 and book_topic_roll <= 325:
    book_topic = 'Craft (weaving)'
elif book_topic_roll >= 326 and book_topic_roll <= 330:
    book_topic = 'Craft (weaponsmithing)'
elif book_topic_roll >= 331 and book_topic_roll <= 335:
    book_topic = 'Craft (wheelwright)'
elif book_topic_roll >= 336 and book_topic_roll <= 340:
    book_topic = 'Diplomacy'
elif book_topic_roll >= 341 and book_topic_roll <= 345:
    book_topic = 'Disguise'
elif book_topic_roll >= 346 and book_topic_roll <= 350:
    book_topic = 'Dungeon Bashing'
elif book_topic_roll >= 351 and book_topic_roll <= 355:
    book_topic = 'Dwarven Brewing'
elif book_topic_roll >= 356 and book_topic_roll <= 360:
    book_topic = 'Eavesdropping'
elif book_topic_roll >= 361 and book_topic_roll <= 365:
    book_topic = 'Elementalism'
elif book_topic_roll >= 366 and book_topic_roll <= 370:
    book_topic = 'Endurance'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'
elif book_topic_roll >= 46 and book_topic_roll <= 50:
    book_topic = 'Apostasy'

else:
    print("ERROR: BOOK TOPIC ROLL DOES NOT HAVE THIS NUMBER")
    print("NUMBER ROLLED:")
    print(book_topic_roll)

print(book_topic)
