def DNA_strand(dna):
    dna_list=[]
    dna = str(dna)
    output = ""
    for letters in dna.strip():
        dna_list.append(letters)
    for com in range (len(dna_list)):
        match dna_list[com]:
            case 'T':
                dna_list[com]= 'A'
                
            case 'A':
                dna_list[com]= 'T'
                
            case 'C':
                dna_list[com]= 'G'
                
            case 'G':
                dna_list[com]= 'C'
        output=output+dna_list[com]
    return output
DNA_strand("ATTGC")