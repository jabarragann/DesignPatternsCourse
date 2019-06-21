class Component(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass

class Child(Component):

    def __init__(self,*args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

    def component_function(self):
        print("{}".format(self.name))


class Composite(Component):

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        self.name = args[0]
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        print("{}".format(self.name))

        for i in self.children:
            i.component_function()


sub1 = Composite("submenu1")

sub11 = Child("sub_submenu 11")
sub12 = Child("sub_submenu 12")
sub1.append_child(sub11)
sub1.append_child(sub12)

top = Composite("top_menu")

sub2 = Composite("submenu2")
sub21 = Child("sub_submenu 21")
sub2.append_child(sub21)

top.append_child(sub1)

top.append_child(sub2)

top.component_function()


