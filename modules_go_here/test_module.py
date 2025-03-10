import secrets
#this library preety much handles all the cryptography stuff for signatures but we should make our own for more control and instead generate with secrets.randbits()
from ecdsa import SigningKey, SECP256k1




private_key = SigningKey.generate(curve=SECP256k1)
public_key = private_key.get_verifying_key()

# Sign a message
message = b"Hello, elliptic curve!"
signature = private_key.sign(message)

# Verify the signature
is_valid = public_key.verify(signature, message)
print("Signature valid:", is_valid)



private_key = secrets.randbits(256)


print(private_key)