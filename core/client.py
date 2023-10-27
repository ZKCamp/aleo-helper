import requests


class AleoClient:
    def __init__(self, host="0.0.0.0", port="3030"):
        self.endpoint = f"http://{host}:{port}"

    def get_transaction(self, transaction_id: str):
        return AleoTransaction(self, transaction_id)


class AleoTransaction:
    def __init__(self, aleo_client: AleoClient, transaction_id: str):
        self.transaction_endpoint = f"{aleo_client.endpoint}/testnet3/transaction/{transaction_id}"
        self.transaction_id = transaction_id

    def _get_raw_transaction(self):
        print(f"[GET] {self.transaction_endpoint}")
        raw_data = requests.get(self.transaction_endpoint).json()
        return raw_data

    def exists(self):
        try:
            _ = self._get_raw_transaction()
            return True
        except Exception:
            return False

    def get_transaction_output_records(self):
        records = []
        raw_data = self._get_raw_transaction()
        for transition in raw_data["execution"]["transitions"]:
            for output in transition["outputs"]:
                if output["type"] == "record":
                    records.append(output["value"])

        return records
