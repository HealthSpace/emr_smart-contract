# EMR - HealthSpace
A brownie based project to develop, test and deploy smart-contracts for EMR

## Prerequisites

Please install or have installed the following:

- [nodejs and npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)
## Installation

[Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html)


```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
# restart your terminal
pipx install eth-brownie
```
Or, if that doesn't work, via pip
```bash
pip install eth-brownie
```

## Deploy to a testnet / Scripts

```
brownie run scripts/deploy.py
```
