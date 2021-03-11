# -*- coding: utf-8 -*-
# author: Runhao G
# time: 2021/3/11
# 该数据集是师兄毕设所用光伏数据
# 取出前16个点，和前一天该时刻前4个点
import numpy as np
import pandas as pd


RAW_DATA_PATH = 'E:\\research\\process-raw-data\\data\\raw_data\\'
PROCESSED_DATA_PATH = 'E:\\research\\process-raw-data\\data\\processed_data\\'


def load_data(filename):
    raw_data = pd.read_csv(RAW_DATA_PATH + filename)
    raw_data_array = raw_data.iloc[:, [0, -2]].values
    return raw_data_array


def save_data(raw_data, filename):
    raw_data_df = pd.DataFrame(raw_data, columns=['Time', 'power'])
    raw_data_df.to_csv(PROCESSED_DATA_PATH + filename, index=False)


def save_data_16_features(raw_data, filename):
    columns = ['Time', 'power_t']
    for i in range(1, 17):
        columns.append('power_t-%d' % i)
    # print(len(columns))
    raw_data_df = pd.DataFrame(raw_data, columns=columns)
    raw_data_df.to_csv(PROCESSED_DATA_PATH + filename, index=False)


def save_data_dayahead(raw, filename):
    columns = ['Time', 'power_t']
    for i in range(1, 17):
        columns.append('power_t-%d' % i)
    for i in range(1, 5):
        columns.append('power_ahead_t-%d' % i)
    # print(len(columns))
    raw_data_df = pd.DataFrame(raw, columns=columns)
    raw_data_df.to_csv(PROCESSED_DATA_PATH + filename, index=False)


def generate_raw_data():
    """
    生成两列数据集，即时间列和平均功率列
    :return:
    """
    raw_data = load_data('Austin_in_January_connected.csv')
    save_data(raw_data, 'January_processed.csv')
    raw_data = load_data('Austin_in_February_connected.csv')
    save_data(raw_data, 'February_processed.csv')
    raw_data = load_data('Austin_in_March_connected.csv')
    save_data(raw_data, 'March_processed.csv')
    raw_data = load_data('Austin_in_April_connected.csv')
    save_data(raw_data, 'April_processed.csv')
    raw_data = load_data('Austin_in_May_connected.csv')
    save_data(raw_data, 'May_processed.csv')
    raw_data = load_data('Austin_in_June_connected.csv')
    save_data(raw_data, 'June_processed.csv')


def generate_16_features():
    month = ['January', 'February', 'March', 'April', 'May', 'June']
    for name in month:
        raw_data = pd.read_csv(PROCESSED_DATA_PATH + name + '_processed.csv')
        avg_power = raw_data.iloc[:, 1].values.reshape(-1, 1)
        time = raw_data.iloc[:, 0].values.reshape(-1, 1)
        raw_data_processed = avg_power[16:, 0].reshape(-1, 1)  # remove the 1st 16 rows, 0-15
        for i in range(1, 17):
            raw_data_processed = np.concatenate((raw_data_processed, avg_power[16-i:-i, 0].reshape(-1, 1)), axis=1)
        raw_data_processed = np.concatenate((time[16:, 0].reshape(-1, 1), raw_data_processed), axis=1)
        save_data_16_features(raw_data_processed, name + '_processed_v1.csv')


def generate_dayahead_features():
    month = ['January', 'February', 'March', 'April', 'May', 'June']
    for name in month:
        raw_data = pd.read_csv(PROCESSED_DATA_PATH + name + '_processed_v1.csv')
        avg_power = raw_data.iloc[:, 1:].values
        time = raw_data.iloc[:, 0].values.reshape(-1, 1)
        raw_data_processed = avg_power[96:, :]  # remove the 1st 16 rows, 0-15
        for i in range(1, 5):
            raw_data_processed = np.concatenate((raw_data_processed, avg_power[96 - i:-i, 0].reshape(-1, 1)), axis=1)
        raw_data_processed = np.concatenate((time[96:, 0].reshape(-1, 1), raw_data_processed), axis=1)
        save_data_dayahead(raw_data_processed, name + '_processed_v2.csv')


if __name__ == '__main__':
    generate_dayahead_features()





