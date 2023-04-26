class ml:
    def __init__(self):
        pass
    def function(self):
        print("activate func", self.val)

class derivative(ml):
    def __init__(self, val):
        super().__init__()
        self.val = val

m = derivative("test")

m.function()