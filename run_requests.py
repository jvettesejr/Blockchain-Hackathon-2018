import requests

url = "http://localhost:5279"

def test_post():
    
    result = requests.post(
        url,
        json={"method":"resolve","params":{"uri":"what"}},
        headers={"Content-Type": "application/json"})
    print("TEST!!")
    print(result.status_code)
    print(result.json())

def post_file(repository, file_name):
    print("CONTENT IS THE FOLLOWING")
    with open(file_name) as f:
        content = f.readlines()
        print(content)
    

def get_files(repository):
    

if __name__ == "__main__":
    test_post()