test = {
  'name': 'Problem 5',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> cluster1 = [
          ...     make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
          ...     make_restaurant('B', [1, -1],  [], 1, [make_review('B', 1)]),
          ...     make_restaurant('C', [2, -4],  [], 1, [make_review('C', 5)]),
          ... ]
          >>> find_centroid(cluster1) # should be a pair of decimals
          fd5a452e9bbe526e96baa12996556f9e
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from recommend import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> cluster1 = [
          ...     make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
          ...     make_restaurant('B', [1, -1],  [], 1, [make_review('B', 1)]),
          ...     make_restaurant('C', [2, -4],  [], 1, [make_review('C', 5)]),
          ... ]
          >>> find_centroid(cluster1) # should be a pair of decimals
          [0.0, -3.0]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import recommend
      >>> import tests.test_functions as test
      >>> test.swap_implementations(recommend) # don't violate abstraction!
      >>> from recommend import *
      """,
      'teardown': r"""
      >>> test.restore_implementations(recommend)
      """,
      'type': 'doctest'
    }
  ]
}
