-- -------------------------------
-- All record
-- -------------------------------
select * from tweets_topic;

select * from tweets;

select distinct model_name from model_training;

select *  from mydataset where id = 100000; 

Select std_label,
	cleanedtxt,
    translate_chn,
    translate_my,
    translate_tm,
    
    cm_en_chn,
    cm_en_my,
    cm_en_tm,
    
    cm_chn_en,
    cm_chn_my,
    cm_chn_tm,
    
    cm_my_en,
    cm_my_chn,
    cm_my_tm,
    
    cm_tm_en,
    cm_tm_chn,
    cm_tm_my,
    
    cw_en_chn,
    cw_en_my,
    cw_en_tm,
    
    cw_chn_en,
    cw_chn_my,
    cw_chn_tm,
    
    cw_my_en,
    cw_my_chn,
    cw_my_tm,
    
    cw_tm_en,
    cw_tm_chn,
    cw_tm_my
    from mydataset;

select * from tweets_topic;
select * from tweets;

select id, clean_text, pseudo_label from tweets where length(clean_text) > 0;

select * from tweets;

select
mbert_eng,
mbert_mul,
xlmr_eng,
xlmr_mul
from tweets;


select * from model_training where model_name like 'Chk%'

-- -------------------------------
-- Analysis
-- -------------------------------

select max(LENGTH(oritxt)) from mydataset;

select avg(LENGTH(oritxt)) from mydataset;

select mod(LENGTH(oritxt)) from mydataset;

select pseudo_label, count(1) from tweets group by pseudo_label;

Select length(tweet), length(clean_text) from tweets; 

select * from model_training where model_name = 'XLM-R_English_800_ori_RO3'

select sum(elapsed)/3600 from model_training where model_name = 'XLM-R_English_800_ori_RO3'


select count(1), std_label from mydataset group by std_label;

select count(1) from mydataset;

select distinct model_name from model_training;

select model_name, sum(elapsed)/60 from model_training group by model_name;



select model_name, max(Elapsed), max(epoch) from model_training group by model_name;


select model_name, max(elapsed) from model_training group by model_name;


select * from  model_training where model_name = 'mBERT_Multilingual_400_ori_RO3_batch'

select model_name from model_training group by model_name order by model_name;

select model_name, max(epoch) from model_training where model_name like 'Chk-FB_%' group by model_name;

select * from model_training;


-- ==============
use myresearch;

show tables;

select * from mydataset limit 10;

-- To get the initial dataset
select count(1), std_label from mydataset group by std_label;

-- To get the accepted dataset
select count(1), std_label from mydataset where cleanedtxt is not null group by std_label;

select median(CHAR_LENGTH(cleanedtxt)) from mydataset limit 10;

-- To get the median length char num
SELECT AVG(middle_values) AS median_length
FROM (
    SELECT field_length AS middle_values
    FROM (
        SELECT field_length,
               @rownum:=@rownum+1 AS `row_number`,
               @total_rows:=@rownum AS `total_rows`
          FROM (
            SELECT CHAR_LENGTH(cleanedtxt) AS field_length
              FROM mydataset
          ORDER BY field_length
               ) AS derived_table1
        JOIN (SELECT @rownum:=0) AS derived_table2
     ) AS derived_table3
WHERE `row_number` IN ( FLOOR((@total_rows+1)/2), FLOOR((@total_rows+2)/2) )
) AS derived_table4;

-- To find the everage
select avg(CHAR_LENGTH(cleanedtxt)) from mydataset limit 10;

-- =======================


-- ========================
-- model performance analysis

use myresearch;

select model_name, max(training_accuracy), max(val_accuracy) from model_training group by model_name;

-- Get training and eval accuracy

select distinct model_name from model_training 
where model_name like 'mBERT_English%'
order by model_name;

select round(training_accuracy, 4) as training_accuracy, round(val_accuracy, 4) as val_accuracy from model_training where model_name = 'mBERT_English_1200_ori_RO3_Batch_8'
order by epoch;


select round(training_accuracy, 4) as training_accuracy, round(val_accuracy, 4) as val_accuracy 
from model_training 
where model_name = 'mBERT_English_1200_ori_RO3_Batch_8'
order by epoch;


select *  from model_training where model_name like 'Chk_mBERT%' order by model_name, epoch;

-- ========================
