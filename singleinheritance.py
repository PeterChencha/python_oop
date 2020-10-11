class Apple(object):
    """docstring for Apple."""

    def __init__(self):
        super(Apple, self).__init__()
        self.manufacturer = "Apple Inc."
        self.contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("To contact us, log on to ", self.contactWebsite)


class MacBook(Apple):
    """docstring for MacBook."""

    def __init__(self):
        super(MacBook, self).__init__()
        self.yearOfManufacture = "2017"

    def manufacturerDetails(self):
        print("This MacBook was manufactures in {} by {}".format(
            self.yearOfManufacture, self.manufacturer))


macBook = MacBook()
macBook.manufacturerDetails()
macBook.contactDetails()
