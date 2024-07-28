-- Check progress
-- 1. Translation to mandarin, Malay and Tamil
select count(1) from mydataset 
where 
not (
cleanedTxt = '' or cleanedTxt is null
) and not (
	translate_chn is null
    or
    translate_my is null
    or
    translate_tm is null
    
)
union all
select count(1) from mydataset where not (
cleanedTxt = '' or cleanedTxt is null
);


-- 2. Generate code-mixed
select 
count(1)
from mydataset 
where 
not (
cleanedTxt = '' or cleanedTxt is null
)
and not (
    cm_en_chn is null or
    cm_en_my  is null or
    cm_en_tm  is null or

    cm_chn_en  is null or
    cm_chn_my  is null or
    cm_chn_tm  is null or

    cm_my_en  is null or
    cm_my_chn  is null or
    cm_my_tm  is null or

    cm_tm_en is null or
    cm_tm_chn is null or
    cm_tm_my  is null
)
union all
select count(1) 
from mydataset where not (
cleanedTxt = '' or cleanedTxt is null
);



-- 3. Generate code-switched
select 
count(1)
from mydataset 
where 
not (
cleanedTxt = '' or cleanedTxt is null
)
and not (
    cw_en_chn is null or
    cw_en_my  is null or
    cw_en_tm  is null or

    cw_chn_en  is null or
    cw_chn_my  is null or
    cw_chn_tm  is null or

    cw_my_en  is null or
    cw_my_chn  is null or
    cw_my_tm  is null or

    cw_tm_en is null or
    cw_tm_chn is null or
    cw_tm_my  is null
)
union all
select count(1) 
from mydataset where not (
cleanedTxt = '' or cleanedTxt is null
);


-----------------------
-- tweets
-----------------------

select count(1) from tweets_topic where status = 'X';

select count(1) from tweets_topic where status = 'N';

select * from tweets_topic order by ID desc

select * from tweets order by ID desc

select * from tweets_topic where status = 'N';

select ID, SEARCH_TXT, URL from tweets_topic where status = 'N'

select id, tweet from tweets where In_English is null;

select count(url) from tweets_topic where url like '%/people' and status = 'N'
