#Recitation0


'''In this recitation, you will complete the Knuth-Morris-Pratt string matching algorithm.
I wrote the function compute_table, which tells you how much to shift the gene when a mismatch is found.
You must complete the algorithm by completing the function, kmp.
'''
def compute_table(gene):
    '''Expect that gene is a string.
    returns a list of indices. The jth index in the list indicates how many places to move the pattern if a mismatch occurs at position j.
    This is not the most efficient way to do this. This is an O(m^3) algorithm, where m is the length of gene.
    I've written it this way because this is the most direct way to describe how the table is defined.
    A better implementation can run in linear time, O(m).
    '''
    table = []
    for j,g in enumerate(gene):
        shift_when_mismatch_at_j = min([s for s in range(j+1) if gene[:j-s]==gene[s:j] and gene[j]!= gene[j-s]], default = j+1)
        table.append(shift_when_mismatch_at_j)
    return table

def test_compute_table():
    gene = "abcabcacab"
    print(compute_table(gene))
    ideal_answer=  [ j - i +1 for j,i in enumerate([0,1,1,0,1,1,0,5,0,1])] #See Knuth's paper, keep in mind he starts indexing at 1 instead of 0.
    assert compute_table(gene)== ideal_answer
test_compute_table()
#print( compute_table("abcabcacab"))

def kmp(gene,genome): 
    if len(gene) < 1:
        return True #True if gene is "" because empty string is contained in genome
    if len(genome) < 1:
        return False #False if genome is ""
    table = compute_table(gene)
    i = 0 #Index for gene
    j = 0 #Index for genome
    while j < len(genome): #Checking index is not larger than length of genome
        if gene[i] == genome[j]:
            i+=1
            j+=1
        if i == len(gene): #If you get through the entire string then return true
            return True
        else:
            if i > 0: 
                j = table[i + 1] #Use compute_table function to start at next right index j
            else: 
                j+=1
            i = 0   #Reset to first element of gene       
    return False
    

    ''' Your code here.
        Implement the Knuth-Morris-Pratt algorithm: On input gene and genome, it should return True if gene in genome and False otherwise.
        Your code should not use string comparison to compare strings of length 2 or more.
        This is because we are pretending to code in C, where we must compare each element of an array, individually.
    '''
    pass

def test_kmp():
    '''
    Do not modify this code. Make sure that this test passes before pushing your code to github.
    '''
    genes = ["", "a","t", "att", "cat", "catacatttcat", "ggggaa", "atatatatat", "aaaat", "aaaa"]
    genomes = ["", "a", "catacattaccattacgaccag", "atgcacattatatatatatgcatat", "gggggggaaaaaaaa", "aaa", "taaa"]

    for gene in genes:
        for genome in genomes: #tests every pair of gene and genome.
            # You can uncomment out this to help you debug.
            print("gene, genome", gene, genome)
            print(kmp(gene, genome))
            print(gene in genome)
            assert(kmp(gene, genome) == (gene in genome) ) #asserts that the kmp function returns the same value as the builtin 'in' function.
test_kmp()
