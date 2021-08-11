# Cherryswap che-che pool auto-compound
Auto compound che-che staking profit in Cherryswap
## I strongly recommend do not using your main wallet(contract address), instead, using extra wallet(contract address) with relatively small amount of money. 
## 强烈建议不要使用你主要的defi钱包（合约地址），相对的，建议使用只有小额资金的额外的钱包（合约地址）。

## Features

- Harvest the che-che staking profit and restake it automatically

## Requirements

- Python 3 and Python 3 packages:
- web3
- json
- time
- requests (for fetching contractAbi)

## Usage
- Firstly, you have to deposit a certain amount of che to the che-che pool (base money), and manually approve the staking and harvesting transcations.
- Download settings.py, harvest_and_restake.py, auto_compound.py
- Setting up the settings.py (secret key, wallet address, restake time et cl.)

To use:
```sh
python3 harvest_and_restake.py
```


###  Variables to set in settings.py:
```sh
rpc: OkexChain rpc address. Set default to 'https://exchainrpc.okex.org'

contract_address: Cherryswap che-che staking pool address. Set default to '0x9Ab8BCf67fE8d8D2aD27D42Ec2A0fD5C206DAE60'

wallet_address: Your contract's public address

private_key: Your contract's(wallet) secret key

harvest_interval: The time between a restake transaction and a harvest transaction (in minutes). Set default to 720 minutes
```

### 
