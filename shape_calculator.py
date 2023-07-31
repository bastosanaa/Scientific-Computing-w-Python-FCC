
class Rectangle:
    
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.height
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return self.diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        wid = "*" * self.width + "\n" 
        picture = wid * self.height
        return picture
    
    def get_amount_inside(self, shape):
        amount_width = int(self.width / shape.width)
        amount_height = int(self.height / shape.height)
        amount = amount_height * amount_width
        return amount
                
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)

    def __str__(self):
        return f"Square(side={self.width})"
