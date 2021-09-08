from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Create a new DSA key
key = DSA.generate(2048)

# Sign a message
message = b"Hello"
hash_obj = SHA256.new(message)
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(hash_obj)

# Load the public key
hash_obj = SHA256.new(message)
pub_key = DSA.import_key(key.publickey().export_key())
verifier = DSS.new(pub_key, 'fips-186-3')
# Verify the authenticity of the message
try:
    verifier.verify(hash_obj, signature)
    print("The message is authentic.")
except ValueError:
    print("The message is not authentic.")