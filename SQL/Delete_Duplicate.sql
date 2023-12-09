-- select * from langchain_pg_embedding
-- where(
-- 	 langchain_pg_embedding.uuid in (
-- 		 select langchain_pg_embedding.uuid from langchain_pg_embedding
-- 		 having count(langchain_pg_embedding.document) = 3

-- 	 )
-- )





select langchain_pg_embedding.uuid from langchain_pg_embedding
having count(langchain_pg_embedding.document) = 3


