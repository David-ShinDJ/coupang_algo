import time


def string_to_timestamp(date_string):
    # 주어진 문자열을 시간 구조체로 변환
    time_struct = time.strptime(date_string, "%Y-%m-%d %H:%M:%S")

    # 시간 구조체를 timestamp로 변환
    timestamp = time.mktime(time_struct)

    return int(timestamp)

# 예제 사용
date_string = "2023-11-15 12:30:45"
timestamp_value = string_to_timestamp(date_string)
print(timestamp_value)