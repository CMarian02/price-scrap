class TextInput:
    def __init__(self, page, locator):
        self.text_input = page.locator(locator)

    def fill(self, value):
        self.text_input.click()
        self.text_input.clear()
        self.text_input.fill(value)
    
    def clear(self):
        self.text_input.clear()
    
    def value(self):
        return self.text_input.input_value()