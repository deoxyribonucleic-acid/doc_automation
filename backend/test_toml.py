import toml

toml_file_path = "./config.toml"
data = toml.load(toml_file_path)
print(data)
# 读取 user 表下的 age
user_age = data['owner']['port']
print(user_age)