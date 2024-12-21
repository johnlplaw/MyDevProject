from sentence_transformers import SentenceTransformer, util

import ValidationFunction as commf
import ValidationObject as commO
from bert_score import score

# Step 1: load all dataset
oritxt_list = commf.get_Syn_Dataset()

# Step 2: Prepare the model
# Load a multilingual model
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Step 3: Similarity
for txtObj in oritxt_list:
    print(txtObj.cleanedtxt)
    for field in commO.field_list:
        #print(txtObj.get_txt(field))
        #similarity = commf.getSimilarityBySentenceTransformer(model, txtObj.cleanedtxt, txtObj.translate_chn)
        #print(str(similarity))
        # commf.insertUpdateSimilarity("similarity_st", txtObj.id, field, similarity)

        P, R, F1 = commf.getSimilarityByBertScore(score, txtObj.cleanedtxt, txtObj.translate_chn)
        commf.insertUpdateSimilarity("similarity_bs", txtObj.id, field, f" {P.mean():.4f}", f" {R.mean():.4f}", f" {F1.mean():.4f}")
        # print(f"BERTScore Precision: {P.mean():.4f}")
        # print(f"BERTScore Recall: {R.mean():.4f}")
        # print(f"BERTScore F1: {F1.mean():.4f}")
