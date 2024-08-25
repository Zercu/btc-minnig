import subprocess
from config import MINER_PATH, POOL_URL, WALLET_ADDRESS

class Miner:
    def __init__(self):
        self.process = None

    def start_mining(self):
        if self.process:
            return "Mining is already running."

        command = [
            MINER_PATH,
            '-o', POOL_URL,
            '-u', WALLET_ADDRESS,
            '-p', 'x'
        ]
        try:
            self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return "Mining started."
        except Exception as e:
            return f"Failed to start mining: {str(e)}"

    def stop_mining(self):
        if not self.process:
            return "Mining is not running."

        self.process.terminate()
        self.process = None
        return "Mining stopped."

    def get_status(self):
        if not self.process:
            return "Mining is not running."
        return "Mining is running."
