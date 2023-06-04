# WRITE YOUR FUNCTIONS HERE 
#lists with numbers
#dictionarys are called with name_ofdictionary["nameofpartofit"]
def get_pet_shop_name(name):
    return (name["name"])

def get_total_cash(cash):
    return (cash["admin"]["total_cash"])


def add_or_remove_cash(pet_shop , num): 
    pet_shop["admin"]["total_cash"] += num
    

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(sold , num):
    sold["admin"]["pets_sold"] += num
    
def get_stock_count(instock_pets):
    count=len(instock_pets["pets"])
    return count



    
def get_pets_by_breed(petshop, breed):
    pets =[]
    for animal in petshop["pets"]:
        if animal["breed"] == breed:
            pets.append(animal)
    return pets


def find_pet_by_name(petshop,animal_name):
    pet= None
    for animal in petshop["pets"]:
        if animal["name"] == animal_name:
            pet=animal
            break
    return pet

def remove_pet_by_name(petshop,animal_name):
    for animal in petshop["pets"]:
        if animal["name"] == animal_name:
            pet=animal
            petshop["pets"].remove(pet)


def add_pet_to_stock(pet_list,new_pet):
    pet_list["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer , comition):
    customer["cash"]= customer["cash"] - comition


def get_customer_pet_count(customer):
    count=0
    for pet in customer["pets"]:
        count += 1
    return count

def add_pet_to_customer(customer,his_new_pet):
    customer["pets"].append(his_new_pet)