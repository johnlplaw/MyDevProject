-- 1) English
select cleanedtxt, std_label from mydataset;


-- 2) Multilingual

select cleanedtxt, std_label from mydataset
union all
select translate_chn, std_label from mydataset
union all
select translate_my, std_label from mydataset
union all
select translate_tm, std_label from mydataset
union all
select cm_en_chn, std_label from mydataset
union all
select cm_en_my, std_label from mydataset
union all
select cm_en_tm, std_label from mydataset
union all
select cm_chn_en, std_label from mydataset
union all
select cm_chn_my, std_label from mydataset
union all
select cm_chn_tm, std_label from mydataset
union all
select cm_my_en, std_label from mydataset
union all
select cm_my_chn, std_label from mydataset
union all
select cm_my_tm, std_label from mydataset
union all
select cm_tm_en, std_label from mydataset
union all
select cm_tm_chn, std_label from mydataset
union all
select cm_tm_my, std_label from mydataset
union all
select cw_en_chn, std_label from mydataset
union all
select cw_en_my, std_label from mydataset
union all
select cw_en_tm, std_label from mydataset
union all
select cw_chn_en, std_label from mydataset
union all
select cw_chn_my, std_label from mydataset
union all
select cw_chn_tm, std_label from mydataset
union all
select cw_my_en, std_label from mydataset
union all
select cw_my_chn, std_label from mydataset
union all
select cw_my_tm, std_label from mydataset
union all
select cw_tm_en, std_label from mydataset
union all
select cw_tm_chn, std_label from mydataset
union all
select cw_tm_my, std_label from mydataset;