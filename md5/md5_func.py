# coding:utf-8
import hashlib
__auther__:"冬阳"

def str_trans_to_md5(input,output):
    src = input.get(1.0,END).strip().replace("\n","").encode()
    if src:
        try:
            myMd5=hashlib.md5()
            myMd5.update(src)
            myMd5_digest = myMd5.hexdigest()
            output.delete(1.0, END)
            output.insert(1.0,myMd5_digest)
        except:
            output.dellete(1.0, END)
            output.insert(1.0,"字符串转md5失败")
    else:
        print("error")

