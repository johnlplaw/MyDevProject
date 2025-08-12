import ot
from sentence_transformers import SentenceTransformer, util
import torch
import ValidationFunction as commf
import ValidationObject as commO
from bert_score import score
import numpy as np

# Define the table for the storage
table_str = "similarity_emd_XLMR"

model = SentenceTransformer('FacebookAI/xlm-roberta-base')

def execution():
    """
    Perform the main task for Earth Mover's Distance (EMD)
    This is to find out whether the embedding of the pre-trained model will impact the distance.
    :return: nothing
    """
    # Step 1: load all data
    oritxt_list = commf.get_Syn_Dataset(table_str, "LIMIT 0, 100")

    # Step 2: Similarity
    for txtObj in oritxt_list:
        emdList = []
        embedding_1 = model.encode(txtObj.cleanedtxt)
        for field in commO.field_list:
            embedding_2 = model.encode(txtObj.get_txt(field))

            # Convert to NumPy arrays if needed
            # (when they are not coming from the GPU)
            embedding1 = np.array(embedding_1).reshape(1, -1)
            embedding2 = np.array(embedding_2).reshape(1, -1)

            # Example for Euclidean distance calculation
            #euclidean_distance = np.linalg.norm(embedding1 - embedding2)

            a = np.ones(len(embedding1)) / len(embedding1)
            b = np.ones(len(embedding2)) / len(embedding2)
            M = ot.dist(embedding1.reshape(1, -1), embedding2.reshape(1, -1), metric="euclidean")
            emd_distance = ot.emd2(a, b, M)
            emdList.append(str(round(emd_distance, 4)))

            # print("Euclidean Distance:", euclidean_distance)
            # print("EMD Distance (feature-level):", emd_distance)

        # Insert into the database
        commf.insertUpdateSimilarityType1(table_str, txtObj.id, commO.field_list, emdList)

#execution()

count = 0;
while count < 100:
    execution()
    count = count + 1
    print(count)

