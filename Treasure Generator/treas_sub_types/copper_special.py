
import random as r
import tools.dice as d

def treasure():
    roll = d._1d(20)
    if roll == 1:
        type = r.choice(['grain','vegetables'])
        return [f'bags of {type}, worth 5sp each (4 stone each)',d._2d(20)]
    elif roll == 2:
        return ['bricks of salt, worth 7cp each (1/2 stone each)',d._4d(6) * 10]
    elif roll == 3:
        return ['amphorae of beer, worth 1gp each (7 stone each)',d._2d(10)]
    elif roll == 4:
        return ['crates of terra–cotta pottery, worth 0.5gp each (3 3/6 stone each)',d._6d(6)]
    elif roll == 5:
        return ['bundles of hardwood logs, worth 1gp each (6 stone each)',d._2d(10)]
    elif roll == 6:
        return ['amphorae of wine and spirits, worth 1gp each (5 stone each)',d._2d(10)]
    elif roll == 7:
        return ['wheels of cheese, worth 25cp each (1/2 stone each)',d._4d(20)]
    elif roll == 8:
        type = r.choice(['oil','sauce'])
        return [f'amphorae of {type}, worth 1.5gp each (5 stone per jar)',d._2d(6)]
    elif roll == 9:
        return ['amphorae of preserved fish, worth 4.5gp each (10 stone each)',d._1d(3)]
    elif roll == 10:
        return ['small amphorae of preserved meat, worth 5gp each (5 stone each)',d._1d(3)]
    elif roll == 11:
        return [f'crates of glassware, worth 7.5gp each (5 stone each)',d._1d(2)]
    elif roll == 12:
        return ['ingots of common metals, worth 1gp each (1/2 stone each)',d._3d(6)]
    elif roll == 13:
        return ['bundles of rare wood, worth 2gp each (1 stone each)',d._2d(4)]
    elif roll == 20:
        return ['sp',100]
    else:
        return ['cp',1000]
