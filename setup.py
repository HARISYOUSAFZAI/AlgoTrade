from setuptools import setup, find_packages

# from typing import List



PROJECT_NAME= "algo-trade"
VERSION = "0.0.2"
AUTHOR = "HYousaf"
DESCRIPTION = "It is the model to predict the upcoming candle of the currency in forex"
PACKAGES = "algotrade"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_req_lst():#->List[str]:
    """
    Description: This functon returns the list of the required libraries for algotrade.
    """
    with open(REQUIREMENT_FILE_NAME) as req_file:
        return req_file.readlines().remove("-e .")


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages= find_packages(), # important
    install_requires = get_req_lst() #important
)
