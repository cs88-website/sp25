CREATE TABLE songs AS
  SELECT "WILDFLOWER" as track, "Billie Eilish" as artist
  UNION
  SELECT "BIRDS OF A FEATHER" , "Billie Eilish"
  UNION
  SELECT "360"                , "Charli xcx"
  UNION
  SELECT "Pasilyo"            , "Sunkissed Lola"
  UNION
  SELECT "Cinderella"         , "Remi Wolf"
  UNION
  SELECT "Good Luck Babe!"    , "Chappell Roan"
  UNION
  SELECT "Meow"               , "Anamanaguchi";

CREATE TABLE more_songs AS
  SELECT * FROM songs
  UNION SELECT 'Fearless' AS track, 'Taylor Swift' AS artist
  UNION SELECT 'Fifteen', 'Taylor Swift'
  UNION SELECT 'Love Story', 'Taylor Swift'
  UNION SELECT 'Hey Stephen', 'Taylor Swift'
  UNION SELECT 'White Horse', 'Taylor Swift'
  UNION SELECT 'You Belong with Me', 'Taylor Swift'
  UNION SELECT 'Breathe', 'Taylor Swift featuring Colbie Caillat'
  UNION SELECT 'Tell Me Why', 'Taylor Swift'
  UNION SELECT 'You''re Not Sorry', 'Taylor Swift'
  UNION SELECT 'The Way I Loved You', 'Taylor Swift'
  UNION SELECT 'Forever & Always', 'Taylor Swift'
  UNION SELECT 'The Best Day', 'Taylor Swift'
  UNION SELECT 'Change', 'Taylor Swift';
