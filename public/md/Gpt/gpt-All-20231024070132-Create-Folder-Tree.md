# **<span style="font-size: 35px; font-style: italic;">Create Folder Tree</span>**


- Create Folder Tree  
- 20231024070132  
- gpt  
- #gpt #code #keyword  
- 아래의 Python 코드는 지정된 디렉토리에서 모든 하위 디렉토리와 파일을 읽고, 이를 트리 구조로 정리하여 JSON 파일로 저장하는 예제입니다,코드를 실행하기 전에 `os` 모듈과 `json` 모듈이 설치되어 있는지 확인하시기 바랍니다.

```python
import os
import json

def create_tree(directory):
    tree = {'name': os.path.basename(directory), 'type': 'directory', 'children': []}
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                tree['children'].append(create_tree(item_path))
            else:
                tree['children'].append({'name': item, 'type': 'file'})
    except OSError as e:
        print(f"Error reading {directory}: {e}")
    return tree

def save_to_json(tree, output_file):
    with open(output_file, 'w') as f:
        json.dump(tree, f, indent=4)

if __name__ == '__main__':
    directory_path = '/Users/hg/DEV/web/WebDocuments/public/icon' # 경로를 여기에 입력하세요.
    output_json_file = 'output.json'  # 저장할 JSON 파일 이름을 여기에 입력하세요.

    full_tree = create_tree(directory_path)
    save_to_json(full_tree, output_json_file)
```

이 코드는 지정된 경로의 모든 폴더와 파일을 읽어들여 트리 구조로 정리하고, 최종적으로 JSON 파일로 저장합니다,주어진 경로와 저장할 JSON 파일 이름을 해당 변수에 입력한 후 코드를 실행하시면 됩니다.


###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-37.png" width="50" height="50" /> context 1  



아래의 Python 코드는 주어진 디렉토리의 모든 파일을 읽어들여, 파일 이름과 경로를 포함한 딕셔너리로 구성하고 이를 JSON 파일로 저장하는 예제입니다  
- [Github edited](http://www.github.com "깃허브")
- <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/22-gear assembly.svg" width="100" height="100" />  
**** 


## Description  

아래의 Python 코드는 지정된 디렉토리에서 모든 하위 디렉토리와 파일을 읽고, 이를 트리 구조로 정리하여 JSON 파일로 저장하는 예제입니다. 코드를 실행하기 전에 `os` 모듈과 `json` 모듈이 설치되어 있는지 확인하시기 바랍니다.

```python
import os
import json

def create_tree(directory):
    tree = {'name': os.path.basename(directory), 'type': 'directory', 'children': []}
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                tree['children'].append(create_tree(item_path))
            else:
                tree['children'].append({'name': item, 'type': 'file'})
    except OSError as e:
        print(f"Error reading {directory}: {e}")
    return tree

def save_to_json(tree, output_file):
    with open(output_file, 'w') as f:
        json.dump(tree, f, indent=4)

if __name__ == '__main__':
    directory_path = '/Users/hg/DEV/web/WebDocuments/public/icon' # 경로를 여기에 입력하세요.
    output_json_file = 'output.json'  # 저장할 JSON 파일 이름을 여기에 입력하세요.

    full_tree = create_tree(directory_path)
    save_to_json(full_tree, output_json_file)
```

이 코드는 지정된 경로의 모든 폴더와 파일을 읽어들여 트리 구조로 정리하고, 최종적으로 JSON 파일로 저장합니다. 주어진 경로와 저장할 JSON 파일 이름을 해당 변수에 입력한 후 코드를 실행하시면 됩니다.


###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-37.png" width="50" height="50" /> context 1  



아래의 Python 코드는 주어진 디렉토리의 모든 파일을 읽어들여, 파일 이름과 경로를 포함한 딕셔너리로 구성하고 이를 JSON 파일로 저장하는 예제입니다. 코드를 실행하기 전에 `os` 모듈과 `json` 모듈이 설치되어 있는지 확인하시기 바랍니다.

```python
import os
import json

def list_files(startpath):
    data = {}
    for root, dirs, files in os.walk(startpath):
        for file in files:
            full_path = os.path.join(root, file)
            data[file] = full_path
    return data

if __name__ == '__main__':
    directory_path = '/Users/hg/DEV/web/WebDocuments/public/icon' # 경로를 여기에 입력하세요.
    output_json_file = 'output.json'  # 저장할 JSON 파일 이름을 여기에 입력하세요.

    data = list_files(directory_path)
    with open(output_json_file, 'w') as f:
        json.dump(data, f, indent=4)
```

이 코드는 주어진 경로의 모든 파일을 읽어들여 파일 이름과 해당 파일의 전체 경로를 딕셔너리로 구성하고, 이를 JSON 파일로 저장합니다. 주어진 경로와 저장할 JSON 파일 이름을 해당 변수에 입력한 후 코드를 실행하시면 됩니다.


###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-33.png" width="50" height="50" /> context 3  



아래의 수정된 코드는 주어진 디렉토리의 모든 파일을 읽어들여, 파일 이름(확장자 제외)과 경로를 포함한 딕셔너리로 구성하고 이를 JSON 파일로 저장하는 예제입니다. 코드를 실행하기 전에 `os` 모듈과 `json` 모듈이 설치되어 있는지 확인하시기 바랍니다.

```python
import os
import json

def list_files(startpath):
    data = {}
    for root, dirs, files in os.walk(startpath):
        for file in files:
            full_path = os.path.join(root, file)
            filename = os.path.splitext(file)[0]
            data[filename] = full_path
    return data

if __name__ == '__main__':
    directory_path = '/Users/hg/DEV/web/WebDocuments/public/icon' # 경로를 여기에 입력하세요.
    output_json_file = 'output.json'  # 저장할 JSON 파일 이름을 여기에 입력하세요.

    data = list_files(directory_path)
    with open(output_json_file, 'w') as f:
        json.dump(data, f, indent=4)
```

이 코드는 주어진 경로의 모든 파일을 읽어들여 확장자를 제외한 파일 이름과 해당 파일의 전체 경로를 딕셔너리로 구성하고, 이를 JSON 파일로 저장합니다. 주어진 경로와 저장할 JSON 파일 이름을 해당 변수에 입력한 후 코드를 실행하시면 됩니다.


###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-35.png" width="50" height="50" /> context 5  



수정된 코드는 `.DS_Store` 파일을 저장하지 않도록 하는 기능을 추가한 것입니다. 아래 코드를 사용하여 파일을 읽고 JSON으로 저장할 수 있습니다.

```python
import os
import json

def list_files(startpath):
    data = {}
    for root, dirs, files in os.walk(startpath):
        for file in files:
            if file != '.DS_Store':
                full_path = os.path.join(root, file)
                filename = os.path.splitext(file)[0]
                data[filename] = full_path
    return data

if __name__ == '__main__':
    directory_path = '/Users/hg/DEV/web/WebDocuments/public/icon'  # 경로를 여기에 입력하세요.
    output_json_file = 'output.json'  # 저장할 JSON 파일 이름을 여기에 입력하세요.

    data = list_files(directory_path)
    with open(output_json_file, 'w') as f:
        json.dump(data, f, indent=4)
```

이 코드는 주어진 경로의 모든 파일을 읽어들일 때 `.DS_Store` 파일을 제외하고, 확장자를 제외한 파일 이름과 해당 파일의 전체 경로를 딕셔너리로 구성하며, 이를 JSON 파일로 저장합니다. 주어진 경로와 저장할 JSON 파일 이름을 해당 변수에 입력한 후 코드를 실행하시면 됩니다.


###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-38.png" width="50" height="50" /> context 7  



수정된 코드는 주어진 경로의 각 파일에 대해 절대 경로의 일부를 제거하여 딕셔너리를 생성하고, 이를 JSON 파일로 저장합니다. 아래는 코드 예시입니다.

```python
import os
import json

def list_files(startpath, basepath):
    data = {}
    for root, dirs, files in os.walk(startpath):
        for file in files:
            if file != '.DS_Store':
                full_path = os.path.join(root, file)
                filename = os.path.splitext(file)[0]
                relative_path = os.path.relpath(full_path, basepath)
                data[filename] = relative_path
    return data

if __name__ == '__main__':
    directory_path = '/Users/hg/DEV/web/WebDocuments/public/icon'  # 경로를 여기에 입력하세요.
    output_json_file = 'output.json'  # 저장할 JSON 파일 이름을 여기에 입력하세요.

    base_path = '/Users/hg/DEV/web/WebDocuments/'
    data = list_files(directory_path, base_path)
    with open(output_json_file, 'w') as f:
        json.dump(data, f, indent=4)
```

이 코드는 주어진 경로의 모든 파일을 읽어들일 때 `.DS_Store` 파일을 제외하고, 상대 경로를 확장자를 제외한 파일 이름과 함께 딕셔너리로 구성하며, 이를 JSON 파일로 저장합니다. 주어진 경로와 저장할 JSON 파일 이름을 해당 변수에 입력한 후 코드를 실행하시면 됩니다.


###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-37.png" width="50" height="50" /> context 9  



네, 파이썬의 딕셔너리는 중복된 키를 허용하지 않습니다. 따라서 동일한 키에 대해 덮어쓰게 됩니다. 이를 방지하기 위해서는 다른 방식으로 처리해야 합니다. 예를 들어, 중복된 키에 대해 리스트로 값을 추가할 수 있습니다. 아래는 그 예시입니다.

```python
import os
import json

def list_files(startpath, basepath):
    data = {}
    for root, dirs, files in os.walk(startpath):
        for file in files:
            if file != '.DS_Store':
                full_path = os.path.join(root, file)
                filename = os.path.splitext(file)[0]
                relative_path = os.path.relpath(full_path, basepath)
                if filename in data:
                    if not isinstance(data[filename], list):
                        data[filename] = [data[filename]]
                    data[filename].append(relative_path)
                else:
                    data[filename] = relative_path
    return data

if __name__ == '__main__':
    directory_path = '/Users/hg/DEV/web/WebDocuments/public/icon'  # 경로를 여기에 입력하세요.
    output_json_file = 'output.json'  # 저장할 JSON 파일 이름을 여기에 입력하세요.

    base_path = '/Users/hg/DEV/web/WebDocuments/'
    data = list_files(directory_path, base_path)
    with open(output_json_file, 'w') as f:
        json.dump(data, f, indent=4)
```

이 코드는 중복된 키가 있을 때 해당 키에 대한 값으로 리스트를 사용하여 모든 관련된 값을 저장합니다. 결과적으로 JSON 파일에 중복된 키가 있더라도 모든 값이 보존됩니다. 주어진 경로와 저장할 JSON 파일 이름을 해당 변수에 입력한 후 코드를 실행하시면 됩니다.


###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/space/workspace-vector-free-icon-set-32.png" width="50" height="50" /> context 11  



<div style="background-color: grey; height: 15px;"></div>

