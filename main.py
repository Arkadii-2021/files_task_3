import os
with open('final.txt', 'w') as f:
    for file_txt in os.listdir("."):
        list_files_txt = []
        if file_txt.endswith('.txt'):
            list_files_txt.append(file_txt)
        my_dict = {}
        my_list = []
        for txt_ in list_files_txt:
            open_files = open(txt_, encoding='utf-8')
            list_strings = open_files.readlines()
            my_list.extend([len(list_strings)])
            my_dict[txt_] = list_strings
            for key_strings_files, volumes_strings_files in my_dict.items():
                f.write(key_strings_files)
                f.write('\n')
                f.write(str(my_list[0]))
                f.write('\n')
                for vol_str_files in volumes_strings_files:
                    f.write(vol_str_files.strip())
                    f.write('\n')
