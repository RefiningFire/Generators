
import tools.dice as d
from treas_sub_types import copper_special
from treas_sub_types import silver_special
from treas_sub_types import ornamentals_special


def get_new_value(new_i,treas_d):
    if new_i[0] in treas_d:
        new_v = new_i[1] + treas_d.get(new_i[0])
    else:
        new_v = new_i[1]
    return new_v

def treasure_type_table_roll(treas_type):
    treas_dict = {}

    if treas_type == 'A':
        # Copper
        if d._1d(100) <= 30:
            for x in range(d._2d(4)):
                new_item = copper_special.treasure()
                new_value = get_new_value(new_item,treas_dict)
                treas_dict.update({new_item[0]:new_value})
        # Silver
        if d._1d(100) <= 30:
            for x in range(d._1d(3)):
                new_item = silver_special.treasure()
                new_value = get_new_value(new_item,treas_dict)
                treas_dict.update({new_item[0]:new_value})
        # Gems
        if d._1d(100) <= 100: #changevto 30
            for x in range(d._1d(400)): #changevto 4
                new_item = ornamentals_special.treasure()
                new_value = get_new_value(new_item,treas_dict)
                treas_dict.update({new_item[0]:new_value})

    elif treas_type == 'B':
        pass
    elif treas_type == 'C':
        pass
    elif treas_type == 'D':
        pass
    elif treas_type == 'E':
        pass
    elif treas_type == 'F':
        pass
    elif treas_type == 'G':
        pass
    elif treas_type == 'H':
        pass
    elif treas_type == 'I':
        pass
    elif treas_type == 'J':
        pass
    elif treas_type == 'K':
        pass
    elif treas_type == 'L':
        pass
    elif treas_type == 'M':
        pass
    elif treas_type == 'N':
        pass
    elif treas_type == 'O':
        pass
    elif treas_type == 'P':
        pass
    elif treas_type == 'Q':
        pass
    elif treas_type == 'R':
        pass


    print()
    for k, v in treas_dict.items():
        print(v,k)



    return
