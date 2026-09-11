CREATE TABLE IF NOT EXISTS page_counter (
	count INT NOT NULL DEFAULT 0
);

INSERT INTO page_counter (count)
SELECT 0
WHERE NOT EXISTS (SELECT 1 FROM page_counter);
