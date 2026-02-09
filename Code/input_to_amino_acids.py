import sys
gene_name = input("please enter a name for the DNA sequnence:" )
print(f'Your sequnce name is:{gene_name}')
sequence_length = float(input("please enter the length of the sequnce:"))
print(f'the length of the sequence is{sequence_length}')
decoded_protein_length = sequence_length/3
print(f'The length of the decoded protein is:{decoded_protein_length}')
if decoded_protein_length % 3 !=0 :
    print("\n\nthe DNA sequence is not a multiple of 3", file = sys.stderr)
    sys.exit(1)
average_weight_protein_sequence = decoded_protein_length * 110 / 1000
print(f'The average weight of the protein sequence is:{average_weight_protein_sequence}')