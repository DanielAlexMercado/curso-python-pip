import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            # print(list(iterable))
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data
            # print(country_dict)
            # print('***' * 5)
            # print(row)

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    print(data[0])
    


"""
def read_csv(path):
   with open(path, 'r') as csvfile:      
      total = sum(int(r[1]) for r in csv.reader(csvfile))
      return total

response = read_csv('./data.csv')
print(response)

"""

"""
import csv
import functools

def read_csv(path):
   # Tu código aquí 👇
   with open(path) as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      data = list()
      for line in reader:
         data.append(int(line[1]))
   total = functools.reduce(lambda x,y: x+y, data)
   return total

response = read_csv('./data.csv')
print(response)
"""
