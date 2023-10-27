import requests
from .client import AleoClient


class AleoProgram:
    def __init__(self, aleo_client: AleoClient, program_name):
        self.client_endpoint = aleo_client.endpoint
        self.endpoint = f"{aleo_client.endpoint}/testnet3/program/{program_name}"
        self.program_name = program_name

    def get_program(self):
        response = requests.get(self.endpoint)
        content = response.content.decode('utf-8').strip('"').split("\\n")
        return content

    def print_program(self):
        for line in self.get_program():
            print(line)

    def get_mapping_value(self, mapping_name: str, key: str):
        response = requests.get(f"{self.client_endpoint}/testnet3/program/{self.program_name}/mapping/{mapping_name}/{key}")
        return response.content.decode("utf-8").strip('"')
