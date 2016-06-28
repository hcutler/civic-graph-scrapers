import csv
import json
import os

#read in csv file of Civic Graph entities
entities = []
upper = []
with open("new_civicgraph_entities.csv", "rb") as file:
  data = csv.reader(file)
  entities = list(data)

for e in entities:
  e = str(e).upper()
  upper.append(e)


#read in all 990 files in current directory
entities2 = []
upper2 = []

irsFiles = []
# for n in range(0,17):
#   irsFiles.append("990dumpPartial/filerNames-" + str(n) + ".csv")


for x in os.listdir(os.getcwd()):
    if x.startswith("f") and x.endswith(".csv"):
      irsFiles.append(x)


for f in irsFiles:
  with open(f) as file2:
    data2 = csv.reader(file2)
    entities2 = list(data2)

  for e2 in entities2:
    e2 = str(e2).upper()
    upper2.append(e2)


overlap = []
for i in entities:
  for j in entities2:
    if i == j:
      overlap.append(i)

print overlap
