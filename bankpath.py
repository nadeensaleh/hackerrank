tree = {}

def addNodeToTree(node):
    parent = node[0]
    child = node[1]
    if parent in tree:
        if type(tree[parent]) != list:
            tree[parent] = [tree[parent]]
        tree[parent].append(child)
    else:
        tree[parent] = child
        
def getParent(node):
    for n in tree:
        children = tree[n]
        if type(children) == list:
            for t in children:
                if t == node:
                    return n
        elif node == children:
            return n
    return None
            
def path_length(src, dest, threshold):
    visited = {}
    dest_found = False
    num_hops = 0
    search = [(src, 0)]
    while len(search) > 0:
        print "Search domain: " + str(search)
        current_tup = search.pop()
        current = current_tup[0]
        current_hops = current_tup[1]
        visited[current] = True
        
        if current == dest:
            # We found the destination!
            num_hops = current_hops
            dest_found = True
            break
        else:
            # If this is true, then current has children
            if current in tree:
                children = tree[current]
                # Children is not a list and is therefore a tuple containing the (key, dist_from_src)
                if type(children) != list and children not in visited:
                    search.append((children, current_hops + 1))
                elif type(children) == list:
                    for child in children:
                        # Only add child if it hasn't been visited
                        if child not in visited:
                            search.append((child, current_hops + 1))
            parent = getParent(current)
            if parent not in visited and parent != None:
                search.append((parent, current_hops + 1))
    if num_hops <= threshold:
        return "Found a path with %d hops!" % num_hops
    else:
        return "No path found under the threshold."


addNodeToTree((1, 7))
addNodeToTree((1, 3))
addNodeToTree((1, 5))
addNodeToTree((5, 2))
addNodeToTree((5, 4))
addNodeToTree((2, 6))

src = 6
dest = 6

print(tree)
print(path_length(src, dest, 100))
