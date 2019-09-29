edge_checkpoints：在优酷数据集上训练edge model  
end_eheck: 在抖音数据集上进行训练  
orig_check:原始下载的模型  
youku_check: 在原始的edge model基础上，直接训练npainting model    
youku_check_random_mask：采用随机产生mask的方式进行训练    
result: 一些测试结果    


# Train  
## 先读readme.md   
## 产生mask  
    执行create_mask，随机产生mask。在'ww_data/mask_list'中写Mask路径  
## 设置 edge_connect中的is_crop，是否进行裁剪    
    裁剪方式，采用随机在四个角进行裁剪，大小为256    

#Test  
在main.py mode==2中设置路径  

concat.py将截取的图像与原图进行拼接  