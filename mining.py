import subprocess
import os
from config import MINER_PATH, POOL_URL, WALLET_ADDRESS

class Miner:
    def __init__(self):
        self.process = None
        self.balance = 0

    def start_mining(self):
        if self.process is not None:
            return "Mining already in progress."

        # Command to start BFGMiner or CGMiner
        command = [
            MINER_PATH,
            '-o', POOL_URL,
            '-u', WALLET_ADDRESS,
            '-p', 'x'
        ]
        # Start the mining process
        self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "Mining started."

    def stop_mining(self):
        if self.process is None:
            return "No mining in progress."
        
        # Terminate the mining process
        self.process.terminate()
        self.process = None
        return "Mining stopped."

    def get_status(self):
        if self.process is None:
            return "Mining is not running."
        else:
            return "Mining is currently running."

    def get_balance(self):
        return self.balance

    def simulate_mining_earnings(self):
        # For simulation purposes, increase balance by a small random amount
        self.balance += 0.00001
        return self.balance
