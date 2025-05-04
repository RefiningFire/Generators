



import tools.dice as d
from treas_type_tables import gritty_ttt as gttt


treas_type_selection = input('What Treasure type letter? ').capitalize()

gttt.treasure_type_table_roll(treas_type_selection)
