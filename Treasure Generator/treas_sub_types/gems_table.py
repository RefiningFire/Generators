

import random as r
import tools.dice as d

def gem_value(type):
    if type == 'ornamental':
        roll = d._2d(20)
    elif type == 'gem':
        roll = d._1d(100)
    elif type == 'brilliant':
        roll = d._1d(100) + 80

    if roll <= 10:
        return [r.choice(['azurite ','hematite ','malachite ','obsidian ','quartz '])+type+'s worth 10gp each',1]
    elif roll <= 25:
        return [r.choice(['agate ','lapis lazuli ','tiger eye ','turquoise '])+type+'s worth 25gp each',1]
    elif roll <= 40:
        return [r.choice(['bloodstone ','crystal ','citrine ','jasper ','moonstone ','onyx '])+type+'s worth 50gp each',1]
