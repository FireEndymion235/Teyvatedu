
from cryptography.hazmat.primitives.asymmetric import rsa, padding

from cryptography.hazmat.primitives import serialization,hashes
import base64
class RSA:
    def __init__(self) -> None:
        # generate RSA key pair
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
    @property
    def public_pem(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    @property
    def private_pem(self):
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    
    def encrypt(self,data:bytes)->bytes:
        return self.public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),  # noqa: F821
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    def decrypt(self,encrypted_data:bytes)->bytes:
        return self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    
    def encrypt_public(public_key:rsa.RSAPublicKey,data:bytes):
        return public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()), 
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    @staticmethod
    def toBase64(data:bytes)->str:
        return base64.b64encode(data)

    @staticmethod
    def fromBase64(data:str)->bytes:
        return base64.b64decode(data)
    