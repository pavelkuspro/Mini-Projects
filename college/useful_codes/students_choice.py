"""
This module imports an Excel table to select students for test writing.
"""

import random as rd
import pandas as pd

if __name__ == "__main__":
    # upload the Excel file
    df = pd.read_excel("studenti_tabulka.ods", engine="odf")
    
    # check the columns' names
    print("\n---\nColumns:\n", list(df.columns), "\n---\n")
    
    # interested in columns with indices 1:-1 (Test 1 - Test 10)
    col_tests = df.columns[1:-1]
    
    # focused on those columns in the dataframe table: df[col_test1to10]
    df["Records"] = df[col_tests].notna().sum(axis=1)
    
    # average number of tests per person
    numb_students = len(df["Jmeno"])         # total number of students
    numb_tests = len(col_tests)               # number of test slots in the semester
    NUMB_STUD_PER_HOUR = 11                   # number of students per test session
    total_numb_tests = numb_tests * NUMB_STUD_PER_HOUR  # total tests to be printed
    numb_test_per_stud = round(total_numb_tests / numb_students)  # average tests per student

    # students with number of records less than the limit
    table_activate_students = df[df["Records"] < numb_test_per_stud]
    print("Number of active students:", len(table_activate_students), "out of", len(df))
    
    # random choice of students
    selected_students = rd.sample(list(table_activate_students["Jmeno"]), NUMB_STUD_PER_HOUR)
    
    # print those students
    for index, student in enumerate(selected_students):
        print(index, student)
