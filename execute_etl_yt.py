import time
from datetime import datetime
from src.extract_transform_yt import last_n_video_channel
from src.load_yt_csv_json import jsonlist_to_dataframe, save_to_csv, save_to_json
from src.load_yt_mongo import jsonlist_to_mongodb

current_datetime = datetime.now()

#extract data from Youtube API
t1=time.time()
channelid="UCYk4LJI0Pr6RBDWowMm-KUw"    #ID for Deddy Corbuzier Channel
howmanyvideo=49                         #Extract last 49 videos
jsonlist = last_n_video_channel(howmanyvideo,channelid)

#import to mongodb
t2=time.time()
url = <MongoDB connect URL>              #URL censored
jsonlist_to_mongodb(jsonlist,url,"channelvideo","DeddyCorbuzier") #import to "channelvideo" db and "DeddyCorbuzier" collection

#make dataframe
t3=time.time()
df = jsonlist_to_dataframe(jsonlist)

#save to csv
t4=time.time()
save_to_csv(df,"DeddyVideo.csv")

#save to jason file
t5=time.time()
save_to_json(df,"DeddyVideo.json")

#write the time log
t6=time.time()
file = open("time_log.txt","a")
file.write(f"{current_datetime}\n")
file.write(f"extract data time = {t2 - t1}\n")
file.write(f"import to mongodb = {t3 - t2}\n")
file.write(f"make data frame = {t4 - t3}\n")
file.write(f"save to csv time = {t5 - t4}\n")
file.write(f"save to json time = {t6 - t5}\n")
file.write(f"total time = {t6 - t1}\n\n")
file.close()
