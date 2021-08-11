from web3 import Web3
import settings


class transaction_result:
    def __init__(self): 
        self.is_harvest = 1
        self.transaction_status = 0
        self.harvest_amount = 0
        self.transaction_hx = ''
        self.gas_consume = 0

def harvest_and_restake(is_harvest, restake_amount):
    web3 = Web3(Web3.HTTPProvider(settings.rpc))
    if web3.isConnected() != True:
        print('Rpc Connection Failed')

    
    contract = web3.eth.contract(settings.contract_address, abi=settings.abiCode)
    
    gas = settings.gas
    gasPrice = int(web3.eth.gas_price*settings.gas_price_multiples)
    transaction_result.harvest_amount = contract.functions.pendingReward(settings.wallet_address).call()
    
    if is_harvest == 1:
       deposit_amount = 0
       transaction_result.is_harvest = 1
    else:
       deposit_amount = restake_amount
       transaction_result.is_harvest = 0
       

    
    txn = contract.functions.deposit(deposit_amount).buildTransaction({
        'gas': gas,
        'gasPrice': gasPrice,
        'nonce': web3.eth.getTransactionCount(settings.wallet_address)
        })
    
    sign_txn = web3.eth.account.signTransaction(txn, private_key=settings.private_key)
    
    while True:
        try:
            hx = web3.eth.sendRawTransaction(sign_txn.rawTransaction)
            break
        except ValueError:
            print("Nonce error, Trying again")
            txn = contract.functions.deposit(deposit_amount).buildTransaction({
                    'gas': gas,
                    'gasPrice': gasPrice,
                    'nonce': web3.eth.getTransactionCount(settings.wallet_address)
                    })
            sign_txn = web3.eth.account.signTransaction(txn, private_key=settings.private_key)
    
    transaction_result.transaction_hx = hx
    receipt = web3.eth.wait_for_transaction_receipt(hx, timeout=settings.transaction_timeout*60)
    transaction_result.gas_consume = gasPrice * receipt.gasUsed
    
    if receipt.status == 1:
        if is_harvest == 1:
            print('Harvest Succeed')
            transaction_result.transaction_status = 1
        else:
            print('Restake Succeed')
    else:
        if is_harvest == 1:
            print('Harvest Failed')
        else:
            print('Restake Failed')
    return transaction_result
        
        
