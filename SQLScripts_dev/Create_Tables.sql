use myresearch;

show tables;

-- Create the table
create table mydataset (
	
    id int NOT NULL AUTO_INCREMENT,
    label varchar(50),
    std_label varchar(50),
    oritxt text,
    cleanedtxt text,
    
    translate_chn text,
    translate_my text,
    translate_tm text,
    
    cm_en_chn text,
    cm_en_my text,
    cm_en_tm text,
    
    cm_chn_en text,
    cm_chn_my text,
    cm_chn_tm text,
    
    cm_my_en text,
    cm_my_chn text,
    cm_my_tm text,
    
    cm_tm_en text,
    cm_tm_chn text,
    cm_tm_my text,
    
    cw_en_chn text,
    cw_en_my text,
    cw_en_tm text,
    
    cw_chn_en text,
    cw_chn_my text,
    cw_chn_tm text,
    
    cw_my_en text,
    cw_my_chn text,
    cw_my_tm text,
    
    cw_tm_en text,
    cw_tm_chn text,
    cw_tm_my text,
    
    PRIMARY KEY (id)
);


----------------------------------

use myresearch;

-- drop table tweets_topic;
create table tweets_topic(
	
    id int NOT NULL AUTO_INCREMENT,
	search_txt text,
    url text,
    status varchar(1),

	PRIMARY KEY (id)
);

-- drop table tweets;
create table tweets (
	id int NOT NULL AUTO_INCREMENT,
    topic_id int,
    tweet text,
    clean_text text,
    In_English text,
    pseudo_label text,
    mbert_eng text,
    mbert_mul text,
    xlmr_eng text,
    xlmr_mul text,
    
	PRIMARY KEY (id)
)



-- ALTER TABLE tweets_topic   
ADD COLUMN status varchar(1) default 'N';  

-- ALTER TABLE tweets_topic   
DROP COLUMN is_done;
    
-- ALTER TABLE tweets   
ADD COLUMN clean_text text after tweet


--------------------------------------

drop table model_training;

create table model_training (
	model_name varchar(255),
	epoch int,
    elapsed double,
    training_loss double,
    training_accuracy double,
    val_loss double,
    val_accuracy double,
	PRIMARY KEY (model_name, epoch)
);


--------------------------------------




