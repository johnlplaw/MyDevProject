select * from model_training;

-- The model name list
select distinct model_name from model_training where model_name like 'Final_%';

-- Select the time spend for the model finetuning
select * from (

select model_name, 
sum(elapsed) as total_seconds,
SEC_TO_TIME(sum(elapsed)) as total_time
from model_training where model_name in
(
select distinct model_name from model_training where model_name like 'Final_%'
) group by model_name

) as src
order by src.total_seconds;



