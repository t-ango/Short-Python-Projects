def main():
    '''
    The main function serves as the entry point of the program. It performs the following:
    
    - Prompts the user to input a genome string.
    - Converts the genome string to uppercase for consistency.
    - Calls the `find_genes` function to identify genes within the genome string.
    - Outputs the found genes as a comma-separated list.
    - If no genes are found, it displays a message: "No gene is found."
    '''
    genome_sequence = input("Enter a genome string: ").upper()
    genes = find_genes(genome_sequence)
    
    if genes:
        print(",".join(genes))
    else:
        print("No gene is found.")
        

def find_genes(genome):
    '''
    The `find_genes` function identifies and extracts genes from a given genome string.

    - **Input**: A string representing the genome sequence (in uppercase).
    - **Process**:
      1. Looks for start codons ("ATG").
      2. Searches for the nearest stop codons ("TAG", "TAA", "TGA") after each start codon.
      3. Extracts the substring (gene) located between the start codon and the nearest stop codon.
      4. Repeats the process for all occurrences of start and stop codons in the genome.
    - **Output**: A list of genes (substrings between start and stop codons).
      - If no genes are found, the list is empty.
    '''
    start_sequense = "ATG"
    stop_sequenses = ["TAG", "TAA", "TGA"]
    
    genes_found = []
    start_index = genome.find(start_sequense)
    
    while start_index != -1:
        end_index = -1
        for stop_sequense in stop_sequenses:
            stop_index = genome.find(stop_sequense, start_index + 3)
            if stop_index != -1:
                if end_index == -1 or stop_index < end_index:
                    end_index = stop_index
        
        if end_index != -1:
            genes_found.append(genome[start_index + 3:end_index])
        
        start_index = genome.find(start_sequense, start_index + 3)
    
    return genes_found


main()