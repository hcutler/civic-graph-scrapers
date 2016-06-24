import csv
import json


with open("term_counts.json", "r") as file:
  data = file.read()
  x = json.loads(x)
  f = csv.writer(open("test.csv", "wb+"))
  
