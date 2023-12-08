with tmp as(
	SELECT document, 
	embedding, 
	COUNT(*) AS COUNT FROM langchain_pg_embedding
	GROUP BY document, embedding HAVING COUNT(*) > 1
)
SELECT * FROM tmp