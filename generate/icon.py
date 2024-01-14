import os
import json

def list_files(startpath, basepath, prefix):
    ddata = {}
    for root, dire,files in os.walk(startpath):
        for file in files:
            if file != '.DS_Store':
                full_path = os.path.join(root, file)
                filename = os.path.splitext(file)[0]
                relative_path = os.path.relpath(full_path, basepath)
                relative_path_with_prefix = prefix + relative_path
                ddata[filename] = relative_path_with_prefix
    print(ddata)
    return ddata

def add_to_iconlist(data_, iconlist_):
    data_['iconlist'] = iconlist_

if __name__ == '__main__':
    directory_path = '/Users/hg/PROJECT/WebDocuments/public/icon'  # 여기에 디렉토리 경로를 입력하세요.
    output_json_file = '/Users/hg/PROJECT/WebDocuments/public/icon/icon.json'  # 저장할 JSON 파일의 이름을 여기에 입력하세요.
    prefix_ = 'https://raw.githubusercontent.com/d10000usd/WebDocuments/main/'  # 파일 경로에 추가할 접두사를 지정하세요.

    base_path = '/Users/hg/PROJECT/WebDocuments/'
    data = list_files(directory_path, base_path, prefix_)

    # 아래에서 "iconlist" : [ ,] 딕셔너리에 추가하는 함수를 사용합니다.
    iconlist = list(data.values())  # 모든 파일 경로를 포함하는 리스트를 가져옵니다.

    add_to_iconlist(data, iconlist)

    with open(output_json_file, 'w',encoding='utf-8') as f:
        json.dump(data, f, indent=4)
