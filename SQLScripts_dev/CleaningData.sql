update mydataset set std_label = 'Happy' where label in ('happy');
update mydataset set std_label = 'Happy' where label in ('joy');
update mydataset set std_label = 'Happy' where label in ('happiness');

update mydataset set std_label = 'Angry' where label in ('anger');
update mydataset set std_label = 'Angry' where label in ('angry');

update mydataset set std_label = 'Sad' where label in ('sadness');
update mydataset set std_label = 'Sad' where label in ('disappointed');

update mydataset set std_label = 'Surprise' where label in ('surprise');

update mydataset set std_label = 'Fear' where label in ('fear');

update mydataset set std_label = 'Fear' where label in ('worry');

update mydataset set std_label = 'Neutral' where label in ('neutral');


Select
        CASE
            WHEN std_label = 'Neutral' THEN '0'
            WHEN std_label = 'Happy' THEN '1'
            WHEN std_label = 'Fear' THEN '2'
            WHEN std_label = 'Surprise' THEN '3'
            WHEN std_label = 'Angry' THEN '4'
            WHEN std_label = 'Sad' THEN '5'
            ELSE '-1'
        END AS std_label
from mydataset limit 100;

-- ==================
select * from mydataset order by id desc limit 10;

update mydataset set
translate_chn = lower(translate_chn), translate_my = lower(translate_my), translate_tm = lower(translate_tm),
cm_en_chn = lower(cm_en_chn), cm_en_my = lower(cm_en_my), cm_en_tm = lower(cm_en_tm),
cm_chn_en = lower(cm_chn_en), cm_chn_my = lower(cm_chn_my), cm_chn_tm = lower(cm_chn_tm),
cm_my_en = lower(cm_my_en), cm_my_chn = lower(cm_my_chn), cm_my_tm = lower(cm_my_tm),
cm_tm_en = lower(cm_tm_en), cm_tm_chn = lower(cm_tm_chn), cm_tm_my = lower(cm_tm_my);