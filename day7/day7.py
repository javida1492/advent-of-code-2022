# Build a directory tree
# A Node will have:
#   - A left and right node
#   - Type (file or folder) & Size
# Lead nodes by default will be files
# Intermediate nodes by default will be folders
# Once tree is built, dfs into the tree and populate folder sizing
# Once we find folder sizes that are <= 100,000, Add to set

from anytree import Node, RenderTree, search, AsciiStyle, PostOrderIter
max_level = 2
def process_cd(cd, root, current_node): 
    if cd == "..":
        if not current_node.name == "/":
            return current_node.parent
        else:
            return current_node
    else:
        if not search.find(current_node, lambda node: node.name==cd, maxlevel=max_level):
            #Create the folder
            Node(cd, size=0, parent=current_node, type="folder")
        # CD into the folder
        return search.find(current_node, lambda node: node.name==cd, maxlevel=max_level)


def process_ls(line, current_node):
    if(line[0] == "dir"):
        if not search.find(current_node, lambda node: node.name == line[1], maxlevel=max_level):
            Node(line[1], size=0, parent=current_node, type="folder")
    else:
        if not search.find(current_node, lambda node: node.name == line[1], maxlevel=max_level):
            Node(line[1], size=int(line[0]), parent=current_node, type="file")
            # current_node.size += int(line[0])

def calculate_sizes(root):
    sizes = []
    for node in PostOrderIter(root):
        if node.type == "file":
            node.parent.size += node.size
        else:
            # if node.size <= 100000:
            sizes.append(node.size)
            if not node.name == "/":
                node.parent.size += node.size

    return sizes

def binary_search(sizes, diff):
    left= int(0)
    right=int(len(sizes))

    while left <= right:
        middle = int(left + (right - left)/2)

        if sizes[middle] > diff and sizes[middle-1] > diff:
            right = middle - 1
        elif sizes[middle] < diff and sizes[middle+1] < diff:
            left = middle + 1
        elif sizes[middle] > diff and sizes[middle-1] < diff:
            return int(middle)
        elif sizes[middle] < diff and sizes[middle+1] > diff:
            return int(middle+1)

with open("input.txt") as f:
    lines = f.readlines()

    sizes = []
    root = Node(name="/", size=0, parent=None, type="folder")
    current_node = root
    current_instruction = ""
    count = 0
    for line in lines:
        line = line.strip("\n")
        line = line.split()
        if line[1] == "ls":
            current_instruction = "ls"
        elif line[1] == "cd":
            current_instruction = "cd"
            current_node = process_cd(line[2], root, current_node)
        elif current_instruction == "ls":
            process_ls(line, current_node)
        count += 1

    sizes = sorted(calculate_sizes(root))

    # print(RenderTree(root))
    # print(RenderTree(root, style=AsciiStyle()).by_attr())
    print(sizes)
    total_size = 0
    total_disk_space = 70000000

    for size in sizes:
        total_size += size

    diff = total_disk_space - root.size
    unused = 30000000
    print(unused-diff)
    idx = int(binary_search(sizes, unused-diff))
    print("Total size: " + str(total_size))
    print("Diff: " + str(total_disk_space - root.size))
    print("Folder size to delete: " + str(sizes[idx]))