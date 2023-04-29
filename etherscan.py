import requests
import wallet

import time 

import random

import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class Etherscan:
    def __init__(self, wallet, url="https://etherscan.io", param="nft-transfers?a="):
        self.__wallet = wallet
        self.__url = url
        self.__param = param
    
    def buildUrl(self):
        return f"{self.__url}/{self.__param}{self.__wallet.getAddress()}"

    def __repr__(self):
        return f"Url used for parsing: {self.buildUrl()}\n"
        
    def parse(self):

        options = webdriver.ChromeOptions() 
        options.headless = True
        options.page_load_strategy = 'none'
        options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36")
        
        chrome_path = ChromeDriverManager().install() 
        chrome_service = Service(chrome_path) 
        
        driver = Chrome(options=options, service=chrome_service) 
        driver.implicitly_wait(5)

        
        driver.get(self.buildUrl()) 
        time.sleep(5)

        nfts = []

        while True:
            content = driver.find_element(By.TAG_NAME, "tbody")
            time.sleep(2)    
            
            for nft in content.find_elements(By.XPATH, '//a[contains(@href,"nft/")]'):
                nftHref = nft.get_attribute('href')
                if nftHref not in nfts:
                    nfts.append(nftHref)
            


            next = driver.find_element(By.CSS_SELECTOR, '#datatable_next')
            
            if "disabled" in next.get_attribute("class"):
                break
            
            next = next.find_element(By.CSS_SELECTOR, 'a:nth-child(1)')

            ActionChains(driver).click(next).perform()

        value = 0
        for nftUrl in nfts:
            driver.get(nftUrl)
            time.sleep(10)
            
            try:
                price = driver.find_element(By.CSS_SELECTOR, 'div.d-flex:nth-child(3) > span:nth-child(1)')
                price = float(price.text.split()[0])
            except Exception:
                price = 0.0
                
            
            try:
                owner = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_divOwner > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)")
                tokenStandard =  driver.find_element(By.CSS_SELECTOR, "div.row:nth-child(5) > div:nth-child(2)")
                nftName = driver.find_element(By.CSS_SELECTOR, ".d-md-block > span:nth-child(1)")
            except Exception as e:
                continue
            
            print(f"Checking {nftName.text}...")

            if owner.text == self.__wallet.getAddress() and tokenStandard.text == "ERC-721":
                print(f"Last sale price: {price} ETH.")
            
            try:
                value += price
            except Exception as e:
                print(e)
            print(f"Total value: {value} ETH.")
            print("")

        print(f"Value of all your NFTs is roughly: {value} ETH.")
        driver.quit()




   


    