class Tree:
    def __init__(self, value, branches=()):
        self.value = value
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.value, branches_str)

    def is_leaf(self):
        return not self.branches

    def add_branch(self, tree):
        assert isinstance(tree, Tree)
        self.branches.append(tree)


def judge(t):
    """
    >>> point1 = Tree(True)
    >>> point2 = Tree(None, [Tree(True), Tree(True)])
    >>> point3 = Tree(False)
    >>> point4 = Tree(None, [Tree(False), Tree(True), Tree(False)])
    >>> judge(Tree(None, [point1, point2, point3]))#debate1
    True
    >>> judge(Tree(None, [point1, point4, point3]))#debate2
    False
    """
    if t.is_leaf():
        return t.value
    else:
        points_won = 0
        for b in t.branches:
            if judge(b):
                points_won += 1
        if 2 * points_won > len(t.branches):
            return True
        else:
            return False
