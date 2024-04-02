import commons.lang.GenCodeMixedSwitched as cm
import commons.mysql.mysqlHelper as sqlHelper
from datetime import datetime
from tqdm import tqdm
import time

# Initial Coding - start
#########################
txt_Eng = "im sitting here in the belmont library listening to hold on tight by electric light orchestra feeling a bit of discontent"
txt_Man = "我坐在贝尔蒙特图书馆听着电灯管弦乐队的演奏，感觉有点不满"
txt_ms = "Saya duduk di sini di perpustakaan belmont sambil mendengar orkestra lampu elektrik berpegangan erat dengan rasa tidak puas hati"
txt_ta = "நான் இங்கே பெல்மாண்ட் நூலகத்தில் அமர்ந்து மின் விளக்கு இசைக்குழுவை இறுகப் பற்றிக் கேட்டுக் கொண்டிருக்கிறேன்."
#
# translate_chn = translate(txt, source_lang="en", target_lang="zh-CN")
# translate_my = translate(txt, source_lang="en", target_lang="ms")
# translate_tm = translate(txt, source_lang="en", target_lang="ta")
#
# translate_chn = translate_chn.results[0].paraphrase
# translate_my = translate_my.results[0].paraphrase
# translate_tm = translate_tm.results[0].paraphrase
#
#
# print(translate_chn)
# print(translate_my)
# print(translate_tm)

print(cm.gen_code_mixed(txt_Eng, 0.8, cm.Eng_code, cm.Man_code))
print(cm.gen_code_mixed(txt_Eng, 0.8, cm.Eng_code, cm.Ms_code))
print(cm.gen_code_mixed(txt_Eng, 0.8, cm.Eng_code, cm.Ta_code))
#
# print(gen_code_mixed(txt_Man, 0.8, Man_code, Eng_code ))
# print(gen_code_mixed(txt_Man, 0.8, Man_code, Ms_code ))
# print(gen_code_mixed(txt_Man, 0.8, Man_code, Ta_code ))
#
# print(gen_code_mixed(txt_ms, 0.8, Ms_code, Eng_code ))
# print(gen_code_mixed(txt_ms, 0.8, Ms_code, Man_code ))
# print(gen_code_mixed(txt_ms, 0.8, Ms_code, Ta_code ))
#
# print(gen_code_mixed(txt_ta, 0.8, Ta_code, Eng_code ))
# print(gen_code_mixed(txt_ta, 0.8, Ta_code, Man_code ))
# print(gen_code_mixed(txt_ta, 0.8, Ta_code, Ms_code ))
# Initial Coding - end
#########################
