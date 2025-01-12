#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:17:00 2024

@author: shaiyaan habib 
NUID: 002144619
"""
import csv
import matplotlib.pyplot as plt

HEADER_LINES = 6
HEADER_LINES_DATA2 = 7
FILENAME1 = "num_borrowers_per_state.csv"
FILENAME2 = "total_loans_per_state.csv"

def readfile(filename): 
    data = []
    with open (filename, "r") as infile:
        file = csv.reader(infile)
        for element in file:
            data.append(element)
    return data

def convert(x):
    x = x.replace("$", "").replace(",", "")
    return int(x)

def clean_lists(data_list, HEADER):
    data_list = data_list[HEADER:]
    cleaned_data = []
    for rows in data_list:
        cleaned_row = []
        cleaned_row.append(rows[0])     
        for elements in rows[1:]:
            if len(elements) > 0: # if there is something there
                cleaned_row.append(convert(elements))
        cleaned_data.append(cleaned_row)
    return cleaned_data

def lst_to_dct(lst):
    dct = {}
    for i in range(len(lst)):
        state = lst[i][0]
        dct[state] = lst[i][1:]
    return dct
'''
This is HW. Each Problem is a function
'''
def sum_borrowers2019(lst):
    sum2019 = [lst[i][4] for i in range(len(lst))]
    total_borrowers = sum(sum2019)        
    return total_borrowers

def balance2021(lst):
    total = [lst[i][7] for i in range(len(lst))] * 1000000
    total_borrowers = sum(total)
    return total_borrowers
    
def average_per_student2016(data, data2):
    num2016 = [data[i][1] for i in range(len(data))]
    student_amount = sum(num2016)
    total2016 = [data2[i][1] for i in range(len(data2))]
    loan_amount = sum(total2016)
    average = loan_amount / student_amount
    return average

def nevada_average(string, dct):
    average = sum(dct[string]) * 1000000 / len(dct[string])
    return average

def greatest_average(dct):
    max_avg = 0
    max_state = ""
    for element in dct:
        values = dct[element]
        avg = sum(values) / len(values)
        if avg > max_avg:
            max_avg = avg
            max_state = element
    return max_state

def lowest_average(dct):
    low_avg = 10000000000000000000000000
    low_state = ""
    for element in dct:
        values = dct[element]
        avg = sum(values) / len(values)
        if avg < low_avg:
            low_avg = avg
            low_state = element          
    return low_state

def change_per_year(dct):
    for state in dct:
        values = dct[state]
        total_change = 0
        for nums in range(1, len(values)):
            total_change = total_change + abs(values[nums] - values[nums - 1]) 
        avg = total_change / (len(values)- 1)
       # print(f"THe difference for {state} was {avg}")    
    return avg

def histogram(data, data2):
    avg = []
    for i in range(len(data)):
        num_borrowers_2021 = data[i][7]
        total_loans_2021 = data2[i][7]
        if num_borrowers_2021 > 0:
            average = total_loans_2021 / num_borrowers_2021
            avg.append(average)
        else:
            avg.append(0)
    return avg

def line_chart(state, data, data2):
    avg = []
    for i in range(1, len(data[state])):
        num_borrowers = data[state][i]
        total_amount = data2[state][i]
        if num_borrowers > 0:
            average = total_amount / num_borrowers
            avg.append(average)
        else:
            avg.append(0)        
    return avg
        
def main():
    start_data = readfile(FILENAME1)
    data = clean_lists(start_data, HEADER_LINES)
    sum_borrowers2019(data)
    
    start_data2 = readfile(FILENAME2)
    data2 = clean_lists(start_data2, HEADER_LINES_DATA2)
    balance2021(data2)
    average_per_student2016(data, data2)
    
    total_loan_dct = lst_to_dct(data2)
    nevada_average("Nevada", total_loan_dct)
    
    greatest_average(total_loan_dct)
    lowest_average(total_loan_dct)
    
    num_borrowers_dct = lst_to_dct(data)
    change_per_year(num_borrowers_dct)
    
    histogram(data, data2)
    average_balances_2021 = histogram(data, data2)
    plt.hist(average_balances_2021, bins=10, edgecolor='black')
    plt.title('Histogram of Average Outstanding Balance Per Borrower (2021)')
    plt.xlabel('Average Balance')
    plt.ylabel('Frequency')
    plt.show()
   
    state1_idx = 4  # California
    state2_idx = 48  # Wyoming
    state1_avg = line_chart(state1_idx, data, data2)
    state2_avg = line_chart(state2_idx, data, data2)    
    years = ['2016','2017','2018','2019','2020 (June)','2020','2021']
    plt.plot(years, state1_avg, label='California)')
    plt.plot(years, state2_avg, label='Wyoming)')
    plt.show()
    
    
    
    
if __name__ == "__main__":
    main()