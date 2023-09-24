import os
import yaml
import json
import glob
import shutil
def create_nav_structure(file_paths):
    nav_structure = []
    file_paths.sort()  # Sort file paths for consistent structure

    for file_path in file_paths:
        components = file_path.split('/')
        current_level = nav_structure

        for i, component in enumerate(components):
            if i == len(components) - 1:
                # Add the file if it's the last component of the file path
                current_level.append(file_path)
            else:
                # If it's a directory, add the directory and descend to the next level
                found = False
                for item in current_level:
                    if isinstance(item, dict) and component in item:
                        current_level = item[component]
                        found = True
                        break

                if not found:
                    # If the directory hasn't been added yet, add it
                    new_directory = {component: []}
                    current_level.append(new_directory)
                    current_level = new_directory[component]

    return nav_structure
def Update_posts_index():
    path = "/Users/hg/DEV/Web/hg-project-bootstrap/public/md"
    naviList = []

    # Get all files with the .md extension in the specified path
    md_files = glob.glob(os.path.join(path, "**/*.md"), recursive=True)

    # Sort the files by their creation time
    sorted_files = sorted(md_files, key=lambda x: os.path.getctime(x), reverse=True)

    # Add the relative paths of the sorted files to naviList
    for file_path in sorted_files:
        relative_path = file_path.split("public/")[-1]
        naviList.append(relative_path)

    
    return naviList
def read_yaml_file(file_path):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data

def main():
    ## 최근 생성 시간을 앞에서 부터 정렬해서 삽입된리스트
    file_paths = Update_posts_index()

    nav_structure = create_nav_structure(file_paths)


    ## 폴더 이름 을 대문자로 변경
    nav_structure = [{'MD': nav_structure[0]['md']}]
    # print(nav_structure)

    p = f'/Users/hg/DEV/Web/hg-project-bootstrap/src/assets/mkdocs_posts_nav.json'
    nav_yaml = yaml.dump({'nav': nav_structure}, allow_unicode=True, sort_keys=False)
    with open(f'{p}', 'w') as json_file:
        json_file.write(json.dumps(nav_structure[0], indent=4, ensure_ascii=False,))

    with open('/Users/hg/DEV/Web/hg-project-bootstrap/src/assets/mkdocs_posts_nav.yml', 'w', encoding='utf-8') as file:
        file.write(nav_yaml)
    print(f"nav_structure saved : {p}")




    ## gpt downloaded from web , copy to project directory that contains the markdwnwn files
    temppath ="/Users/hg/Downloads"
    tagetpath ="/Users/hg/DEV/Web/hg-project-bootstrap/public/md"
    # uploadpath1 ="Usage"
    uploadpath2 ="Post"
    uploadpath3 ="Gpt"

    copy_file(temppath, f"{tagetpath}/{uploadpath3}")



    return nav_structure
    # data = read_yaml_file('/Users/hg/DEV/Web/hg-project-bootstrap/public/md/mkdocs_posts_nav_pp.yml')
    # 
# 경로1 에 있는 .md 파일을 경로2 에 저장
def copy_file(path1, path2):
    files = os.listdir(path1)
    files = [f for f in files if f.endswith('.md')]
    for f in files:
        src = os.path.join(path1, f)
        dst = os.path.join(path2, f.replace(" ", "-"))
        print(f)
        shutil.copy(src, dst)

main()