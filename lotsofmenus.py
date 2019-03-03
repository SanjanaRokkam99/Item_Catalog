from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User("name="Sanjana Rokkam", email="sanjanarokkam7@gmail.com","
             "picture='https://www.bing.com/images/search?view=detailV2&id=8F2"
             "224446466D8BB6E729A3DD0E958D782A2379C&thid=OIP.XVQhw3zWkizu6LGmE"
             "vAmqwHaHa&mediaurl=https%3A%2F%2Fwww.hit4hit.org%2Fimg%2Flogin%"
             "2Fuser-icon-6.png&exph=512&expw=512&q=user&selectedindex=18&ajax"
             "hist=0&vt=0&eim=2,6'")
session.add(User1)
session.commit()

# Menu for UrbanBurger
restaurant1 = Restaurant(user_id=1, name="Urban Burger")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem("user_id=1, name="Veggie Burger", description="Juicy gri"
                     "lled veggie patty with tomato mayo and lettu"
                     "ce", "
                     "price="$7.50", course="Entree", restaurant=restaurant1")

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem("user_id=1, name="French Fries", description="with garli"
                     "c and parmesan", "
                     "price="$2.99", course="Appetizer", restaurant=restauran"
                     "t1")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem("user_id=1, name="Chicken Burger", description="Juicy gri"
                     "lled chicken patty with tomato mayo and lettuce", "
                     "price="$5.50", course="Entree", restaurant=restaurant1")

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem("user_id=1, name="Chocolate Cake", description="fresh ba"
                     "ked and served with ice cream", "
                     "price="$3.99", course="Dessert", restaurant=restaurant1")

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem("user_id=1, name="Sirloin Burger", description="Mad"
                     "e with grade A beef", "
                     "price="$7.99", course="Entree", restaurant=restaurant1")

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem("user_id=1, name="Root Beer", description="16oz of refre"
                     "shing goodness", "
                     "price="$1.99", course="Beverage", restaurant=restaurant"
                     "1")

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Iced Tea", description="with Lemon",
                     price="$.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem("user_id=1, name="Grilled Cheese Sandwich", "
                     "description="On texas toast with American Cheese", pri"
                     "ce="$3.49", course="Entree", restaurant=restaurant1")

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem("user_id=1, name="Veggie Burger", description="Mad"
                     "e with freshest of ingredients and home grown spices", "
                     "price="$5.99", course="Entree", restaurant=restaurant1")

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Restaurant(user_id=1, name="Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem("user_id=1, name="Chicken Stir Fry", description="With y"
                     "our choice of noodles vegetables and sauces", "
                     "price="$7.99", course="Entree", restaurant=restaurant2")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem("user_id=1, name="Peking Duck", "
                     "description=" A famous duck dish from Beijing[1] that h"
                     "as been prepared since the imperial era. The meat is pr"
                     "ized for its thin, crisp skin, with authentic version"
                     "s of the dish serving mostly the skin and little meat, s"
                     "liced in front of the diners by the cook", price="$2"
                     "5", course="Entree", restaurant=restaurant2")

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem("user_id=1, name="Spicy Tuna Roll", description="Seare"
                     "d rare ahi, avocado, edamame, cucumber with wasabi so"
                     "y sauce ", "
                     "price="15", course="Entree", restaurant=restaurant2")

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem("user_id=1, name="Nepali Momo ", description="Steamed d"
                     "umplings made with vegetables, spices and meat. ", "
                     "price="12", course="Entree", restaurant=restaurant2")

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem("user_id=1, name="Beef Noodle Soup", description="A Chin"
                     "ese noodle soup made of stewed or red braised beef, be"'
                     "ef broth, vegetables and Chinese noodles.", "
                     "price="14", course="Entree", restaurant=restaurant2")

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem("user_id=1, name="Ramen", description="a Japanese noodl"
                     "e soup dish. It consists of Chinese-style wheat noodle"
                     "s served in a meat- or (occasionally) fish-based brot"
                     "h, often flavored with soy sauce or miso, and uses topp"
                     "ings such as sliced pork, dried seaweed, kamaboko, an"
                     "d green onions.", "
                     "price="12", course="Entree", restaurant=restaurant2")

session.add(menuItem6)
session.commit()


# Menu for Panda Garden
restaurant1 = Restaurant(user_id=1, name="Panda Garden")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem("user_id=1, name="Pho", description="a Vietnamese noodl"
                     "e soup consisting of broth, linguine-shaped rice noodle"
                     "s called banh pho, a few herbs, and meat.", "
                     "price="$8.99", course="Entree", restaurant=restaurant1")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem("user_id=1, name="Chinese Dumplings", description="a comm"
                     "on Chinese dumpling which generally consists of mince"
                     "d meat and finely chopped vegetables wrapped into a pie"
                     "ce of dough skin. The skin can be either thin and elast"
                     "ic or thicker.", "
                     "price="$6.99", course="Appetizer", restaurant=restaurant"
                     "1")

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem("user_id=1, name="Gyoza", description="light seasonin"
                     "g of Japanese gyoza with salt and soy sauce, and i"
                     "n a thin gyoza wrapper", "
                     "price="$9.95", course="Entree", restaurant=restaurant1")

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem("user_id=1, name="Stinky Tofu", description="Taiwanese di"
                     "sh, deep fried fermented tofu served with pickled cabba"
                     "ge.", "
                     "price="$6.99", course="Entree", restaurant=restaurant1")

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem("user_id=1, name="Veggie Burger", description="Juicy gri"
                     "lled veggie patty with tomato mayo and lettuce", "
                     "price="$9.50", course="Entree", restaurant=restaurant1")

session.add(menuItem2)
session.commit()


# Menu for Thyme for that
restaurant1 = Restaurant(user_id=1, name="Thyme for That Vegetarian Cuisine ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem("user_id=1, name="Tres Leches Cake", description="Rich, l"
                     "uscious sponge cake soaked in sweet milk and topped wit"
                     "h vanilla bean whipped cream and strawberries.", "
                     "price="$2.99", course="Dessert", restaurant=restaurant1")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem("user_id=1, name="Mushroom risotto", description="Portab"
                     "ello mushrooms in a creamy risotto", "
                     "price="$5.99", course="Entree", restaurant=restaurant1")

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem("user_id=1, name="Honey Boba Shaved Snow", "
                     "description="Milk snow layered with honey boba, jasmin"
                     "e tea jelly, grass jelly, caramel, cream, and freshly m"
                     "ade mochi", price="$4.50", course="Dessert", restauran"
                     "t=restaurant1")

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem("user_id=1, name="Cauliflower Manchurian", descriptio"
                     "n="Golden fried cauliflower florets in a midly spiced s"
                     "oya,garlic sauce cooked with fresh cilantro, celery, chi"
                     "lies,ginger & green onions", "
                     "price="$6.95", course="Appetizer", restaurant=restauran"
                     "t1")

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem("user_id=1, name="Aloo Gobi Burrito", description="Vega"
                     "n goodness. Burrito filled with rice, garbanzo beans, cu"
                     "rry sauce, potatoes (aloo), fried cauliflower (gobi) an"
                     "d chutney. Nom Nom", "
                     "price="$7.95", course="Entree", restaurant=restaurant1")

session.add(menuItem5)
session.commit()

menuItem2 = MenuItem("user_id=1, name="Veggie Burger", description="Juicy gri"
                     "lled veggie patty with tomato mayo and lettuce", "
                     "price="$6.80", course="Entree", restaurant=restaurant1")

session.add(menuItem2)
session.commit()


# Menu for Tony's Bistro
restaurant1 = Restaurant(user_id=1, name="Tony\'s Bistro ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem("user_id=1, name="Shellfish Tower", description="Lobste"
                     "r, shrimp, sea snails, crawfish, stacked into a delicio"
                     "us tower", "
                     "price="$13.95", course="Entree", restaurant=restaurant1")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem("user_id=1, name="Chicken and Rice", description="Chicke"
                     "n... and rice", "
                     "price="$4.95", course="Entree", restaurant=restaurant1")

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem("user_id=1, name="Mom's Spaghetti", description="Spaghet"
                     "ti with some incredible tomato sauce made by mom", "
                     "price="$6.95", course="Entree", restaurant=restaurant1")

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem("user_id=1, name="Choc Full O\' Mint("Smitten\'s Fres""
                     ""h Mint Chip ice cream"")", "
                     "description="Milk, cream, salt, ..., Liquid nitrogen ma"
                     "gic", price="$3.95", course="Dessert", restaurant=resta"
                     "urant1")

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem("user_id=1, name="Tonkatsu Ramen", description="Noodle"
                     "s in a delicious pork-based broth with a soft-boile"
                     "d egg", "
                     "price="$7.95", course="Entree", restaurant=restaurant1")

session.add(menuItem5)
session.commit()


# Menu for Andala's
restaurant1 = Restaurant(user_id=1, name="Andala\'s")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem("user_id=1, name="Lamb Curry", description="Slow cook tha"
                     "t thang in a pool of tomatoes, onions and alllll thos"
                     "e tasty Indian spices. Mmmm.", "
                     "price="$9.95", course="Entree", restaurant=restaurant1")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem("user_id=1, name="Chicken Marsala", description="Chicke"
                     "n cooked in Marsala wine sauce with mushrooms", "
                     "price="$7.95", course="Entree", restaurant=restaurant1")

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem("user_id=1, name="Potstickers", description="Delicious c"
                     "hicken and veggies encapsulated in fried dough.", "
                     "price="$6.50", course="Appetizer", restaurant=restauran"
                     "t1")

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem("user_id=1, name="Nigiri Sampler", description="Maguro"
                     ", Sake, Hamachi, Unagi, Uni, TORO!", "
                     "price="$6.75", course="Appetizer", restaurant=restauran"
                     "t1")

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem("user_id=1, name="Veggie Burger", description="Juicy gri"
                     "lled veggie patty with tomato mayo and lettuce", "
                     "price="$7.00", course="Entree", restaurant=restaurant1")

session.add(menuItem2)
session.commit()


# Menu for Auntie Ann's
restaurant1 = Restaurant(user_id=1, name="Auntie Ann\'s Diner' ")

session.add(restaurant1)
session.commit()

menuItem9 = MenuItem("user_id=1, name="Chicken Fried Steak", "
                     "description="Fresh battered sirloin steak fried and smo"
                     "thered with cream gravy", price="$8.99", course="Entre"
                     "e", restaurant=restaurant1")

session.add(menuItem9)
session.commit()


menuItem1 = MenuItem("user_id=1, name="Boysenberry Sorbet", description="An u"
                     "nsettlingly huge amount of ripe berries turned into fro"
                     "zen (and seedless) awesomeness", "
                     "price="$2.99", course="Dessert", restaurant=restaurant1")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem("user_id=1, name="Broiled salmon", description="Salmon f"
                     "illet marinated with fresh herbs and broiled hot & fas"
                     "t", "
                     "price="$10.95", course="Entree", restaurant=restaurant1")

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem("user_id=1, name="Morels on toast(seasonal)", "
                     "description="Wild morel mushrooms fried in butter, ser"
                     "ved on herbed toast slices", price="$7.50", course="App"
                     "etizer", restaurant=restaurant1")

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem("user_id=1, name="Tandoori Chicken", description="Chick"
                     "en marinated in yoghurt and seasoned with a spicy m"
                     "ix(chilli, tamarind among others) and slow cooked i"
                     "n a cylindrical clay or metal oven which gets its h"
                     "eat from burning charcoal.", "
                     "price="$8.95", course="Entree", restaurant=restaurant1")

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem("user_id=1, name="Veggie Burger", description="Juicy gri"
                     "lled veggie patty with tomato mayo and lettuce", "
                     "price="$9.50", course="Entree", restaurant=restaurant1")

session.add(menuItem2)
session.commit()

menuItem10 = MenuItem("user_id=1, name="Spinach Ice Cream", description="vani"
                      "lla ice cream made with organic spinach leaves", "
                      "price="$1.99", course="Dessert", restaurant=restauran"
                      "t1")

session.add(menuItem10)
session.commit()


# Menu for Cocina Y Amor
restaurant1 = Restaurant(user_id=1, name="Cocina Y Amor ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem("user_id=1, name="Super Burrito Al Pastor", "
                     "description="Marinated Pork, Rice, Beans, Avocado, Cil"
                     "antro, Salsa, Tortilla", price="$5.95", course="Entre"
                     "e", restaurant=restaurant1")

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem("user_id=1, name="Cachapa", description="Golden brown, c"
                     "orn-based Venezuelan pancake; usually stuffed with ques"
                     "o telita or queso de mano, and possibly lechon. ", "
                     "price="$7.99", course="Entree", restaurant=restaurant1")

session.add(menuItem2)
session.commit()


restaurant1 = Restaurant(user_id=1, name="State Bird Provisions")
session.add(restaurant1)
session.commit()
menuItem1 = MenuItem("user_id=1, name="Chantrelle Toast", description="Crispy"
                     "Toast with Sesame Seeds slathered with buttery chant"
                     "relle mushrooms", "
                     "price="$5.95", course="Appetizer", restaurant=restauran"
                     "t1")
session.add(menuItem1)
session.commit
menuItem1 = MenuItem("user_id=1, name="Guanciale Chawanmushi", "
                     "description="Japanese egg custard served hot with spic"
                     "ey Italian Pork Jowl (guanciale)", price="$6.95", cour"
                     "se="Dessert", restaurant=restaurant1")
session.add(menuItem1)
session.commit()
menuItem1 = MenuItem("user_id=1, name="Lemon Curd Ice Cream Sandwich", "
                     "description="Lemon Curd Ice Cream Sandwich on a chocola"
                     "te macaron with cardamom meringue and cashews", price="$"
                     "4.25", course="Dessert", restaurant=restaurant1")
session.add(menuItem1)
session.commit()
print "added menu items!"
