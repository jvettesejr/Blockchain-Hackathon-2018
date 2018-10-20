import os
import requests
from typing import Dict


initial_wallet_address = "bUUH24gcxF2rWwcunaWFfwoTR5dDFfYjnt"

tx_id = "e2d4c71097d290062111d4eee2a1e65464f0abcbac0e93bb7eae85c9ee1eb52d"

url = "http://localhost:5279"


def test_post():
    print("\nAnalyzing connection to blockchain...")
    json = post_information(method="resolve", params={"uri":"what"})
    print(json)


def post_file(repository, file_name):
    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    real_path = os.path.join(current_dir_path, file_name)

    metadata = {
        "description": "Testing out a file upload",
        "title": "Zipped file upload",
        "author": "File created by the Three Comma Club",
        "language": "en",
        "license": "TCC",
        "nsfw": False
    }
    params = {
        "name": repository,
        "file_path": real_path,
        "bid": 1.0,
        "metadata": metadata,
    }

    json = post_information(method="publish", params=params)

    print("\nUploaded the file with a post, a bid of 1 LBC")
    print(json)
    

def get_files(repository):
    # CLI: get(uri=repository)
    json = post_information(method="get", params={"uri": repository})
    print("\nRetrived the files and they will be downloaded at:")
    print(json["result"]['download_path'])
    print("\nThe following data was returned:")
    print(json)

def generate_wallet_address():
    """
    result = requests.post(
        url,
        json={"method":"wallet_new_address"},
        headers={"Content-Type": "application/json"}
    )
    print(result.json())
    """
    pass

def get_wallet_balance():
    print("\nRetrieving wallet balance")
    print(post_information(method = "wallet_balance"))


def post_information(method: str, params: Dict = dict()) -> Dict:
    json = dict()
    if not method:
        return {}
    if not(params):
        json = {"method": method}
    else:
        json = {
            "method": method,
            "params": params,
        }
    result = requests.post(
        url,
        json = json,
        headers={"Content-Type": "application/json"}
    )
    if result.status_code != 200:
        return {}
    else:
        return result.json()


if __name__ == "__main__":
    # test_post()
    get_wallet_balance()
    # get_files("hackathon-lbry-threecommaclub")

    # post_file(repository = "hackathon-lbry-threecommaclub", file_name = "README.zip")

    