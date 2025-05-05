test = {
  'name': 'matchmaker',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read hw11.sql
      """,
      'cases': [
        {
            'code': r"""
            sqlite> SELECT * FROM matchmaker LIMIT 10;
            dog|Dancing Queen|green|blue
            dog|Dancing Queen|green|blue
            dog|Dancing Queen|green|pink
            dog|Dancing Queen|green|green
            dog|Bohemian Rhapsody|lavender|orange
            dog|Bohemian Rhapsody|lavender|blue
            dog|Bohemian Rhapsody|lavender|orange
            dog|Bohemian Rhapsody|lavender|black
            dog|Shake It Off|black|blue
            dog|Shake It Off|black|blue
            """,
          'hidden': False,
          'locked': False
        }
      ],
    }
  ]
}