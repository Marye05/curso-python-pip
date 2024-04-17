import csv

def read_csv(path):
  with open(path, 'r') as csvfile: #permiso de lectura con la r
    reader = csv.reader(csvfile, delimiter=';') #delimiter la forma en que vienen separado los datos del archivo
    header = next(reader)
    data = []
    for row in reader: #iteramos y leemos fila a fila
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv') #acá que lea el archivo
  print(data[0])