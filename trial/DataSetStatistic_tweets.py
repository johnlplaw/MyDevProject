import statistics

import commons.mysql.mysqlHelper as sqlHelper

conn = sqlHelper.get_mysql_conn()

mycursor = conn.cursor()

print("Query data... start")
# sql = "Select length(oritxt), length(cleanedtxt) from mydataset where cleanedtxt is not null and length(cleanedtxt) > 0"
sql = "Select length(tweet), length(clean_text) from tweets where clean_text is not null and length(clean_text) > 0;"

mycursor.execute(sql)
myresult = mycursor.fetchall()

print("Query data... end")

print("Loading data... start")
i = 0
oritxt_length_list = []
cleantxt_length_list = []

for x in myresult:
    oritxt_length_list.append(x[0])
    cleantxt_length_list.append(x[1])

print("Loading data... end")

print(len(oritxt_length_list))
print(len(cleantxt_length_list))

if (conn.is_connected()):
    conn.disconnect()
    conn.close()


# Statistic:
# median
print("Median:")
ori_median = statistics.median(oritxt_length_list)
clean_median = statistics.median(cleantxt_length_list)
print(ori_median)
print(clean_median)

# mode
print("Mode:")
ori_mode = statistics.mode(oritxt_length_list)
clean_mode = statistics.mode(cleantxt_length_list)
print(ori_mode)
print(clean_mode)

# mean
print("Mean:")
ori_mean = statistics.mean(oritxt_length_list)
clean_mean = statistics.mean(cleantxt_length_list)
print(ori_mean)
print(clean_mean)

# min
print("Min:")
ori_min = min(oritxt_length_list)
clean_min = min(cleantxt_length_list)
print(ori_min)
print(clean_min)

# max
print("Max:")
ori_max = max(oritxt_length_list)
clean_max = max(cleantxt_length_list)
print(ori_max)
print(clean_max)

# 1/4
print("quantiles: ")
ori_q = statistics.quantiles(oritxt_length_list, n=4 )
clean_q = statistics.quantiles(cleantxt_length_list, n=4 )
print(ori_q)
print(clean_q)
