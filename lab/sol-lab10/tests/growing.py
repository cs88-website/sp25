test = {
  'name': 'growing',
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
          sqlite> SELECT * FROM growing;
          Bud|29.3
          Bird|25.3
          Pumpkin|25.3
          Tom|26.8
          """,
        },
      ],
    },
  ]
}