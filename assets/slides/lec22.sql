-- lec22.sql: SQL Aggregation Examples using Billboard Hot 100 data

-- 1. Most total songs by artist
-- Shows which artists appeared the most on the Hot 100 chart overall.
SELECT artist, COUNT(*) AS num_songs
FROM billboard
GROUP BY artist
ORDER BY num_songs DESC
LIMIT 5;

-- -- 2. Best average chart performance (lower rank is better)
-- -- Filters to artists with >5 appearances to avoid noise from one-hit wonders.
-- SELECT artist, AVG(rank) AS avg_rank
-- FROM billboard
-- GROUP BY artist
-- HAVING COUNT(*) > 5
-- ORDER BY avg_rank ASC
-- LIMIT 5;

-- -- 3. Songs that stayed on the chart the longest
-- -- Finds the top 5 songs with the most weeks on the Hot 100.
-- SELECT song, artist, MAX("weeks-on-board") AS max_weeks
-- FROM billboard
-- GROUP BY song, artist
-- ORDER BY max_weeks DESC
-- LIMIT 5;

-- -- 4. Number of #1 hits per week
-- -- Counts how many songs were ranked #1 on each chart date.
-- SELECT date, COUNT(*) AS num_1_hits
-- FROM billboard
-- WHERE rank = 1
-- GROUP BY date
-- ORDER BY date
-- LIMIT 5;

-- -- 5. Artists with the most #1 hits
-- -- Aggregates all chart data to find which artists reached rank 1 the most.
-- SELECT artist, COUNT(*) AS num_1_hits
-- FROM billboard
-- WHERE rank = 1
-- GROUP BY artist
-- ORDER BY num_1_hits DESC
-- LIMIT 5;

-- -- 6. Average longevity of songs per artist
-- -- Looks at the average number of weeks artists stayed on the chart.
-- SELECT artist, AVG("weeks-on-board") AS avg_weeks
-- FROM billboard
-- GROUP BY artist
-- ORDER BY avg_weeks DESC
-- LIMIT 5;


-- CREATE TABLE chart_entries AS
-- SELECT date, rank, song, artist
-- FROM billboard;

-- CREATE TABLE chart_entries AS
-- SELECT date, rank, song, artist
-- FROM billboard;


-- -- Join to get song info along with its rank on 2021-11-06
-- SELECT c.date, c.rank, s.song, s.artist, s."peak-rank", s."weeks-on-board"
-- FROM chart_entries AS c
-- JOIN songs AS s
--   ON c.song = s.song AND c.artist = s.artist
-- WHERE c.date = '2021-11-06'
-- ORDER BY c.rank ASC;

-- -- Left join to find songs in songs that never appeared on 2021-11-06
-- SELECT s.song, s.artist, c.rank
-- FROM songs AS s
-- LEFT JOIN chart_entries AS c
--   ON s.song = c.song AND s.artist = c.artist AND c.date = '2021-11-06'
-- WHERE c.rank IS NULL;





