class Smartphone:  
    def __init__(self, brand, model, storage_capacity, is_5g_enabled):  
        self.brand = brand  
        self.model = model  
        self.storage_capacity = storage_capacity  # in GB  
        self.is_5g_enabled = is_5g_enabled  

    def make_call(self, number):  
        return f"Calling {number} from {self.brand} {self.model}..."  

    def send_message(self, number, message):  
        return f"Sending message to {number}: {message}"  

    def check_internet(self):  
        if self.is_5g_enabled:  
            return f"{self.brand} {self.model} is connected to a 5G network."  
        else:  
            return f"{self.brand} {self.model} is not connected to 5G."  

class GamingSmartphone(Smartphone):  
    def __init__(self, brand, model, storage_capacity, is_5g_enabled, has_external_gamepad):  
        super().__init__(brand, model, storage_capacity, is_5g_enabled)  
        self.has_external_gamepad = has_external_gamepad  

    def play_game(self, game_name):  
        return f"Playing {game_name} on {self.brand} {self.model} with {'an external gamepad' if self.has_external_gamepad else 'no external gamepad'}."  

# Example of instantiating objects   
my_phone = Smartphone("Apple", "iPhone 14", 128, True)  
my_gaming_phone = GamingSmartphone("ASUS", "ROG Phone 6", 512, True, True)  

# Use the methods  
print(my_phone.make_call("123456789"))  
print(my_gaming_phone.play_game("Genshin Impact"))