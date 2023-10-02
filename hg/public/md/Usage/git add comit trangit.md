
# ~ Publishing
- ==/Users/hg/WORKSPACE/Gitblog/mkdocs-material/site==
- 안쪽에 있는것 만 push
- mkdocs-material/
- mkdocs gh-deploy --force
- 기존 브랜치와 충돌이 날때는 pull 하지 말고    
- 브랜치를 웹에서 삭제하고, 새로 추가 하는것이 빠르고 확실한 방법  
- 웹에서 브랜치 리스트를 클릭하고 나면 브랜치 폴더들을 삭제 할 수 있음    
<div class="input">  

</div>
# Deploy  
mkdocs build  
mkdocs gh-deploy --force  
mkdocs serve
<div class="input">  

</div>


# Local monitoring
npm start 
mkdocs serve --watch-theme  
<div class="input">  
gpt-Bokeh Trendline Plotting.md  <br>
gpt-Stock DIV & DPS.md  <br>
gpt-JSON Data Sorting.md  <br>
gpt-주식 PBR 공식 요약.md  <br>
gpt-Sort Coin Data LH (1).md  <br>
gpt-실시간 차트 구현 (Vue.js).md  <br>
gpt-Sort Coin Data LH.md  <br><br>
gpt-Bokeh 차트 Dash에 삽입.md  <br>
gpt-Vue.js Image Display Issue..md  <br>
gpt-Vue 3 리소스 가져오기.md  <br>
gpt-code-server Extension Installation.md  <br>
gpt-ChatGPT.md  <br>
</div>
# Git 
  ```
  if [ -d .git ]; then  
    rm -rf .git  
  fi

  git push origin gh-pages  
  error: src refspec gh-pages does not match any  
  error: failed to push some refs to 
  'https://github.com/d10000usd/d10000usd.github.io.git'  

  rm -rf .git
  re-init
  ```

```
git init  
Initialized empty 
Git repository in /Users/hg/WORKSPACE/Gitblog/mkdocs-material/src/.git/   
```

```
git add .  
git remote add origin https://github.com/d10000usd/d10000usd.github.io.git  
git branch -m gh-pages  
git commit -m "commit gh"  
```
```
git remote -v  
- git remote -v  
- origin  https://github.com/d10000usd/d10000usd.github.io.git (fetch)  
- origin  https://github.com/d10000usd/d10000usd.github.io.git (push)  
```

<div class="input">  

</div>