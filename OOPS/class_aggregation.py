class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
        self.display_address()
        

    def display_address(self):
        print(self.address.city,self.address.pin,self.address.state)

    def edit_details(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_state)
    def __str__(self):
        return "name:-{}\npin:-{}\ncity:-{}\nstate:{}".format(self.name,self.address.pin,self.address.city,self.address.state)


class Address():
    def __init__(self,city,pin,state):
        self.city = city
        self.pin = pin
        self.state = state
    def edit_address(self,new_city,new_pin,new_state):
        self.city = new_city
        self.state = new_state
        self.pin = new_pin


add1 = Address("Bhilai",490023,"CG")
C1 = Customer("niral","female",add1)
C1.edit_details(new_pin= 124 , new_state= "chhattishgarh", new_city= "supela",new_name= "jai mata di ")
print(C1)
