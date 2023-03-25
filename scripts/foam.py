from ape import accounts, Contract
from web3 import utils,contract, Web3
import typing
from dotenv import dotenv_values
import json


'''
this is the core class that will allow the wallet to interact with contract.



'''



def get_abi_from_artifact():
    artifact_file_path = "./artifacts/contracts/foam.sol/foam.json"
    with open(artifact_file_path) as file:
        artifact = json.load(file)
    return artifact['abi']





config = dotenv_values(".env")

class userInformation:
    personId = int
    userAddress = string

##
address = '0xeb1C79E2632acf0c699C27c58e4e7D4557A60cF7'


class Foam:
    contractAddress 
    contractInstance
    w3
    def __init__(self):
        self.contractAddress =  address
        self.abi = get_abi_from_artifact()
        self.w3 = Web3(Web3.HTTPProvider(config["INFURA_MUMBAI_RPC"]))
        self.contractInstance = contract(addres = self.contractAddress,abi=self.abi)

    # to be only possible by deployer contract.
    def init_oracle(self, oracle_address) -> bool:
        function_call = self.contract.functions.initOracle(oracle_address)
        return self.send_transaction(function_call)

    def init_user_information(self, person_id, user_address, _hash, from_address, private_key):
        function_call = self.contract.functions.initUserInformation(person_id, user_address, _hash)
        return self.send_transaction(function_call, from_address, private_key)

    def get_user_information(self, person_id):
        return self.contract.functions.getUserInformation(person_id).call()

    def set_user_score(self, person_id, scoring, from_address, private_key):
        function_call = self.contract.functions.setUserScore(person_id, scoring)
        return self.send_transaction(function_call, from_address, private_key)

    def send_transaction(self, function_call):
        tx_hash = self.wallet.send_transaction(self.contract_address, 0, function_call.data)
        tx_receipt = self.wallet.monitor_transaction(tx_hash)
        return tx_receipt


