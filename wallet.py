from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Configuration details from your bitcoin.conf
rpc_user = "your_rpc_username"
rpc_password = "your_rpc_password"
rpc_host = "127.0.0.1"
rpc_port = "8332"

# Connect to Bitcoin Core RPC
rpc_url = f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
client = AuthServiceProxy(rpc_url)

def get_new_address(label=""):
    """
    Generate a new Bitcoin address.
    """
    try:
        address = client.getnewaddress(label)
        return address
    except JSONRPCException as e:
        print(f"Error generating new address: {e}")
        return None

def get_balance():
    """
    Get the balance of the wallet.
    """
    try:
        balance = client.getbalance()
        return balance
    except JSONRPCException as e:
        print(f"Error getting balance: {e}")
        return None

def send_to_address(address, amount):
    """
    Send Bitcoin to a specific address.
    """
    try:
        txid = client.sendtoaddress(address, amount)
        return txid
    except JSONRPCException as e:
        print(f"Error sending to address: {e}")
        return None
