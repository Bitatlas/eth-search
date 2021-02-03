from web3 import IPCProvider, Web3
from web3.middleware import geth_poa_middleware
w3 = Web3(IPCProvider('/home/ubuntu/.ethereum/geth.ipc'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

def find(addr):
    for i in range(999000, 1000000): #here we define a range of blocks to search
        txLen = len(w3.eth.getBlock(i).transactions) #to get the transactions and lenght of the transactions 
        for j in range(txLen): #this loop will go through all the transactions to check the transactions in the blocks
            print("Block: %d/%d --- Transaction: %d/%d" % (i, 1000000, j, txLen)) #will print the transaction in the block
            if addr == w3.eth.getBlock(i, True).transactions[j]["from"]: #if we get a transaction with the adress that we are looking for, it will print the transaction hash
                print("FOUND BABIBlock: %d\nTX: %s" % (i, w3.eth.getBlock(i).transactions[j].hex()))
                return
