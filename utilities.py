"""This python will handle some extra functions."""
import sys
from os.path import exists

import ddddocr
import yaml
from yaml import SafeLoader


def config_file_generator():
    """Generate the template of config file"""
    with open('config.yml', 'w', encoding="utf8") as f:
        f.write("""# ++--------------------------------++
# | Auto_bot_test                        |
# | Made by KXX (MIT License)            |
# ++--------------------------------++
# 輸入起訖站
# |  南港  台北  板橋  桃園  新竹  苗栗      |
# |  台中  彰化  雲林  嘉義  台南  左營      |
start_station : '台北'
end_station : '左營'
# -------------------------------------------
# 輸入出發時間 (24小時制 !!01:00-04:59沒有營業 !!)
# | 00:00 00:30 05:00 05:30 06:00 06:30 07:00 07:30 08:00 08:30 |
# | 09:00 09:30 10:00 10:30 11:00 11:30 12:00 12:30 13:00 13:30 |
# | 14:00 14:30 15:00 15:30 16:00 16:30 17:00 17:30 18:00 18:30 |
# | 19:00 19:30 20:00 20:30 21:00 21:30 22:00 22:30 23:00 23:30 |
start_time : '00:00'
# -------------------------------------------
# 輸入票種及數量，沒有則填0
regular_ticket : '0' #全票
children_ticket : '0' #孩童票
disabled_ticket : '0' #愛心票
student_ticket : '0' #大學生票
senior_persons_ticket : '0' #敬老票
# -------------------------------------------
# 僅顯示尚有早鳥優惠之車次 '是'or'否'
early_ticket : '否'
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
            start_station = get_start_station(data['start_station'])
            end_station = get_end_station(data['end_station'])
            start_time = get_start_time(data['start_time'])
            ticket_dict['regular_ticket'] = data['regular_ticket']
            ticket_dict['children_ticket'] = data['children_ticket']
            ticket_dict['disabled_ticket'] = data['disabled_ticket']
            ticket_dict['student_ticket'] = data['student_ticket']
            ticket_dict['senior_persons_ticket'] = data['senior_persons_ticket']
            early_ticket = get_early_ticket(data['early_ticket'])
            config = {
                'start_station': start_station,
                'end_station': end_station,
                'start_time': start_time,
                'regular_ticket': ticket_dict['regular_ticket'],
                'children_ticket': ticket_dict['children_ticket'],
                'disabled_ticket': ticket_dict['disabled_ticket'],
                'student_ticket': ticket_dict['student_ticket'],
                'senior_persons_ticket': ticket_dict['senior_persons_ticket'],
                'early_ticket': early_ticket
            }
            return config
    except (KeyError, TypeError):
        print(
            "An error occurred while reading config.yml, please check if the file is corrected filled.\n"
            "If the problem can't be solved, consider delete config.yml and restart the program.\n")
        sys.exit()


time_list = [
    '00:00', '00:30', '05:00', '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30',
    '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30',
    '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30',
    '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30',
]
station_list = [
    '南港', '台北', '板橋', '桃園', '新竹', '苗栗',
    '台中', '彰化', '雲林', '嘉義', '台南', '左營'
]
ticket_dict = {
    'regular_ticket': '0',
    'children_ticket': '0',
    'disabled_ticket': '0',
    'student_ticket': '0',
    'senior_persons_ticket': '0'
}


def get_start_station(start_station):
    start_station = station_list.index(start_station) + 2
    return start_station


def get_end_station(end_station):
    end_station = station_list.index(end_station) + 2
    return end_station


def get_start_time(start_time):
    start_time = time_list.index(start_time) + 2
    return start_time


def get_ocr_password(ocr_image_path):
    """Get the answer of ocr.
    :rtype: str
    """
    ocr = ddddocr.DdddOcr()
    with open(ocr_image_path, 'rb') as f:
        image = f.read()
    password = ocr.classification(image)
    return password


def get_early_ticket(early_ticket):
    if early_ticket == '是':
        early_ticket = 1
        return early_ticket
    elif early_ticket == '否':
        early_ticket = 0
        return early_ticket
