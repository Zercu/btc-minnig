from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from config import RPC_USER, RPC_PASSWORD, RPC_HOST, RPC_PORT

# Connect to Bitcoin Core RPC
rpc_url = f"http://{RPC_USER}:{RPC_PASSWORD}@{RPC_HOST}:{RPC_PORT}"
client = AuthServiceProxy(rpc_url)

def get_new_address(label=""):
    try:
        address = client.getnewaddress(label)
        return address
    except JSONRPCException as e:
        print(f"Error generating new address: {e}")
        return None

def get_balance():
    try:
        balance = client.getbalance()
        return balance
    except JSONRPCException as e:
        print(f"Error getting balance: {e}")
        return None

def send_to_address(address, amount):
    try:
        txid = client.sendtoaddress(address, amount)
        return txid
    except JSON
