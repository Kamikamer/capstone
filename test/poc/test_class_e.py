from icecream import ic

class MagicBox:
    def __init__(self):
        self._items = []
        # This is a private attribute (encapsulated)
        self.__items = []

    def add_item(self, item) -> None:
        self._items.append(item)
        self.__items.append(item)

    def get_items(self) -> list:
        return self._items
    
    def get__items(self) -> list:
        # This method provides controlled access to the items (encapsulated)
        return self.__items

if __name__ == "__main__":
  ic.configureOutput(prefix='Private variables (ツ)_/¯ ')
  my_box = MagicBox()

  # Trying to directly access the private attribute (will result in an error)

  # Adding items through a method
  my_box.add_item("Gold coin")
  my_box.add_item("Magical wand")

  # # Getting items through a method
  # ic("Items in the box:", my_box._items) # ['Gold coin', 'Magical wand'] <- works

  ic(f"Items with 1 underscores: {my_box.get_items()}")
  try:
    ic(my_box.__items) # Errors, this is an idealogy of private variable
    pass
  except AttributeError as e:
    # raise e
    pass
  ic(f"Items with 2 underscores: {my_box.get__items()}")