import json

def test_crawler_uniqueness(fpath):
    with open(fpath, 'r') as f:
        data_dict = json.load(f)
    
    # check uniqueness of output
    data_arr = list(data_dict.values())

    # 
    data_set = set(data_arr)

    return len(data_set) == len(data_arr)