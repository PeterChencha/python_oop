class OperatingSystem(object):
    """docstring for OperatingSystem."""
    multitasking = True
    name = "Windows OS"


class Microsoft(object):
    """docstring for Microsoft."""
    website = "www.microsoft.com"
    name = "Microsoft Pro"


class Surface(OperatingSystem, Microsoft):
    """docstring for Surface."""

    def __init__(self):
        if self.multitasking is True:
            print("This is a multitasking system. Visit {} for more detals".
                  format(self.website))
            print("Name: ", self.name)


surface = Surface()
