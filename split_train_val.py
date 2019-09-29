with open('./ww_data/douyin_list.txt') as f:
    a = f.readlines()
with open('./ww_data/douyin_list_train.txt','w') as f_t:
    for i in range(int(len(a)*0.7)):
        f_t.write(a[i])
with open('./ww_data/douyin_list_val.txt','w') as f_v:
    for i in range(int(len(a)*0.7),len(a)):
        f_v.write(a[i])