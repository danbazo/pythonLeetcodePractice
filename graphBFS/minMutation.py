def minMutation(startGene, endGene, bank):
    if startGene==endGene: return 0
    bank=set(bank)
    if endGene not in bank: return -1
    geneCharacters=set(["A","C","G","T"])
    currentGenes=[startGene]
    mutationCount=0
    while currentGenes:
        mutationCount+=1
        newGenes=[]
        for gene in currentGenes:
            for i in range(len(gene)):
                for letter in geneCharacters:
                
                    if letter!=gene[i]:
                        possibleGene=gene[:i]+letter+gene[i+1:]
                        if possibleGene in bank:
                            if possibleGene==endGene: return mutationCount
                            newGenes.append(possibleGene)
                            bank.remove(possibleGene)
        currentGenes=newGenes
    return -1
