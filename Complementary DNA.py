def DNA_strand(dna):
    ltt = ''
    for letter in dna:
        match letter:
            case 'A':
                ltt += 'T'
            case 'T':
                ltt += 'A'
            case 'G':
                ltt += 'C'
            case 'C':
                ltt += 'G'
    return ltt
