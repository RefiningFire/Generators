

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
    elif roll <= 55:
        return [r.choice(['carnelian ','chalcedony ','sardonyx ','zircon '])+type+'s worth 75gp each',1]
    elif roll <= 70:
        return [r.choice(['amber ','amethyst ','coral ','jade ','jet ','tourmaline '])+type+'s worth 100gp each',1]
    elif roll <= 80:
        return [r.choice(['garnet ','pearl ','spinel '])+type+'s worth 250gp each',1]
    elif roll <= 90:
        return [r.choice(['aquamarine ','alexandrite ','topaz '])+type+'s worth 500gp each',1]
    elif roll <= 95:
        return [r.choice(['opal ','star ruby, ','star sapphire ','sunset amethyst ','imperial topaz '])+type+'s worth 750gp each',1]
    elif roll <= 100:
        return [r.choice(['black sapphire, ','diamond ','emerald ','jacinth ','ruby '])+type+'s worth 1,000gp each',1]
