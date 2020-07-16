from appliances import DishWasher
from appliances import Refrigerator
from appliances import CanOpener
from appliances import CoffeeMaker
from appliances import Stove
from appliances import Dryer
from appliances import Washer

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "electric")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

grandmas_rusty_can_opener = CanOpener("rust")
grandmas_rusty_can_opener.open_can()
