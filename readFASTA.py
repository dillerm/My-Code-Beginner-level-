#The following code is meant to parse a FAFSA file and return the defline and sequence string
#Note that, if a file contains multiple sequences, the defline of sequences after the first...
#...will be indicated by a '>'

fileName = raw_input('Enter FASTA file name: ') #Prompts user for file name

fastaOpen = open(fileName) #Opens FASTA file based on user's entry

defline = fastaOpen.readline() #Reads Description line in FASTA file

if defline.startswith('>'): #Checks whether or not the first line begins with '>'
    identifier = defline.lstrip('>;')
    print identifier 
else:
    print 'Not a FASTA file'

def read_fasta_file(): #Reads file and returns
    while 1:
        sequence = fastaOpen.read().rstrip()
        if sequence == "" or sequence.endswith('*'):
            break
        print sequence

read_fasta_file()
        