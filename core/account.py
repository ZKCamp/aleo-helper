import requests
from helpers.shell import Shell
from core.client import AleoClient


class AleoAccount:
    def __init__(self, aleo_client: AleoClient, address: str, view_key: str, private_key: str):
        self.address = address
        self.view_key = view_key
        self.private_key = private_key

        self.shell = Shell()
        self.aleo_client = aleo_client

    def decode_cipher(self, cipher_text: str):
        return_value = self.shell.execute(f"snarkos developer decrypt --ciphertext {cipher_text} --view-key {self.view_key}")

        print("\n".join(return_value.split("\n")[1:]))

    def get_balance(self):
        balance_endpoint = f"{self.aleo_client.endpoint}/testnet3/program/credits.aleo/mapping/account/{self.address}"
        balance = requests.get(balance_endpoint).content.decode("utf-8").strip('"')

        if balance == "null":
            return 0
        else:
            return int(balance[:-3]) / (10**6)
