import os
import glob

#ファイル名に含まれる変更したい単語と変更後の単語
before_word = ""
after_word = ""

files = []

#カレントディレクトリのファイル数を取得(index.pyは除くものとして-1にする)
DIR = './'
DIR_LENGTG = sum(os.path.isfile(os.path.join(DIR, name)) for name in os.listdir(DIR)) -1

print(DIR_LENGTG)

#カレントディレクトリに含まれるファイルを取得するq
for i in range(DIR_LENGTG):
   files.append(glob.glob('*'+str(i).zfill(2) + before_word +'*'))

print(files)

def flatten_2d(data):
    for block in data:
        for elem in block:
            yield elem

files = list(flatten_2d(files))

for before_file_name in files:
    after_file_name = before_file_name.replace(before_word,after_word)
    os.rename(before_file_name,after_file_name)