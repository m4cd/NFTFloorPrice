import string

class Wallet:
    def __setAddress(self, address):
        try:
            self.__address = None

            if address[:2] != "0x":
                raise ValueError("Incorrect format of the address not starting with \"0x\"")
            '''if len(address) != 42:
                raise ValueError("Incorrent length of the address")'''
            if all(c in string.hexdigits for c in address[2:]) == False:
                raise ValueError("Address contains incorrect digits")
            self.__address = address
        except Exception as e:
            print(e)

    def __init__(self, address):
        self.__setAddress(address)

    def __repr__(self):
        return f"Wallet address: {self.getAddress()}"
    
    def getAddress(self):
        return self.__address
    
