def all_data(address : str) -> str :
    file = open(address)
    return file.read()

def data_list(address : str) -> list[str] :
    file = all_data(address)
    return file.split("\n")


