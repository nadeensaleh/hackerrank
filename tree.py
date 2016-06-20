tree = {}

def addNodeToTree(node):
    parent = node[0]
    child = node[1]
    if parent in tree:
        """Insert a value in dict at key if one does not exist
        Otherwise, convert value to list and append"""
        if type(tree[parent]) != list:
            tree[parent] = [tree[parent]]
        tree[parent].append(child)
    else:
        tree[parent] = child  
        
def getParent(node):
    for n in tree:
        children = tree[n]
        if (type(children) == list and node in children) or node == children:
            return n
    return None
            
def is_sublist(a, b):
    if a == []: return True
    if b == []: return False
    return b[:len(a)] == a or is_sublist(a, b[1:])

addNodeToTree((1, 7))
addNodeToTree((1, 3))
addNodeToTree((1, 5))
addNodeToTree((5, 2))
addNodeToTree((5, 4))
addNodeToTree((2, 6))

print tree

counter_th = 0
last_search = []
visited = {}
src = 7
dest = 4
dest_found = False
while not dest_found:
    search = [src]
    while len(search) > 0:
        current = search.pop()
        visited[current] = True
        if current == dest:
            dest_found = True
            break
        if current in tree:
            if type(tree[current]) != list and tree[current] not in visited:
                search.append(tree[current])
            if type(tree[current]) == list:
                for child in tree[current]:
                    if child not in visited:
                        search.append(child)
        parent = getParent(current)
        if parent not in visited and parent != None:
            search.append(parent)

        print search, last_search
        if((set(search).issubset(set(last_search)) == False)):
            counter_th += 1
            print counter_th
            
        last_search = list(search)

    dest_found = True
        
print dest_found
if (counter_th > th):
    r_message = "NO"
