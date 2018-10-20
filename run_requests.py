import os
import requests
from typing import Dict, Tuple


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

    repository, increment = split_str_int(identify_newest_file())
    increment += 1

    metadata = {
        "description": "Testing out a file upload",
        "title": "Zipped file upload",
        "author": "File created by the Three Comma Club",
        "language": "en",
        "license": "TCC",
        "nsfw": False
    }
    params = {
        "name": repository + str(increment),
        "file_path": real_path,
        "bid": '0.011',
        "metadata": metadata,
    }

    json = post_information(method="publish", params=params)

    print("\nUploaded the file with a post, a bid of 0.001 LBC")
    print(json)
    print()


def identify_newest_file() -> str:
    json = post_information(method="claim_list_mine")
    results = json["result"]

    highest_index = 0
    highest_value = 0
    for i in range(len(results)):
        result, index_int = split_str_int(results[i]["name"])
        if index_int > highest_value:
            highest_value = index_int
            highest_index = i

    interesting = results[highest_index]["permanent_url"]
    return interesting[:interesting.find("#")]

def split_str_int(string) -> Tuple[str, int]:
    # print("STRING IS", string)
    end_index = -1
    for i in range(len(string)):
        if string[i].isdigit() == True:
            end_index = i
            break
    if end_index == -1:
        return string, 0
    repo_name = string[:end_index]
    repo_index = int(string[end_index:])
    # print("PRINTING REPO INFO")
    # print(repo_name, repo_index)
    return repo_name, repo_index

def get_files(repository) -> Dict:
    repository = identify_newest_file()
    # CLI: get(uri=repository)
    print()
    print("*"*88)
    print("Retrieving file from repository:", repository)
    json = post_information(method="get", params={"uri": repository})
    if not json.get('result') or json.get('error'):
        print("*"*88)
        print("The network has not yet processed all the blobs for the newest version of this file.")
        print("Please try again soon.\n")
        return json
    print("Retrived the files and they will be downloaded at:")
    print(json["result"]['download_path'])
    print("*"*88)
    print("\nThe following data was returned:")
    print(json)
    print()
    return json

def delete_files(repository):
    json = post_information(method="get", params={"uri": repository})


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
    # print(identify_newest_file())
    # get_files("hackathon-lbry-threecommaclub")

    # post_file(repository = "hackathon-lbry-threecommaclub", file_name = "README.zip")

    