class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return self.width * 2 + self.height * 2
    
    def get_diagonal(self):
        return round((self.width ** 2 + self.height ** 2) ** .5, 2)
    
    def get_picture(self):
        pic = "*"
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return (pic * self.width + '\n') * self.height
    
    def get_amount_inside(self, width, height):
        total = 0
        if int(self.width / width) > 0 and int(self.height / height) > 0:
            total = int(self.width / width) * int(self.height / height)
        return total
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
        
class Square(Rectangle): 

    def __init__(self, side):
        self.width = side
        self.height = side
    
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.height = side
        self.width = side
    
    def __str__(self):
        return f'Square(side={self.width})'
    


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_width(4)
rect.set_height(5)
print(rect.get_perimeter())
print(rect.get_diagonal())
print(rect.get_picture())
print(rect)
sq = Square(2)
print(rect.get_amount_inside(4,4))
sq.set_side(5)
print(rect.get_picture())
print(sq.get_perimeter())
print(sq)