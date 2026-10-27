class Device:
    
    def __init__(self,brand,**kwargs):
        super().__init__(**kwargs)
        self.brand=brand
        
    def show_brand(self):
        print("Brand is :",self.brand)
        
        
class Phone(Device):
    
    def __init__(self,secren_size,**kwargs):
        super().__init__(**kwargs)
        self.secren_size=secren_size
        
    def make_call(self):
        print("its calls..!")
        
class Camera(Device):
    
    def __init__(self,resolution,**kwargs):
        super().__init__(**kwargs)
        self.resolution=resolution
        
    def take_photo(self):
        print("save photo :",self.resolution)
        

class SmartPhone (Phone,Camera):
    
    def __init__(self,brand,secren_size,resolution):
        super().__init__(brand=brand,secren_size=secren_size,resolution=resolution)
        
    def show_smartphone(self):
        self.show_brand()
        print(self.secren_size)
        self.take_photo()
        self.make_call()
        

my_phone=SmartPhone("Apple",780,"4K (1080)")
my_phone.show_smartphone()