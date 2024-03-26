import requests
def update_id(id,attribute):
    url = 'http://localhost:8000/login/'  
    data_dict = {'password': attribute,'account':id}
    r = requests.post(url, data_dict)
    print("request: ", r.text)
    return r.text
    # print(response.json())
       
# if __name__ == '__main__':
#     account = input("账号")
#     password = input("密码")
#     update_id(account,password)