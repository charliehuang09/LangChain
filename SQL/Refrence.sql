select * from langchain_pg_embedding limit 10

select distinct collection_id from langchain_pg_embedding;

select * from langchain_pg_embedding
where
collection_id = 'e9a1ed87-7647-48e1-9f3b-142ce25846cc'
and
uuid = '3e582250-4755-4130-9ee3-6b9e9371a203';

select uuid from langchain_pg_embedding
order by uuid desc
limit 5;

update langchain_pg_embedding 
set custom_id=5 
where uuid = '3e582250-4755-4130-9ee3-6b9e9371a203';
select * from langchain_pg_embedding where uuid = '3e582250-4755-4130-9ee3-6b9e9371a203';

delete from langchain_pg_embedding
where uuid = '3e582250-4755-4130-9ee3-6b9e9371a203';
select * from langchain_pg_embedding where uuid = '3e582250-4755-4130-9ee3-6b9e9371a203'; 

truncate table langchain_pg_embedding

alter table langchain_pg_embedding add delete int;
alter table langchain_pg_embedding alter delete type bool;
alter table langchain_pg_embedding drop column delete;

select * from langchain_pg_embedding where custom_id between 1 and 3

select document as __document__ from langchain_pg_embedding as tmp

select * from langchain_pg_embedding
where uuid in ('3b85f6ae-9345-4dba-8b88-36a0d322c79a', '387fda40-f475-48b3-92ce-75a535c8bf9c')

select document from langchain_pg_embedding
where lower(document) like '%apriltag%'--like wildcard

--insert into tablea select * from tableb where condition

