from eth_account import Account
from brownie import EMR, network, config
from .helpers import get_account


def deploy_emr():
    account = get_account()
    emr = EMR.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed EMR!")
    return emr


def add_user_key(unique_token,user_key):
    account = get_account()
    emr = EMR[-1]
    tx = emr.addUserKey(unique_token,user_key,{'from':account})
    tx.wait(1) # waiting for 1 block to mine

def add_user_hash(unique_token,user_hash):
    emr = EMR[-1]
    tx = emr.addUserHash(unique_token,user_hash)
    tx.wait(1)

def get_user_key(unique_token):
    emr = EMR[-1]
    tx = emr.getUserKey.call(unique_token)
    return tx


def get_user_data(unique_token):
    account = get_account()
    emr = EMR[-1]
    tx = emr.getUserHashData.call(unique_token,{'from':account})
    return tx

def main():
    deploy_emr()

    testing_token = "T-2022TN0001"
    testing_private_key = "HelloWorld"
    testing_hashed_data = "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"

    add_user_key(testing_token,testing_private_key) # Unique_token,private_key
    add_user_hash(testing_token,testing_hashed_data) # Unique_token,Hashed Data
    private_key = get_user_key(testing_token)
    hashed_records = get_user_data(testing_token)

    print("PRIVATE KEY: ",private_key)
    print("HASHED RECORDS: ",hashed_records)

