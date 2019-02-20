
# name
# avatar (profile picture)
# inventory 

# def do_stuff():
#   pass

class Character(): # class names start with capital letter and are one word
    # the "dunder init" method is the constructor
    def __init__(self, new_name):
        # `self` is the customary way to refer to the instance being built
        # In some other language, they use `this`
        self.name = new_name