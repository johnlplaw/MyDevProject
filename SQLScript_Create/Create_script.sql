-- ------------
-- Schema
-- ------------
CREATE DATABASE `myresearch` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

-- ------------
-- Training dataset
-- ------------

CREATE TABLE `Synth_text` (
  `id` int NOT NULL AUTO_INCREMENT,
  `label` varchar(50) DEFAULT NULL,
  `std_label` varchar(50) DEFAULT NULL,
  `pseudo_label` varchar(255) DEFAULT NULL,
  `oritxt` text,
  `cleanedtxt` text,
  `translate_chn` text,
  `translate_my` text,
  `translate_tm` text,
  `cm_en_chn` text,
  `cm_en_my` text,
  `cm_en_tm` text,
  `cm_chn_en` text,
  `cm_chn_my` text,
  `cm_chn_tm` text,
  `cm_my_en` text,
  `cm_my_chn` text,
  `cm_my_tm` text,
  `cm_tm_en` text,
  `cm_tm_chn` text,
  `cm_tm_my` text,
  `cw_en_chn` text,
  `cw_en_my` text,
  `cw_en_tm` text,
  `cw_chn_en` text,
  `cw_chn_my` text,
  `cw_chn_tm` text,
  `cw_my_en` text,
  `cw_my_chn` text,
  `cw_my_tm` text,
  `cw_tm_en` text,
  `cw_tm_chn` text,
  `cw_tm_my` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=981009 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `ChatGPT_text` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ori_text` text,
  `text_type` text,
  `lang` text,
  `label` text,
  `pseudo_label` varchar(255) DEFAULT NULL,
  `In_English` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49616 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- --------------
-- Evaluation Dataset
-- --------------

CREATE TABLE `tweets_topic` (
  `id` int NOT NULL AUTO_INCREMENT,
  `search_txt` text,
  `url` text,
  `status` varchar(1) DEFAULT 'N',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5284 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `tweets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `topic_id` int DEFAULT NULL,
  `tweet` text,
  `clean_text` text,
  `In_English` text,
  `pseudo_label` text,
  `mbert_eng` text,
  `mbert_mul` text,
  `xlmr_eng` text,
  `xlmr_mul` text,
  `mbert_eng_400` text,
  `mbert_eng_1600` text,
  `mbert_eng_2800` text,
  `mbert_mul_400` text,
  `mbert_mul_1600` text,
  `mbert_mul_2800` text,
  `xlmr_eng_400` text,
  `xlmr_eng_1600` text,
  `xlmr_eng_2800` text,
  `xlmr_mul_400` text,
  `xlmr_mul_1600` text,
  `xlmr_mul_2800` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14099 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- -------------------
-- Validation on datasets
-- -------------------

CREATE TABLE `similarity_st_XLMR` (
  `id` int NOT NULL,
  `translate_chn` decimal(10,5) DEFAULT NULL,
  `translate_my` decimal(10,5) DEFAULT NULL,
  `translate_tm` decimal(10,5) DEFAULT NULL,
  `cm_en_chn` decimal(10,5) DEFAULT NULL,
  `cm_en_my` decimal(10,5) DEFAULT NULL,
  `cm_en_tm` decimal(10,5) DEFAULT NULL,
  `cm_chn_en` decimal(10,5) DEFAULT NULL,
  `cm_chn_my` decimal(10,5) DEFAULT NULL,
  `cm_chn_tm` decimal(10,5) DEFAULT NULL,
  `cm_my_en` decimal(10,5) DEFAULT NULL,
  `cm_my_chn` decimal(10,5) DEFAULT NULL,
  `cm_my_tm` decimal(10,5) DEFAULT NULL,
  `cm_tm_en` decimal(10,5) DEFAULT NULL,
  `cm_tm_chn` decimal(10,5) DEFAULT NULL,
  `cm_tm_my` decimal(10,5) DEFAULT NULL,
  `cw_en_chn` decimal(10,5) DEFAULT NULL,
  `cw_en_my` decimal(10,5) DEFAULT NULL,
  `cw_en_tm` decimal(10,5) DEFAULT NULL,
  `cw_chn_en` decimal(10,5) DEFAULT NULL,
  `cw_chn_my` decimal(10,5) DEFAULT NULL,
  `cw_chn_tm` decimal(10,5) DEFAULT NULL,
  `cw_my_en` decimal(10,5) DEFAULT NULL,
  `cw_my_chn` decimal(10,5) DEFAULT NULL,
  `cw_my_tm` decimal(10,5) DEFAULT NULL,
  `cw_tm_en` decimal(10,5) DEFAULT NULL,
  `cw_tm_chn` decimal(10,5) DEFAULT NULL,
  `cw_tm_my` decimal(10,5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `similarity_st_mBERT` (
  `id` int NOT NULL,
  `translate_chn` decimal(10,5) DEFAULT NULL,
  `translate_my` decimal(10,5) DEFAULT NULL,
  `translate_tm` decimal(10,5) DEFAULT NULL,
  `cm_en_chn` decimal(10,5) DEFAULT NULL,
  `cm_en_my` decimal(10,5) DEFAULT NULL,
  `cm_en_tm` decimal(10,5) DEFAULT NULL,
  `cm_chn_en` decimal(10,5) DEFAULT NULL,
  `cm_chn_my` decimal(10,5) DEFAULT NULL,
  `cm_chn_tm` decimal(10,5) DEFAULT NULL,
  `cm_my_en` decimal(10,5) DEFAULT NULL,
  `cm_my_chn` decimal(10,5) DEFAULT NULL,
  `cm_my_tm` decimal(10,5) DEFAULT NULL,
  `cm_tm_en` decimal(10,5) DEFAULT NULL,
  `cm_tm_chn` decimal(10,5) DEFAULT NULL,
  `cm_tm_my` decimal(10,5) DEFAULT NULL,
  `cw_en_chn` decimal(10,5) DEFAULT NULL,
  `cw_en_my` decimal(10,5) DEFAULT NULL,
  `cw_en_tm` decimal(10,5) DEFAULT NULL,
  `cw_chn_en` decimal(10,5) DEFAULT NULL,
  `cw_chn_my` decimal(10,5) DEFAULT NULL,
  `cw_chn_tm` decimal(10,5) DEFAULT NULL,
  `cw_my_en` decimal(10,5) DEFAULT NULL,
  `cw_my_chn` decimal(10,5) DEFAULT NULL,
  `cw_my_tm` decimal(10,5) DEFAULT NULL,
  `cw_tm_en` decimal(10,5) DEFAULT NULL,
  `cw_tm_chn` decimal(10,5) DEFAULT NULL,
  `cw_tm_my` decimal(10,5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `similarity_st` (
  `id` int NOT NULL,
  `translate_chn` decimal(10,5) DEFAULT NULL,
  `translate_my` decimal(10,5) DEFAULT NULL,
  `translate_tm` decimal(10,5) DEFAULT NULL,
  `cm_en_chn` decimal(10,5) DEFAULT NULL,
  `cm_en_my` decimal(10,5) DEFAULT NULL,
  `cm_en_tm` decimal(10,5) DEFAULT NULL,
  `cm_chn_en` decimal(10,5) DEFAULT NULL,
  `cm_chn_my` decimal(10,5) DEFAULT NULL,
  `cm_chn_tm` decimal(10,5) DEFAULT NULL,
  `cm_my_en` decimal(10,5) DEFAULT NULL,
  `cm_my_chn` decimal(10,5) DEFAULT NULL,
  `cm_my_tm` decimal(10,5) DEFAULT NULL,
  `cm_tm_en` decimal(10,5) DEFAULT NULL,
  `cm_tm_chn` decimal(10,5) DEFAULT NULL,
  `cm_tm_my` decimal(10,5) DEFAULT NULL,
  `cw_en_chn` decimal(10,5) DEFAULT NULL,
  `cw_en_my` decimal(10,5) DEFAULT NULL,
  `cw_en_tm` decimal(10,5) DEFAULT NULL,
  `cw_chn_en` decimal(10,5) DEFAULT NULL,
  `cw_chn_my` decimal(10,5) DEFAULT NULL,
  `cw_chn_tm` decimal(10,5) DEFAULT NULL,
  `cw_my_en` decimal(10,5) DEFAULT NULL,
  `cw_my_chn` decimal(10,5) DEFAULT NULL,
  `cw_my_tm` decimal(10,5) DEFAULT NULL,
  `cw_tm_en` decimal(10,5) DEFAULT NULL,
  `cw_tm_chn` decimal(10,5) DEFAULT NULL,
  `cw_tm_my` decimal(10,5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------
-- Fine-tuning preparation - Resampling
-- ----------------------

CREATE TABLE `Resample_synth_text` (
  `id` int NOT NULL AUTO_INCREMENT,
  `lang_type` text,
  `ori_text` text,
  `mul_text` text,
  `lang_col` text,
  `label` text,
  `plabel` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57601 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- ----------------------
-- Model fine-tuning result
-- ----------------------
CREATE TABLE `model_training` (
  `model_name` varchar(255) NOT NULL,
  `epoch` int NOT NULL,
  `elapsed` double DEFAULT NULL,
  `training_loss` double DEFAULT NULL,
  `training_accuracy` double DEFAULT NULL,
  `val_loss` double DEFAULT NULL,
  `val_accuracy` double DEFAULT NULL,
  PRIMARY KEY (`model_name`,`epoch`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- ----------------------
-- Model Evaluation - Result (Deprecated)
-- ----------------------
CREATE TABLE `eva_eng_text` (
  `id` int NOT NULL AUTO_INCREMENT,
  `clean_text` text,
  `label` text,
  `pseudo_label` text,
  `mbert_eng_400` text,
  `mbert_eng_1600` text,
  `mbert_eng_2800` text,
  `mbert_mul_400` text,
  `mbert_mul_1600` text,
  `mbert_mul_2800` text,
  `xlmr_eng_400` text,
  `xlmr_eng_1600` text,
  `xlmr_eng_2800` text,
  `xlmr_mul_400` text,
  `xlmr_mul_1600` text,
  `xlmr_mul_2800` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3361 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `eva_mul_text` (
  `id` int NOT NULL AUTO_INCREMENT,
  `clean_text` text,
  `label` text,
  `pseudo_label` text,
  `mbert_eng_400` text,
  `mbert_eng_1600` text,
  `mbert_eng_2800` text,
  `mbert_mul_400` text,
  `mbert_mul_1600` text,
  `mbert_mul_2800` text,
  `xlmr_eng_400` text,
  `xlmr_eng_1600` text,
  `xlmr_eng_2800` text,
  `xlmr_mul_400` text,
  `xlmr_mul_1600` text,
  `xlmr_mul_2800` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3361 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- ----------------------
-- Model Evaluation - Result
-- ----------------------

CREATE TABLE `EvaText` (
  `id` int NOT NULL AUTO_INCREMENT,
  `thetext` text,
  `label` text,
  `dstype` text,
  `labeltype` text,
  `GPT_LBL_XMLB` text,
  `GPT_PLBL_XMLB` text,
  `GPT_SLBL_XMLB` text,
  `GPT_LBL_MBERT` text,
  `GPT_PLBL_MBERT` text,
  `GPT_SLBL_MBERT` text,
  `SYN_LBL_XMLB` text,
  `SYN_PLBL_XMLB` text,
  `SYN_SLBL_XMLB` text,
  `SYN_LBL_MBERT` text,
  `SYN_PLBL_MBERT` text,
  `SYN_SLBL_MBERT` text,
  `SYN_LBL_XMLB_E` text,
  `SYN_PLBL_XMLB_E` text,
  `SYN_SLBL_XMLB_E` text,
  `SYN_LBL_MBERT_E` text,
  `SYN_PLBL_MBERT_E` text,
  `SYN_SLBL_MBERTE` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17482 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `evaTweets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `topic_id` int DEFAULT NULL,
  `tweet` text,
  `clean_text` text,
  `In_English` text,
  `pseudo_label` text,
  `label` text,
  `GPT_LBL_XMLB` text,
  `GPT_PLBL_XMLB` text,
  `GPT_SLBL_XMLB` text,
  `GPT_LBL_MBERT` text,
  `GPT_PLBL_MBERT` text,
  `GPT_SLBL_MBERT` text,
  `SYN_LBL_XMLB` text,
  `SYN_PLBL_XMLB` text,
  `SYN_SLBL_XMLB` text,
  `SYN_LBL_MBERT` text,
  `SYN_PLBL_MBERT` text,
  `SYN_SLBL_MBERT` text,
  `SYN_LBL_XMLB_E` text,
  `SYN_PLBL_XMLB_E` text,
  `SYN_SLBL_XMLB_E` text,
  `SYN_LBL_MBERT_E` text,
  `SYN_PLBL_MBERT_E` text,
  `SYN_SLBL_MBERTE` text,
  `agreement_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16384 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ------------------
-- Evaluation analysis
-- ------------------

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `selectedtweets` AS
select `t`.`id` AS `id`,`t`.`tweet` AS `tweet`,`t`.`clean_text` AS `clean_text`,`t`.`pseudo_label` AS `pseudo_label`,`t`.`mbert_eng_400` AS `mbert_eng_400`,`t`.`mbert_eng_1600` AS `mbert_eng_1600`,`t`.`mbert_eng_2800` AS `mbert_eng_2800`,`t`.`mbert_mul_400` AS `mbert_mul_400`,`t`.`mbert_mul_1600` AS `mbert_mul_1600`,`t`.`mbert_mul_2800` AS `mbert_mul_2800`,`t`.`xlmr_eng_400` AS `xlmr_eng_400`,`t`.`xlmr_eng_1600` AS `xlmr_eng_1600`,`t`.`xlmr_eng_2800` AS `xlmr_eng_2800`,`t`.`xlmr_mul_400` AS `xlmr_mul_400`,`t`.`xlmr_mul_1600` AS `xlmr_mul_1600`,`t`.`xlmr_mul_2800` AS `xlmr_mul_2800` from (`tweets` `t` join (select min(`tweets`.`id`) AS `id`,`tweets`.`tweet` AS `tweet` from `tweets` group by `tweets`.`tweet`) `s` on((`t`.`id` = `s`.`id`)));


