# tests
import csv

with open('streamers.txt', 'r') as f:
    r_list = f.read().split('\n')

print(r_list)

for i in r_list:
    print(i)