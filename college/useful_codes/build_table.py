"""
This module contains a list of students, which is exported to an Excel file.
"""

import pandas as pd

if __name__ == "__main__":
    # the list of students
    students_list = [
    'Pavel', 'Karel', 'Pepa', 'Tereza', 'Jan', 'Eva', 'Martin', 'Lucie', 'Jakub', 'Anna',
    'Tomáš', 'Petra', 'Michaela', 'Ondřej', 'Jana', 'Filip', 'Veronika', 'Marek', 'Lenka', 'David',
    'Barbora', 'Radek', 'Kateřina', 'Vojtěch', 'Simona', 'Michal', 'Alena', 'Jakub', 'Ivana', 'Roman'
    ]
    # from that list, we create a DataFrame with a single column
    df = pd.DataFrame(students_list, columns=["Jmeno"])
    # we add 10 columns: Test 1 to Test 10
    for i in range(1,11):
        df[f"Test {i}"] = ""
    # we add one more column: the average success in %
    df["Úspěšnost (%)"] = ""
    # we save the DataFrame as an Excel file
    df.to_excel("studenti_tabulka.ods", index=False)
