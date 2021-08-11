import json
import requests

rpc = 'https://exchainrpc.okex.org'

# stakign contract
contract_address = '0x9Ab8BCf67fE8d8D2aD27D42Ec2A0fD5C206DAE60'

# staking contract abi (for verified contract)

def get_contractAbi(contract_address):
    contract_url = 'https://www.oklink.com/api/explorer/v1/okexchain/addresses/' + contract_address + '/contract'
    contract_json = requests.get(contract_url)
    contract_json_data = json.loads(contract_json.text)
    contract_json_data = contract_json_data['data']
    abiCode = contract_json_data['contractAbi']
    abiCode = json.loads(abiCode)
    return abiCode




# your wallet public address
wallet_address = ''      

# your wallet private key
private_key = ''

# gas and gas price
gas = int(20000*10)
gas_price_multiples = 1.5

# time settings in minutes
harvest_interval = 5

transaction_timeout = 3

