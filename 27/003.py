my_shopping_list = ["Miraj","Bubu","Dudu"]
# To remove the dulicate in the list using --> set
print(my_shopping_list)
print(len(my_shopping_list))

def bring_more_item(my_list):
    my_list.append("Buau0")
    # my_list.remove()
    my_list.insert(1,"Buau0")

    return my_list
l = bring_more_item(my_shopping_list)
print(l)