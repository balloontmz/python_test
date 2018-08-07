import os
# from the review area
# need to completed

def find_in_dir(abs_path, cur_dir, input_str, find_dic):
    temp_path = os.path.join(abs_path,cur_dir,'.')
    dir_list = os.listdir(temp_path)
    for filestr in dir_list:
        fpath = os.path.join(abs_path,cur_dir,filestr)
        if os.path.isfile(fpath):
            if input_str in filestr:
                find_dic[cur_dir] = filestr
        else:
            temp_dir = os.path.join(cur_dir,filestr)
            find_in_dir(abs_path, temp_dir, input_str, find_dic)

if __name__ == '__main__':
    input_str = input("请输入您要查找的文件：")
    abs_path = os.path.abspath('.')
    find_dic = {}
    find_in_dir(abs_path, '', input_str, find_dic)
    if len(find_dic) == 0:
        print("未找到您要搜索的文件！")
    else:
        print("搜索到%d个文件：\n"%len(find_dic))
        for x in find_dic.keys():
            print(x,find_dic[x])