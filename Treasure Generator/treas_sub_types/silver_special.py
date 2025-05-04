
import random as r
import tools.dice as d

def treasure():
    roll = d._1d(20)
    if roll == 1:
        return ['cp',10000]
    elif roll == 2:
        type = r.choice(['beaver','fox','rabbit'])
        return [f'bundles of {type} pelts, worth 15gp each (3 stone each)',d._2d(6)]
    elif roll == 3:
        return ['rolls of woven textiles, worth 30gp each (4 stone each)',d._1d(6)]
    elif roll == 4:
        return ['jars of dyes and pigments, worth 50gp each (5 stone each)',d._1d(3)]
    elif roll == 5:
        return ['bags of loose herbs, worth 75gp each (5 stone each)',d._1d(2)]
    elif roll == 6:
        return ['bags of clothing, worth 75gp each (5 stone each)',d._1d(2)]
    elif roll == 7:
        return ['crates of tools, worth 75gp each (5 stone each)',d._1d(2)]
    elif roll == 8:
        return ['crate of armor and weapons, worth 110gp (5 stone)',1]
    elif roll == 9:
        type = r.choice(['boar tusks','bull horns','deer antlers'])
        value = d._1d(10)
        return ['{type} worth {value}gp each (1 stone per 10gp value)',d._4d(8)]
    elif roll == 10:
        return ['captured or enslaved laborers, worth 40gp each (15 stone each if unconscious)',d._1d(4)]
    elif roll == 11:
        return [f'captured or enslaved domestic servants, worth 100gp each (15 stone if unconscious)',1]
    elif roll == 20:
        return ['gp',100]
    else:
        return ['sp',1000]
