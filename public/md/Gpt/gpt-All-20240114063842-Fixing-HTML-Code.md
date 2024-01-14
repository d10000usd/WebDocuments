# **<span style="font-size: 35px; font-style: italic;">Fixing HTML Code</span>**

>Fixing HTML Code  
2024년 01월 14일 06시 38분  
SaaS  
#article #code #keyword  
[Github edited](https://github.com/d10000usd/WebDocuments/tree/main/public/md/Gpt "깃허브")
Here’s a brief explanation read more
## Description  

<body class="body-full"><div class="c-custom-card"> <div class="spacing mb-2">  



###  <img src="https://raw.githubusercontent.com/d10000usd/WebDocuments/main/public/icon/Team/40-goal.svg" width="50" height="50" />   

  It looks like there are a couple of issues in your code. Let me help you fix them:

1. The variable `title0` is being overwritten in each iteration of the loop. Instead, you should use the current iteration's title.
2. You are using the same variable `title0` both outside and inside the loop. It's better to use a different variable inside the loop to avoid confusion.

Here's the corrected code:

```python
def htmlSett(apiData):
    listofnews = """"""
    for index, value in enumerate(apiData['newscontents']):
        title = value['title']
        listofnewsTp = f"""
            <li class="cc_text_item">
                <a href="https://n.news.naver.com/article/023/0003806119?type=editd&amp;cds=news_edit"
                   class="cc_text_a _MM_VISITED_COLOR" data-aid="0003806119" data-oid="023" data-clk="wkeynews">{title}</a>
            </li>
        """
        listofnews += listofnewsTp

    # Rest of your code...

# Call the function with your API data
# htmlSett(yourApiData)
```

This should fix the issues in your code. Make sure to replace `yourApiData` with the actual data you are working with.


  </div></div></div>

  <div style="background-color: grey; height: 15px;"></div>

  