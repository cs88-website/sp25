test = {
  'name': 'big',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read lab10.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> SELECT name, ROUND(pounds, 2) FROM big;
          Flappy|40.48
          Pumpkin|42.46
          Tom|58.96
          Waddle|48.62
          """,
        },
      ],
    },
  ]
}