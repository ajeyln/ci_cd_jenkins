# Finding count of charecters in string
''' importing modules'''
import pandas as pd

def count_char(name_1):
    ser = pd.Series(list(name_1))
    freq = ser.value_counts()
    print(freq)
    least_freq = freq.dropna().index[-1]
    "".join(ser.replace(' ', least_freq))
    print("least frequently used charecter is {0}". format(least_freq))

if __name__ == "__main__":
    my_str = input("Enter an string with spaces: ")
    count_char(my_str)
