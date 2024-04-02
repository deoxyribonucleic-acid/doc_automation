import requests
def update_id(id,attribute):
    url = 'http://localhost:8888/login/'  
    data_dict = {'password': attribute,'account':id}
    r = requests.post(url, data_dict)
    print("request: ", r.text)
    return r.text
    # print(response.json())

def fetch_proposal(id):
    url = 'http://localhost:8888/update_proposal/'  
    data_dict = {'ID':id}
    r = requests.get(url, data_dict)
    # print("request: ", r.text)
    return r.text    
    
def fetch_midterm(id):
    url = 'http://localhost:8888/update_midterm/'  
    data_dict = {'ID':id}
    r = requests.get(url, data_dict)
    # print("request: ", r.text)
    return r.text    

def fetch_defense(id):
    url = 'http://localhost:8888/update_defense/'  
    data_dict = {'ID':id}
    r = requests.get(url, data_dict)
    # print("request: ", r.text)
    return r.text    

# if __name__ == '__main__':
#     account = input("账号")
#     fetch_proposal(account)
