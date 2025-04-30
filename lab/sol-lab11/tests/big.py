test = {
  'name': 'big',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read lab11.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> SELECT * FROM big;
          61A
          61B
          61C
          """,
        },
      ],
    },
  ]
}