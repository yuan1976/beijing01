import yaml


def read_yaml(filename):
    with open("./data/"+filename,'r',encoding="utf-8")as f:
        return yaml.load(f)

if __name__ == '__main__':
    # print(read_yaml("login.yaml"))
    # print("--" * 50)
    # arrs = []
    # for data in read_yaml("login.yaml").values():
    #     arrs.append(tuple(data.values()))
    # print(arrs)

    print(read_yaml("address.yaml"))
    print("--" * 50)
    arrs = []
    data = read_yaml("address.yaml").get("add_address")
    arrs.append(tuple(data.values()))
    print(arrs)