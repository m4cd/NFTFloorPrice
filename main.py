from wallet import Wallet
from etherscan import Etherscan

def main():
    address = input("Please provide your wallet's address: ")
    
    wallet = Wallet(address)

    print(wallet)
    etherscan = Etherscan(wallet)
    print(etherscan)
    etherscan.parse()
    
main()