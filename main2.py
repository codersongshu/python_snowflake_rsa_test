import snowflake.connector
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

pwd = 'qwerty'

with open("/Users/gurdeep/rsa_key.p8", "rb") as key:
    p_key= serialization.load_pem_private_key(
        key.read(),
        password=pwd.encode(),
        backend=default_backend()
    )

pkb = p_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption())

ctx = snowflake.connector.connect(
    user='test_user2',
    private_key=pkb,
    account='aq54466.ca-central-1.aws'
    )

cs = ctx.cursor()

cs.execute('SELECT * FROM MYDB2.MYSCHEMA.MYTABLE')

results = cs.fetchall()

print(results)