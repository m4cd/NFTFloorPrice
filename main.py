from wallet import Wallet

def main():
    address = input("Please provide your wallet's address:")
    wallet = Wallet(address)
    print(wallet)
    
main()