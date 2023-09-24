# Markdown 컨텐츠
markdown_content = """
```mermaid
graph LR

A[소스 코드] --> B[빌드]
B --> C[단위 테스트]
C --> D[정적 코드 분석]
D --> E[패키징]
E --> F[통합 테스트]
F --> G[배포]
G --> H[운영 환경]
H --> I[테스트 환경]

```

위의 다이어그램은 일반적인 CI/CD 프로세스를 나타내고 있습니다. 각각의 단계는 다음과 같은 의미를 가집니다:

* **소스 코드**: 개발자가 작성한 소스 코드입니다.
* **빌드**: 소스 코드를 컴파일하고 실행 가능한 아티팩트를 생성하는 단계입니다.
* **단위 테스트**: 단위별로 작성된 코드의 동작을 검증하는 단계입니다.
* **정적 코드 분석**: 소스 코드의 품질을 검사하고 잠재적인 버그나 취약점을 찾는 단계입니다.
* **패키징**: 빌드된 아티팩트를 패키지로 묶는 단계입니다.
* **통합 테스트**: 다양한 컴포넌트 또는 서비스 간의 통합을 검증하는 단계입니다.
* **배포**: 패키지된 아티팩트를 운영 환경에 배포하는 단계입니다.
* **운영 환경**: 실제 사용자가 접근하는 환경입니다.
* **테스트 환경**: 개발자가 테스트하는 환경으로, 운영 환경과 유사한 설정을 가지고 있습니다.

"""

# Mermaid 코드
mermaid_code_0 = """
graph TD
Compute(fa:fa-cloud Computing) -->|150a 50mm| Shutdown
Compute -->|150a 50mm| Shunt

Shutdown[Shutdown] -->|150a 50mm| BusPositive[Cloud Bus +]

Shunt -->|150a 50mm| BusNegative[Cloud Bus -]

BusPositive -->|40a| Firewall[Firewall]
BusPositive -->|?a| Legacy{Legacy Network}

BusNegative -->|40a| Firewall

Firewall -->|10a| VM1(VM Instance 1)
Firewall -->|10a| VM2(VM Instance 2)
Firewall -->|1.5a| LoadBalancer -->|1.5a| CDN

CDN -->|1.5a| Firewall

Firewall -->|10a| Database(Database Server)
Firewall -->|10a| Database 

Firewall -->|10a| App1[Application 1]
Firewall -->|10a| App1 

Firewall -->|10a| App2[Application 2]
Firewall -->|10a| App2 

BusNegative -->|?a| Legacy

CloudSolar --> CloudCont[Cloud Controller]
CloudSolar --> CloudCont

CloudCont --> BusNegative
CloudCont --> BusPositive

linkStyle 0,1,2,4,5,8,9 stroke-width:2px,fill:none,stroke:red;
linkStyle 3,6,7 stroke-width:2px,fill:none,stroke:black;
linkStyle 10 stroke-width:2px,fill:none,stroke:red;
linkStyle 11 stroke-width:2px,fill:none,stroke:black;
linkStyle 12 stroke-width:2px,fill:none,stroke:red;
linkStyle 13 stroke-width:2px,fill:none,stroke:black;
linkStyle 14 stroke-width:2px,fill:none,stroke:red;
linkStyle 15 stroke-width:2px,fill:none,stroke:black;
linkStyle 16 stroke-width:2px,fill:none,stroke:black;
linkStyle 17 stroke-width:2px,fill:none,stroke:red;
linkStyle 18 stroke-width:2px,fill:none,stroke:black;
linkStyle 19 stroke-width:2px,fill:none,stroke:black;
"""

# Mermaid 코드
mermaid_code_1 = """
classDiagram
로직C1 <|-- AveryLongClass : Cool
로직C3 *-- 로직C4
로직C5 o-- 로직C6
로직C7 .. 로직C8
로직C9 --> C2 : Hook msg?
로직C9 --* C3
로직C9 --|> 로직C7
로직C7 : equals()
로직C7 : Object[] elementData
로직C1 : size()
로직C1 : [...activeTabCoins.value]
로직C1 : indexOf(data.code)
로직C8 <--> C2: Task Time Check
"""
# Mermaid 코드
mermaid_code_2 = """
sequenceDiagram
    participant AppLayer as Application Layer
    participant SaaS as Software as a Service
    participant PaaS as Platform as a Service
    participant AIModel as AI Model
    participant IaaS as Infrastructure as a Service
    
    AppLayer->>SaaS: User initiates message exchange
    SaaS->>AppLayer: SaaS application processes user request
    SaaS->>AIModel: SaaS leverages an AI model for analysis
    SaaS->>PaaS: SaaS application deployment and scaling
    PaaS->>AppLayer: Platform provides tools for application development
    PaaS->>AIModel: AI models integrated into applications on the platform
    IaaS->>PaaS: Infrastructure resources provided for platform operation
    IaaS->>SaaS: Cloud resources utilized for SaaS services
    SaaS-->>AppLayer: SaaS application responds to the user
    AIModel-->>SaaS: Results of AI analysis returned to SaaS
"""
mermaid_code_3 = """
sequenceDiagram
    participant web as Web Browser
    participant blog as Blog Service
    participant account as Account Service
    participant mail as Mail Service
    participant db as Storage

    Note over web,db: The user must be logged in to submit blog posts
    web->>+account: Logs in using credentials
    account->>db: Query stored accounts
    db->>account: Respond with query result

    alt Credentials not found
        account->>web: Invalid credentials
    else Credentials found
        account->>-web: Successfully logged in

        Note over web,db: When the user is authenticated, they can now submit new posts
        web->>+blog: Submit new post
        blog->>db: Store post data

        par Notifications
            blog--)mail: Send mail to blog subscribers
            blog--)db: Store in-site notifications
        and Response
            blog-->>-web: Successfully posted
        end
    end
"""
# Mermaid 코드
mermaid_code_Saas = """
graph TD
    User[User] -->|Access| SaaS(SaaS Platform)

    SaaS -->|Data Storage| Database[Database]
    SaaS -->|User Authentication| Auth[Authentication Service]
    SaaS -->|Payment Processing| Payment[Payment Gateway]

    SaaS -->|Service Logic| Logic[Application Logic]

    Logic -->|Access Data| Database
    Logic -->|Verify Identity| Auth
    Logic -->|Handle Payments| Payment

    SaaS -->|User Interface| UI[User Interface]

    UI -->|Interact with Logic| Logic
    UI -->|Display Data| Database

    linkStyle 0,1,2,3,4,6 stroke-width:2px,fill:none,stroke:black;
    linkStyle 5 stroke-width:2px,fill:none,stroke:blue;
    linkStyle 7 stroke-width:2px,fill:none,stroke:blue;
    linkStyle 8,9 stroke-width:2px,fill:none,stroke:blue;
"""

# JSON 코드
json_code = """
{
  "compilerOptions": {
    "target": "esnext",
    "module": "esnext",
    "strict": true,
    "jsx": "preserve",
    "moduleResolution": "node",
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "forceConsistentCasingInFileNames": true,
    "useDefineForClassFields": true,
    "sourceMap": true,
    "allowJs": true,
    "baseUrl": "."
  }
}
"""

# HTML 템플릿 생성
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Include the necessary CSS for syntax highlighting (you can choose a different theme if you want) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/styles/default.min.css">
  <!-- Include the Markdown-it and Highlight.js libraries -->
  <script src="https://cdn.jsdelivr.net/npm/markdown-it@13.0.1/dist/markdown-it.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/highlight.min.js"></script>
  <!-- <script>hljs.initHighlightingOnLoad();</script>
  Deprecated as of 10.6.0. initHighlightingOnLoad() is deprecated.  Use highlightAll() instead. -->
  <script>hljs.highlightAll();</script>
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.4.0/dist/mermaid.esm.min.mjs';

    mermaid.initialize({{
      startOnLoad: true,
    }});
  </script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/markdown-it/13.0.1/markdown-it.min.js" integrity="sha512-SYfDUYPg5xspsG6OOpXU366G8SZsdHOhqk/icdrYJ2E/WKZxPxze7d2HD3AyXpT7U22PZ5y74xRpqZ6A2bJ+kQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

<script>
  window.onload = function() {{
    var md = window.markdownit();
    var markdownElements = document.getElementsByClassName('markdown');
  
    Array.from(markdownElements).forEach(function(element) {{
      var content = element.innerHTML;
      element.innerHTML = md.render(content);
    }});
  }}
</script>

</head>
<body>
  <div class="markdown">
    {markdown_content}
  </div>
  
  <div class="mermaid">
    {mermaid_code_0}
  </div>
    <div class="mermaid">
    {mermaid_code_1}
  </div>
      <div class="mermaid">
    {mermaid_code_2}
  </div>
    <div class="mermaid">
    {mermaid_code_3}
  </div>
    <div class="mermaid">
    {mermaid_code_Saas}
  </div>
    <div class="mermaid">
    {mermaid_code_1}
  </div>
  <pre><code class="language-json">
    {json_code}
  </code></pre>
</body>
</html>
"""

# HTML 파일 생성
with open("/Users/hg/DEV/Web/hg-project-bootstrap/public/diagram/flowchart.html", "w") as html_file:
    html_file.write(html_template)

print("HTML 파일이 생성되었습니다.")

# 파이썬에서 
# 중괄호는 이중으로 넣어야 html 로 됨 {{ }}
# 변수는 { json_code }