# read large file data chunk by chunk using generator 
import csv

def read_large_file(fileobj):
    while True:
        data = fileobj.readline()
        # break if this is end of the file
        if not data:
            break
        # otherwise return data 
        yield data 

def main():
    with open('Codes/Pandas/baby_names.csv') as file:
        gen_file = read_large_file(file)

    file.close()
    print(next(gen_file)) 
    print(next(gen_file))
    print(next(gen_file))

main()     