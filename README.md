Export data from [spreadsheet](https://docs.google.com/spreadsheets/d/1myKBPm0_4PQek0mBjPlTcxjD0lQsL4GGKBM3zTdT87g/edit#gid=0) as csv.

### Results
```md
$ python3 main.py
-----Decreased By-----
          ΔConnected to Father Culture  ΔConnected to Mother Culture
Asian                        -1.000000                     -0.923077
Black                         0.250000                           NaN
Hispanic                     -1.000000                      0.000000
White                        -0.428571                     -0.500000
Native                             NaN                      1.000000

-----Parent Combos-----
  Father Race Mother Race  Count    Percent
5       White       Asian     12  54.545455
0       Asian       White      3  13.636364
3       Black       White      2   9.090909
1       Black       Asian      1   4.545455
2       Black    Hispanic      1   4.545455
4    Hispanic       White      1   4.545455
6       White    Hispanic      1   4.545455
7       White      Native      1   4.545455
```
