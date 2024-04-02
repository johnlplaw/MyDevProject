import commons.webscrapping.scrapping as sc
import commons.mysql.mysqlHelper as sqlHelper
import mysql.connector

search_list = [
#'pakatanharapan_',
# 'perikatan_n',
# 'anwaribrahim',
# 'MuhyiddinYassin',
#'PMX',
#'MalaysiaMADANI',
#'KerajaanPerpaduan',
#'EkonomiMADANI'
# '@PNRasmiMY',
# '@Bnrasmi'
# '@DrZahidHamidi',
# '@Hajijinoor',
# '@partiwarisan'
# '@mohdshafieapdal',
# '@PBMRasmi',
# '@partimuda',
#'@SyedSaddiq'
# '@Anifah_myg',
# '@PSB_Digital',
# '@umnoonline'
    #,

#
# '@DrZahidHamidi',
# '@MCAHQ',
# '@weekasiongmp',
# '@MIC_Malaysia',
# '@OnlineMIC',
# '@TSVigneswaranSA',
# '@tsjosephkurup',
# '@SyedSeri',
# '@DatukLoga'
    #,
# '@PartiCintaMy',
# '@PPBMofficial',
# '@MuhyiddinYassin',
# '@PASPusat',
# '@abdulhadiawang',
# '@RakyatParti',
# '@JeffreyKitingan',
# '@yongtl',
# '@KEADILAN',
# '@anwaribrahim',
# '@dapmalaysia',
# '@guanenglim',
# '@anthonyloke',
# '@PartiAmanah',
# '@MSabuOfficial',
# '@UPKOMalaysia',
# '@EwonBenedick',
# '@simkuihian',
# '@tiongkingsing',
# '@Hajijinoor',
# '@pbssab',
# '@pbs_sabah',
# '@mpkotamarudu',
# '@JeffreyKitingan',
# '@yongtl',
# '@PejuangRasmi',
# '@MukhrizOfficial',
# '@berjasamalaysia',
# '@Zamani_BERJASA',
# '@iman4uofficial',
# '@Sedar_official',
# '@partiwarisan',
# '@mohdshafieapdal',
# '@PBMRasmi',
# '@partimuda',
# '@SyedSaddiq',
# '@Partirakyatmsia'
    # ,
# '@partisosialis',
# '@MawanADUN47',
# '@PSB_Digital',
# '@Anifah_myg',
# '@liewyunfah',
# '@BumiParti',
# '@PartiUtama'
    'Malaysia'
]

language_list = [
'en',
#'ta' #,
'id',
'zh-cn',
'zh-tw'
]

from_date = '2024-01-01'
to_date = '2024-02-29'

def execute(search_txt):

    topic_urls = sc.main_scrap_topic(search_txt)
    print(str(len(topic_urls)) + " topic retrieved")

    try:
        conn = sqlHelper.get_mysql_conn()
        mycursor = conn.cursor()
        sql = ("INSERT tweets_topic (search_txt, url) values (%s, %s)")

        for topic_url in topic_urls:
            val = (search_txt, topic_url)
            mycursor.execute(sql, val)
        conn.commit()

    except mysql.connector.Error as error:
        print("Failed to insert record to database: {}".format(error))
    finally:
        if conn.is_connected():
            mycursor.close()
            conn.close()
            print("MySQL connection is closed")


for searchItem in search_list:
    for lang in language_list:
        search_Txt = "lang:" + lang + " " + "since:" + from_date + " " + "until:" + to_date + " "+ searchItem
        print(search_Txt)
        execute(search_Txt)

# search_text = "lang:en since:2024-01-01 until:2024-02-29 pakatanharapan_"
# execute(search_text)
