import os
from PIL import Image

dirname_read="D:/csm/"
dirname_write="D:/B"
names=os.listdir(dirname_read)
count=0
for name in names:
    img=Image.open(dirname_read+name)
    name=name.split(".")
    print(name[-1])
    if name[-1] == "png":
        name[-1] = "jpg"
        name = str.join(".", name)
        r,g,b,a=img.split()
        img=Image.merge("RGB",(r,g,b))
        to_save_path = dirname_write + name
        img.save(to_save_path)
        count+=1
        print(count)
        print(to_save_path, "------conut：",count)
    else:
        continue
