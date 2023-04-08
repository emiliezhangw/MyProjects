sqlite3 favorites.db
.schema
SELECT * FROM shows;
SELECT * FROM shows ORDER BY title ASC;
UPDATE shows SET title = "How I Met Your Mother" WHERE title = "How i met your mother";
UPDATE shows SET title = "The Queen's Gambit" WHERE id = 73;
SELECT * FROM shows ORDER BY title DESC;
SELECT * FROM shows WHERE title LIKE "%the%";
SELECT * FROM shows ORDER BY title ASC;