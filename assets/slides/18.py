class Tree:
    """A tree is a label and a list of branches."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

def print_sums(t):
    return print_sums_helper(t, 0)

def print_sums_helper(t, path_sum):
    path_sum += t.label
    if t.is_leaf():
        print(path_sum)

def count_leaves(t):
    """Count the leaves of a tree."""
    if t.is_leaf():
        return 1
    else:
        branch_counts = [count_leaves(b) for b in t.branches]
        return sum(branch_counts)

def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented."""
    if t.is_leaf():
        return Tree(t.label + 1)
    else:
        branches = [increment_leaves(b) for b in t.branches]
        return Tree(t.label, branches)

def increment_leaves_in_place(t):
    """Return a tree like t but with leaf labels incremented."""
    if t.is_leaf():
        t.label = t.label + 1
    else:
        for b in t.branches:
            increment_leaves_in_place(b)


def increment(t):
    """Return a tree like t but with all labels incremented."""
    return Tree(t.label + 1, [increment(b) for b in t.branches])

def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    # print(f"Deptrh? {indent}")
    print(f"{'     ' * indent}{t.value}")

    for b in t.branches:
        print_tree(b, indent + 1)

def count_nodes(t):
    """The number of leaves in tree."""
    return 1 + sum(map(count_nodes, t.branches))

def count_paths(t, total):
    """Return the number of paths from the root to any node in tree t
    for which the labels along the path sum to total.

    >>> t = Tree(3, [Tree(-1), Tree(1, [Tree(2, [Tree(1)]), Tree(3)]), Tree(1, [Tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if t.label == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - t.label) for b in t.branches])

def fib_tree(n):
    if n <= 1:
        return Tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return Tree(left.label + right.label, [left, right])

t = Tree(3, [Tree(-1), Tree(1, [Tree(2, [Tree(1)]), Tree(3)]), Tree(1, [Tree(-1)])])
small_tree = Tree(1, [Tree(2), Tree(3)])
med_tree = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])

uc_berkeley = Tree('UC Berkeley', [
        Tree('College of Letters & Science', [
            Tree('Mathematics'),
            Tree('Physics'),
            Tree('Economics')
        ]),
        Tree('College of Engineering', [
            Tree('EECS'),
            Tree('Civil Engineering'),
            Tree('Mechanical Engineering')
        ]),
        Tree('College of Chemistry', [
            Tree('Chemistry'),
            Tree('Chemical Engineering')
        ]),
        Tree('Haas School of Business', [
            Tree('Business Administration'),
            Tree('Finance')
        ]),
        Tree('College of Environmental Design', [
            Tree('Architecture'),
            Tree('City Planning')
        ]),
        Tree('College of Computing, Data Science, and Society', [
            Tree('Computer Science'),
            Tree('Statistics'),
            Tree('Data Science')
        ])
    ])

uc_system = Tree('UCOP', [
    Tree('UC Berkeley'),
    Tree('UC Davis'),
    Tree('UC Irvine'),
    Tree('UC Los Angeles'),
    Tree('UC Merced'),
    Tree('UC Riverside'),
    Tree('UC San Diego'),
    Tree('UC San Francisco'),
    Tree('UC Santa Barbara'),
    Tree('UC Santa Cruz')
])

uc_system_with_cal = Tree('UCOP', [
    uc_berkeley,
    Tree('UC Davis'),
    Tree('UC Irvine'),
    Tree('UC Los Angeles'),
    Tree('UC Merced'),
    Tree('UC Riverside'),
    Tree('UC San Diego'),
    Tree('UC San Francisco'),
    Tree('UC Santa Barbara'),
    Tree('UC Santa Cruz')
])
