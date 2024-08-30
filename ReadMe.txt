This is the project for developing a classification model to classify a text into emotion class.

The structure of the coding is shown as below:

Common: Library (Folder: commons)


Part 1: Process of the synthetic dataset (Folder: Proc_Synthetic_Dataset)
-----------------------------------------------------------
- Step1_InsertDataInoDB.py
- Step2_CleanTheTweets.py
- Step3_Translate.py
- Step4_CodeMixed.py
- Step5_CodeSwitched.py

Part 2: Process of the scrapping data from X platform (Folder: Proc_ScrapX)
-----------------------------------------------------------
- Step1_Scrap_X_topic.py
- Step2_Scrap_X_tweets.py
- Step3_Tweets_PseudoLabel.py

Part 3: Process of the model developing (Folder: Proc_Pretrained_Model)
-----------------------------------------------------------
* Library
- PTM_Lib.py
- Variable.py

* Prepare the training dataset (Set 1)
- Prepare1_Load_Data.py
- Prepare2_re-Sampling_dataset.py
- Prepare3a_Prepare_Training_dataset.py
- Prepare3b_OverView_Training_dataset.py

* Prepare the training dataset (Set 2)
- Step1_InsertData
- Step2_PseudoLabel


* Identifying the best learning rate
- Preproc_Training_FB_XLM-R_ori_batch.py
- Preproc_Training_mBERT_ori_batch.py

* Tuning process
- TrainingProc_FB_XLM-R_ori_batch_Create.py
- TrainingProc_mBERT_ori_batch_Create.py

* Validation
Val1_ Prepare_Test_dataset.py
Val2_Prepare_Data_Table.py
Val3_Eval_proc.py

Part 4: Validation (Folder: Proc_Analysis)
-----------------------------------------------------------
