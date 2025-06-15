This is the project for developing a classification model to classify a text into emotion class.

The structure of the coding is shown as below:

Common: Library (Folder: commons)


Part 1a: Process of the synthetic dataset (Folder: Proc_Synthetic_Dataset)
-----------------------------------------------------------
- Step1_InsertDataInoDB.py
- Step2_CleanTheTweets.py
- Step3_Translate.py
- Step4_CodeMixed.py
- Step5_CodeSwitched.py

Part 1b: (Fodler: Proc_EmotionTexT_ChatGPT_Dataset)
-----------------------------------------------------------
- Step1_InsertData.py
- Step2_PseudoLabel.py

Part 2: Process of the scrapping data from X platform (Folder: Proc_ScrapX)
-----------------------------------------------------------
- Step1_Scrap_X_topic.py
- Step2_Scrap_X_tweets.py
- Step3_Tweets_PseudoLabel.py

Part 3: Process of Prepare ChatGPT dataset (Folder: Proc_Pretrained_Model_ChatGPTDS)
-----------------------------------------------------------
Steps:
Step1_Prepare_Training_DS.py
Step2_Prepare_DataFrame.py
Step3_Prepare_DataFrame_slbl.py

Part 4: Process of the model developing (Folder: Proc_Pretrained_Model)
-----------------------------------------------------------
* Library
- PTM_Lib.py
- Variable.py

* Prepare the training dataset (Set 1)
- Prepare1_Load_Data_label.py
- Prepare1_Load_Data_plabel.py
- Prepare1_Load_Data_samelabel.py

- Prepare1_OverView_Dataset_lbl.py
- Prepare1_OverView_Dataset_plbl.py
- Prepare1_OverView_Dataset_slbl.py

- Prepare2_Re-Sampling_dataset_lbl.py
- Prepare2_Re-Sampling_dataset_plbl.py
- Prepare2_Re-Sampling_dataset_slbl.py

- Prepare3a_Prepare_Training_dataset_lbl.py
- Prepare3a_Prepare_Training_dataset_plbl.py
- Prepare3a_Prepare_Training_dataset_slbl.py

- Prepare3b_OverView_Training_dataset.py
- Prepare3b_OverView_Training_dataset_SLBL.py

* Identifying the best learning rate
- Preproc_Training_FB_XLM-R_ori_batch.py
- Preproc_Training_mBERT_ori_batch.py

* Tuning process
- TrainingProc_FB_XLM-R_gpt_lbl_batch_Create.py
- TrainingProc_FB_XLM-R_gpt_plbl_batch_Create.py
- TrainingProc_FB_XLM-R_gpt_slbl_batch_Create.py
- TrainingProc_FB_XLM-R_ori_lbl_batch_Create.py
- TrainingProc_FB_XLM-R_ori_plbl_batch_Create.py
- TrainingProc_FB_XLM-R_ori_slbl_batch_Create.py

- TrainingProc_mBERT_gpt_lbl_batch_Create.py
- TrainingProc_mBERT_gpt_plbl_batch_Create.py
- TrainingProc_mBERT_gpt_slbl_batch_Create.py
- TrainingProc_mBERT_ori_lbl_batch_Create.py
- TrainingProc_mBERT_ori_plbl_batch_Create.py
- TrainingProc_mBERT_ori_slbl_batch_Create.py

Part 5: Performance - overview (Folder: Proc_Model_performance_overview)
-----------------------------------------------------------
* Lib
- Model_Var.py

* Training
- TrainingProcess_bar_phrase2.py

Part 6: Validation (Folder: Proc_Analysis_phrase2)
-----------------------------------------------------------
* Lib
- Analysis_Lib.py

* Prepare the evaluation dataset from testing dataset
- Step1_LoadTheTrainingData.py

* Perform prediction
- Step2_PredictByEachModelsEvaText.py
- Step2_PredictByEachModelsTweets.py

* Perform validation
- Step3_Proc_Performance_EvaText.py
- Step3_Proc_Performance_TweetText.py

* Perform checking agreement
- Step4_Proc_Agreement_EvaText.py
- Step4_Proc_Agreement_EvaTweets.py


For Dataset structure:
Database to use: MySQL8.2.1

Database create tables script
.\SQLScript_Create\Create_script.sql

Database connection:
Modify the script ./commons/mysql/mysqlHelper.py
Change the info below:

def get_mysql_conn():
    mydb = mysql.connector.connect(
        host="<Your database host>",
        user="<Your user name>",
        password="<Your password>",
        database="<Your schema name>"
    )
    return mydb
