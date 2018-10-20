import os
import requests


initial_wallet_address = "bUUH24gcxF2rWwcunaWFfwoTR5dDFfYjnt"

tx_id = "e2d4c71097d290062111d4eee2a1e65464f0abcbac0e93bb7eae85c9ee1eb52d"


url = "http://localhost:5279"

def test_post():
    result = requests.post(
        url,
        json={"method":"resolve","params":{"uri":"what"}},
        headers={"Content-Type": "application/json"}
    )
    print("TEST!!")
    print(result.status_code)
    print(result.json())

def post_file(repository, file_name):
    print("CONTENT IS THE FOLLOWING")

    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    real_path = os.path.join(current_dir_path, file_name)

    print(real_path)

    file_data = {
        "method":"publish",
        "params": {
            "name": repository,
            "file_path": real_path,
            "bid": 1.0,
            "metadata":  {
                "description": "Testing out a file upload",
                "title": "Zipped file upload",
                "author": "File created by the Three Comma Club",
                "language": "en",
                "license": "TCC",
                "nsfw": False
            }
        }
    }

    result = requests.post(
        url,
        json=file_data,
        headers={"Content-Type": "application/json"}
    )

    print(result.json())

    

def get_files(repository):
    pass

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
    result = requests.post(
        url,
        json={"method":"wallet_balance"},
        headers={"Content-Type": "application/json"}
    )
    print(result.json())




if __name__ == "__main__":
    # test_post()
    get_wallet_balance()

    # post_file(repository = "hackathon-lbry-threecommaclub", file_name = "README.zip")

    