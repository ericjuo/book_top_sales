import pandas as pd
import sqlite3
from datetime import date


conn = sqlite3.connect("../../data/03_processed/top_sales_books.db")
stores = ['books', 'kingstone', 'sanmin', 'taaze', 'cite', 'tcsb']
df_list = [pd.read_sql("select name from topsales where store == '%s'" % i, conn) for i in stores]
df_list.insert(0, pd.Series([i for i in range(1, 11)]))
columns = ['TOP', '博客來', '金石堂', '三民書局', '讀冊', '城邦讀書花園', '墊腳石']
df = pd.concat(df_list, axis=1)
df.columns = columns
today = date.today()
if today.month -1 == 0:
    rank_month = 12
    rank_year = today.year -1
else:
    rank_month = today.month -1
    rank_year = today.year

with open("../../README.md", 'w') as f:
    f.write("# 台灣暢銷書排行榜  \n")
    f.write("## %s年%s月排行榜  \n" % (rank_year, rank_month))
    f.write("Updated on %s  \n" % today.strftime("%Y-%m-%d"))
    f.write(df.to_markdown(index=False)+ "  \n")
conn.close()

