## Description

This utility can be used to deterministically produce BIP39 mnemonic phrases from arbitrary text, text that will act as a seed in the process of generating the mnemonic phrase.

The resulting mnemonic phrase can be used in devices and crypto wallets that are compatible with the BIP39 specification.


## Implementation:

In the process of generating a random BIP39 mnemonic phrase we usually take a random sequence of bits ranging from 128 to 256 bits in length and then we apply a procedure to transform these bits into mnemonics.

Here, instead of taking this initial sequence of bits at random, we simply generate them from the SHA256 hash of the provided text.



