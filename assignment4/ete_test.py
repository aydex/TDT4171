from ete3 import Tree

t = Tree('((((H,K)D,(F,I)G)B,E)A,((L,(N,Q)O)J,(P,S)M)C)X;', format=1)
print t.get_ascii(show_internal=True)

#print rooted_tree