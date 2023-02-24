"""This python will handle some extra functions."""
import sys
from os.path import exists

import yaml
from yaml import SafeLoader


def config_file_generator():
    """Generate the template of config file"""
    with open('config.yml', 'w', encoding="utf8") as f:
        f.write("""# ++--------------------------------++
# | Auto_bot_test                     |
# | Made by KXX (MIT License)         |
# ++--------------------------------++
# 輸入起訖站
# |  南港  台北  板橋  桃園  新竹  苗栗   |
# |  台中  彰化  雲林  嘉義  台南  左營   |
start_station : ''
end_station : ''
"""
                )
    sys.exit()


def read_config():
    """Read config file.
    Check if config file exists, if not, create one.
    if exists, read config file and return config with dict type.
    :rtype: dict
    """
    if not exists('./config.yml'):
        print("Config file not found, create one by default.\nPlease finish filling config.yml")
        with open('config.yml', 'w', encoding="utf8"):
            config_file_generator()

    try:
        with open('config.yml', 'r', encoding="utf8") as f:
            data = yaml.load(f, Loader=SafeLoader)
            start = transpose_start(data['start_station'])
            end = transpose_end(data['end_station'])
            config = {
                'start_station': start,
                'end_station': end
            }
            return config
    except (KeyError, TypeError):
        print(
            "An error occurred while reading config.yml, please check if the file is corrected filled.\n"
            "If the problem can't be solved, consider delete config.yml and restart the program.\n")
        sys.exit()

station = dict["//*[@id='BookingS1Form']/div[3]/div[1]/div/div[1]/div/select/option[2]",]

def transpose_start(start):
    if start == "南港":
        start = 1
    elif start == "台北":
        start = 2
    elif start == "板橋":
        start = 3
    elif start == "桃園":
        start = 4
    elif start == "新竹":
        start = 5
    elif start == "苗栗":
        start = 6
    elif start == "台中":
        start = 7
    elif start == "彰化":
        start = 8
    elif start == "雲林":
        start = 9
    elif start == "嘉義":
        start = 10
    elif start == "台南":
        start = 11
    elif start == "左營":
        start = 12
    return start


def transpose_end(end):
    if end == "南港":
        end = 1
    elif end == "台北":
        end = 2
    elif end == "板橋":
        end = 3
    elif end == "桃園":
        end = 4
    elif end == "新竹":
        end = 5
    elif end == "苗栗":
        end = 6
    elif end == "台中":
        end = 7
    elif end == "彰化":
        end = 8
    elif end == "雲林":
        end = 9
    elif end == "嘉義":
        end = 10
    elif end == "台南":
        end = 11
    elif end == "左營":
        end = 12
    return end
