test = {
  'name': 'Problem 7',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'fb82a22c057637e022eb7ddae6aaea79',
          'choices': [
            'the restaurants in restaurants',
            'the names of restaurants in restaurants',
            'the extracted values for each restaurant in restaurants',
            'the restaurants reviewed by user'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does the list xs represent?'
        },
        {
          'answer': '2caff30c9cfd0d45a873304adfe81d51',
          'choices': [
            'the scores for the restaurants reviewed by user',
            'the scores for the restaurants in restaurants',
            'the names for the restaurants reviewed by user',
            'the names for the restaurants in restaurants'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does the list ys represent?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> user = make_user('John D.', [
          ...     make_review('A', 1),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 2.5),
          ... ])
          >>> restaurant = make_restaurant('New', [-10, 2], [], 2, [
          ...         make_review('New', 4),
          ... ])
          >>> cluster = [
          ...     make_restaurant('B', [4, 2], [], 1, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 2)
          ...     ]),
          ...     make_restaurant('D', [4, 2], [], 3.5, [
          ...         make_review('D', 2.5),
          ...         make_review('D', 3),
          ...     ]),
          ... ]
          >>> pred, r_squared = find_predictor(user, cluster, restaurant_price)
          >>> round(pred(restaurant), 5)
          4.0
          >>> round(r_squared, 5)
          1.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> user = make_user('John D.', [
          ...     make_review('A', 1),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 2.5),
          ... ])
          >>> restaurant = make_restaurant('New', [-10, 2], [], 2, [
          ...         make_review('New', 4),
          ... ])
          >>> cluster = [
          ...     make_restaurant('B', [4, 2], [], 1, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 2)
          ...     ]),
          ...     make_restaurant('D', [4, 2], [], 3.5, [
          ...         make_review('D', 2.5),
          ...         make_review('D', 3),
          ...     ]),
          ... ]
          >>> pred, r_squared = find_predictor(user, cluster, restaurant_mean_score)
          >>> round(pred(restaurant), 5)
          3.9359
          >>> round(r_squared, 5)
          0.99256
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> user = make_user('John D.', [
          ...     make_review('A', 1),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 2.5),
          ... ])
          >>> restaurant = make_restaurant('New', [-10, 2], [], 2, [
          ...         make_review('New', 4),
          ... ])
          >>> cluster = [
          ...     make_restaurant('B', [4, 2], [], 1, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 2)
          ...     ]),
          ...     make_restaurant('D', [4, 2], [], 3.5, [
          ...         make_review('D', 2.5),
          ...         make_review('D', 3),
          ...     ]),
          ... ]
          >>> pred, r_squared = find_predictor(user, cluster, restaurant_num_scores)
          >>> round(pred(restaurant), 5)
          3.5
          >>> round(r_squared, 5)
          0.12903
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> import recommend
      >>> test.swap_implementations(recommend)
      >>> from recommend import *
      """,
      'teardown': r"""
      >>> test.restore_implementations(recommend)
      """,
      'type': 'doctest'
    }
  ]
}
