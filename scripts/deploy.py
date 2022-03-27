from brownie import EMR, network, config
from .helpers import get_account


def deploy_emr():
    account = get_account()
    emr = EMR.deploy({"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed EMR!")
    return emr


def main():
    deploy_emr()    