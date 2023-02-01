from csv import reader, DictReader
from sys import argv, exit

sequences = {}

#validate input
if len(argv) < 3:
    print("Usage:", "python dna.py data.csv sequence.txt")
    exit(1);

# get maximum number of STR sequence
def get_max(dna, STR):
    i = 0
    j = len(STR)
    max = 0;
    for x in range(len(dna)):
        if dna[i:j] == STR:
            temp = 0;
            while dna[i:j] == STR:
                temp += 1
                i+= len(STR)
                j+= len(STR)
                if(temp > max):
                    max = temp
        else:
            i+=1
            j+=1
    return max


with open(argv[2], 'r') as dnafile:
    dna = dnafile.read()

# open peopleFile to get sequence keyes
with open(argv[1], "r") as peopleFile:
    peopleReader = reader(peopleFile)
    for row in peopleReader:
        header = row
        header.pop(0)
        for item in header:
            sequences[item] = 0;
        break

# give sequence keys value from max function
for key in sequences:
    ans = get_max(dna, key)
    sequences[key] = ans

# print persons if found
with open(argv[1], "r") as peopleFile:
    people = DictReader(peopleFile)
    for person in people:
        match = 0
        for key in sequences:
            if int(person[key]) == sequences[key]:
                match += 1
        if match == len(sequences):
            print(person["name"])
            exit(0)

    print("No match")