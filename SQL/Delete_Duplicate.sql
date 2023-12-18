select langchain_pg_embedding.document, count(langchain_pg_embedding.document)
from langchain_pg_embedding
group by langchain_pg_embedding.document
having count(langchain_pg_embedding.document) > 1;

delete from langchain_pg_embedding
using langchain_pg_embedding langchain_pg_embedding_
where langchain_pg_embedding.uuid < langchain_pg_embedding_.uuid
and langchain_pg_embedding.document = langchain_pg_embedding_.document;

select langchain_pg_embedding.document from langchain_pg_embedding 
