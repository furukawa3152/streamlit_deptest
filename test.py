import pandas as pd
# data_file = pd.read_excel("登録テスト.xlsx")
# arg_df = data_file[["ID", "登録日"]].values
# for row in arg_df:
#     ID = str(int(row[0]))
#     ymd = row[1]
#     alt_y = "5" + str("{0:02d}".format(ymd.year - 2018))
#     alt_m = str("{0:02d}".format(ymd.month))
#     alt_d = str("{0:02d}".format(ymd.day))
#     alt_ymd = alt_y + alt_m + alt_d
#     print(ID, alt_ymd)
#     if ID == "":
#         break
#     #10 5030601
#     #15 5030701

# 薬剤リスト取得(dict)
import pandas as pd
hoge_data = pd.read_excel("登録テスト.xlsx")
hoge_df = hoge_data[["ID", "登録日"]].values
hoge_dic = {}
for drug in hoge_df:
    key = drug[0]
    value = drug[1]
    hoge_dic[key] = value
print(hoge_dic)
#{10: Timestamp('2021-06-01 00:00:00'), 15: Timestamp('2021-07-01 00:00:00')}
