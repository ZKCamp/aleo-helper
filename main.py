import os

import requests
from core.client import AleoClient, AleoTransaction
from core.program import AleoProgram
from core.account import AleoAccount


program_name = "magic_square.aleo"

aleo_client = AleoClient()
program = AleoProgram(aleo_client, program_name)
account = AleoAccount(
    aleo_client,
    os.getenv("ADDRESS"),
    os.getenv("VIEW_KEY"),
    os.getenv("PRIVATE_KEY")
)

# Deployment

# transaction = AleoTransaction(aleo_client, "at1gt5lyaskejk2lgzz4qsdrkzvs3u09rtfke9nnc22a572pezcwggq65g5q3")
# print(transaction.exists())

# Adding puzzle

# transaction = AleoTransaction(aleo_client, "at1gt5lyaskejk2lgzz4qsdrkzvs3u09rtfke9nnc22a572pezcwggq65g5q3")
# print(transaction.exists())
#
# print(program.get_mapping_value("puzzles", "67691673676804187u64"))

# Adding solution

# transaction = AleoTransaction(aleo_client, "at1rd7w5y4uudr8hwry6wzq0p3p72g84tu35zf3nsvvvqw0pskzzczskdghpz")
# print(transaction.exists())
#
# records = transaction.get_transaction_output_records()
#
# for record in records:
#     account.decode_cipher(record)
