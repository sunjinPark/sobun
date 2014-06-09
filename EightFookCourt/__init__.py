from kitchens.kitchen import *
from menus.menu import *
from stores.order import *
from stores.store import *
from stores.store_facade import *

order_list = order_manager()
menu_list = menu_list()
cook_list = cook_manager(order_list)
# store = Paldal()
# store_facade = store_facade()
# store_facade.order_menu("main", "noodle")