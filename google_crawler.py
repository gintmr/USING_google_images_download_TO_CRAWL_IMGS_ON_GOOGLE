from google_images_download import google_images_download   #importing the library
import os
response = google_images_download.googleimagesdownload()   #class instantiation

noun_list = [    
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog",
    "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite",
    "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle",
    "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich",
    "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa",
    "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote",
    "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book",
    "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
    ]

import os
import re

def rename(path, noun):
    i = 1  # 初始化序号
    for filename in os.listdir(path):
        # 使用正则表达式匹配文件名前面的数字标号
        match = re.match(r'^(\d+)\.', filename)
        if match:
            number = match.group(1)  # 提取数字标号
            file_extension = os.path.splitext(filename)[1]  # 获取文件扩展名
            new_filename = f'{noun}_{number}{file_extension}'  # 构造新的文件名
            try:
                os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
                print(f"Renamed '{filename}' to '{new_filename}'")  # 打印重命名成功的信息
            except OSError as e:
                print(f"Error renaming '{filename}' to '{new_filename}': {e}")  # 打印错误信息
            i += 1  # 增加序号以便下一次重命名

# 使用示例
# rename('/path/to/your/directory', 'your_noun')


for noun in noun_list:
    arguments = {"keywords":f"{noun}","limit":20,"print_urls":True} 
    #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    
    print(paths)   #printing absolute paths of the downloaded images
    
    PATH = './downloads/'+ noun + '/'  # 指定文件夹路径
    rename(PATH, noun)
    