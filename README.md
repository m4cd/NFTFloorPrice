# NFT Floor Price Checker

## Requirements

To make it work please install the following packages:

```
sudo apt-get install libnss3 libglib2.0-0 libgconf-2-4 libfontconfig1
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```

## How it works

The application asks you to provide your ETH address where you have all your NFT. Then it parses the web page:
https://etherscan.io/nft-transfers?a=your_address
and extracts all etherscan url leading to every of your NFTs directly.

After that it parses every site and sums up all last sale prices to roughly estimate worth of all your NFTs

Application uses headless chrome browser in the background. It requires some time to let is generate and parse all the pages so please be patient :)

### Remarks

Application does not work when the address has configured ENS record.