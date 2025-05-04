
import random as r
import tools.dice as d
import treas_sub_types.gems_table as gt

def treasure():
    roll = d._1d(12)
    if roll == 1:
        return ['silver arrows, each worth 5gp',d._1d(12)]
    elif roll == 2:
        type = r.choice(['lungwort','willowbark'])
        return [f'pouches of {type}, worth 5gp each (1/6 stone each)',d._1d(12)]
    elif roll == 3:
        type = r.choice(['birthwort','comfrey','goldenrod','woundwort'])
        return [f'pouches of {type} worth 10gp each (1/6 stone each)',d._1d(6)]
    elif roll == 4:
        type = r.choice(['aloe','belladonna','bitterwood','blessed thistle','wolfsbane'])
        return [f'pouches {type} worth 10gp each (1/6 stone each)',d._1d(6)]
    elif roll == 5:
        return ['pouches of horsetail, worth 15gp each (1/6 stone each)',d._1d(4)]
    elif roll == 6:
        return ['vials of holy water, worth 25gp each (1/6 stone each)',d._1d(2)]
    else:
        return gt.gem_value('ornamental')
