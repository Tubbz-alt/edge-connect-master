from PIL import Image
import cv2
import numpy as np
import os
def concat(small,img,size,path):
    img[:256,-size:]=small
    cv2.imwrite(path,img)
with open('./ww_data/youku_test_list.txt') as f:
    b = f.readlines()

base_path = './result/edgeT_in_F'
for i in b:
    org_path = i.strip()
    if org_path.split('/')[-1].split('.')[0]=='100':
        continue
    small_path = org_path.split('/')[-1].split('.')[0]+"_gt_res.png"
    org = cv2.imread(org_path)
    # org.flags['WRITEABLE'] = True
    org_ = org.copy()
    small_img = cv2.imread(os.path.join(base_path,small_path))
    concat(small_img,org,256,'./concat_result/'+small_path)
    print(i)

