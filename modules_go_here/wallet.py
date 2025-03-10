from ecdsa import SigningKey, SECP256k1
import json

class wallet_manager:
    def __init__(self,wallet_location:str = None):
        pass

    def generate_new_wallet(self):
        private_key = SigningKey.generate(curve = SECP256k1)
        private_key_hex = private_key.to_string().hex()

        with open(__file__[:-25] + 'client_data\\wallet.json','r') as file:
            wallet_data = json.load(file)

        wallet_data['private'] = private_key_hex

        with open(__file__[:-25] + 'client_data\\wallet.json','w') as file:
            json.dump(wallet_data,file,indent = 4)