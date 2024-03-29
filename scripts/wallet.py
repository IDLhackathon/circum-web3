from web3 import Web3

from dotenv import dotenv_values
config = dotenv_values(".env")


''''
this class allows the user to create arbitrary wallet (without generating key) and do the operations for the user working on the streamlit side

once the user opens the application, it should be initiating the wallet corresponding to the user and fetch the address.


IMP: THIS IS NOT AT ALL THE WALLET USED FOR PRODUCTION, THERE ARE VARIOUS CONCEPTS THAT ARE ABSTRACTED HERE and thus 


instructions to use: 
1. insure that variable INFURA_MUMBAI_RPC is set in the env 
2. import the following operator (with private key as optional variable)
wallet = Wallet()



'''
ocean = '0xd8992Ed72C445c35Cb4A2be468568Ed1079357c8'
class Wallet:
    def __init__(self,name,email, private_key=None):
        self.w3 = Web3(Web3.HTTPProvider(config['INFURA_MUMBAI_RPC']))
        self.name = name
        self.email = email
        if private_key:
            self.account = self.w3.eth.account.privateKeyToAccount(private_key)

        else:
            self.account = self.w3.eth.account.create()

    def get_balance(self):
        balance = self.w3.eth.getBalance(self.account.address)
        return Web3.fromWei(balance, 'ether')

    def send_transaction(self, to, value, data="0x", gas=None, gas_price=None):
        if not gas:
            gas = self.w3.eth.estimateGas({"from": self.account.address, "to": to, "data": data})
        if not gas_price:
            gas_price = self.w3.eth.gasPrice

        transaction = {
            'to': to,
            'value': Web3.toWei(value, 'ether'),
            'gas': gas,
            'gasPrice': gas_price,
            'nonce': self.w3.eth.getTransactionCount(self.account.address),
            'data': data
        }

        signed_transaction = self.w3.eth.account.signTransaction(transaction, self.account.privateKey)
        tx_hash = self.w3.eth.sendRawTransaction(signed_transaction.rawTransaction)
        return tx_hash

    def monitor_transaction(self, tx_hash):
        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt

    def interact_with_contract(self, contract_address, abi, function_name, *args):
        contract = self.w3.eth.contract(address=contract_address, abi=abi)
        function_call = contract.get_function_by_name(function_name)(*args)
        tx_hash = self.send_transaction(contract_address, 0, function_call.data)
        return tx_hash


    def get_address(self):
        return self.account.address
    
    def mint_tokens(self):
        pass

    def get_transaction_hash(user_address, function_signature, contract_address, web3_provider):
    # create a web3 instance

    # create a contract instance
        contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)

    # create a function object for the function you want to call
        function = contract.functions[function_signature]

    # get the transaction hash for the function call
        transaction_hash = function.transact({'from': user_address}).hex()

        return transaction_hash