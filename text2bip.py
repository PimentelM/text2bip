#!/usr/local/bin/python3
import hashlib, sys

def sha256(data):
    if type(data) == type(""):
        data = data.encode("utf-8")

    return hashlib.sha256(data).digest()

def getwordlist():
    return open("english.txt","r").read().split("\n")


def getbinarystring(digest):
    bits = ""
    for byte in digest:
        bits += bin(byte)[2:].rjust(8,"0")
    return bits

def getmnemonicphrase(text):
    # sha256 of the text
    digest = sha256(text)        
    # calculate the hash bits
    hashbits = getbinarystring(sha256(digest))[:8]
    # string of bits from the digest
    binarystring = getbinarystring(digest) + hashbits
    # wordlist of mnemonics
    wordlist = getwordlist()
    # bits spllited in groups of 11 bits
    entropygroups = [binarystring[i:i+11] for i in range(0,len(binarystring),11)]
    # convert these groups of bits into integers that will be used as indexes
    mnemonicindexes = map(lambda x : int(x,2),entropygroups)
    # map mnemonics
    mnemonics = list(map(lambda x : wordlist[x],mnemonicindexes))
    return " ".join(mnemonics)

def main():
    text = input("Please, enter your secret text below:\n")
    result = getmnemonicphrase(text)
    print("Your mnemonic phrase is:")
    print(result)


if __name__ == "__main__":
    # execute only if run as a script
    main()