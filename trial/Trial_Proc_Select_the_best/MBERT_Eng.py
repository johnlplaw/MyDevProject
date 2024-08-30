import Lib_Select as lib
from matplotlib import pyplot as plt

model_1 = "mBERT_Eng_1200"
model_1_acc_t, model_1_acc_e = lib.get_model_list("mBERT_English_1200_ori_RO3_Batch_8")

model_2 = "mBERT_Eng_1600"
model_2_acc_t, model_2_acc_e = lib.get_model_list("mBERT_English_1600_ori_RO3_Batch_8")

model_3 = "mBERT_Eng_2000"
model_3_acc_t, model_3_acc_e = lib.get_model_list("mBERT_English_2000_ori_RO3_Batch_8")

model_4 = "mBERT_Eng_2400"
model_4_acc_t, model_4_acc_e = lib.get_model_list("mBERT_English_2400_ori_RO3_Batch_8")

model_5 = "mBERT_Eng_2800"
model_5_acc_t, model_5_acc_e = lib.get_model_list("mBERT_English_2800_ori_RO3_Batch_8")

model_6 = "mBERT_Eng_800"
model_6_acc_t, model_6_acc_e = lib.get_model_list("mBERT_English_800_ori_RO3_Batch_8")

model_7 = "mBERT_Eng_400"
model_7_acc_t, model_7_acc_e = lib.get_model_list("mBERT_English_400_ori_RO3_Batch_8")


ages_x = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

plt.subplot(2, 1, 1)
plt.plot(ages_x, model_7_acc_t, marker='.', linewidth='1', label='n=400')
plt.plot(ages_x, model_6_acc_t, marker='.', linewidth='1', label='n=800')
plt.plot(ages_x, model_1_acc_t, marker='.', linewidth='1', label='n=1200')
plt.plot(ages_x, model_2_acc_t, marker='.', linewidth='1', label='n=1600')
plt.plot(ages_x, model_3_acc_t, marker='.', linewidth='1', label='n=2000')
plt.plot(ages_x, model_4_acc_t, marker='.', linewidth='1', label='n=2400')
plt.plot(ages_x, model_5_acc_t, marker='.', linewidth='1', label='n=2800')

plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title('Accuracy (Training) by Epoch (Tuned by English)')
#plt.grid(True)
plt.legend()
plt.tight_layout()
#plt.show()

plt.subplot(2, 1, 2)
plt.plot(ages_x, model_7_acc_e, marker='.', linewidth='1', label='n=400')
plt.plot(ages_x, model_6_acc_e, marker='.', linewidth='1', label='n=800')
plt.plot(ages_x, model_1_acc_e, marker='.', linewidth='1', label='n=1200')
plt.plot(ages_x, model_2_acc_e, marker='.', linewidth='1', label='n=1600')
plt.plot(ages_x, model_3_acc_e, marker='.', linewidth='1', label='n=2000')
plt.plot(ages_x, model_4_acc_e, marker='.', linewidth='1', label='n=2400')
plt.plot(ages_x, model_5_acc_e, marker='.', linewidth='1', label='n=2800')
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title('Accuracy (Evaluation) by Epoch (Tuned by Multilingual)')

#plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('mBERT-Eng-e.png')
plt.show()
