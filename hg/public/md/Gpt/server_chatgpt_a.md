# Chatbot UI History  

  


# Vue3 Express 서버 사용법
## 개요
이 문서는 Vue3와 Express로 서버를 구성하는 방법을 안내합니다.

## 설치 방법
1. Vue3 프로젝트 생성
    - Vue CLI를 이용하여 새로운 프로젝트를 생성합니다.
    ```
    $ vue create my-project
    ```
2. Express 설치
    - npm을 이용하여 Express를 설치합니다.
    ```
    $ npm install express
    ```

## 서버 코드 작성
1. Express 서버 생성
    - Express 서버를 생성하고 리스닝합니다.
    ```javascript
    const express = require('express');
    const app = express();

    // 서버 리스닝
    app.listen(3000, () => {
        console.log('Express server is listening on port 3000');
    });
    ```
2. 정적 파일 제공
    - Vue3에서 빌드한 정적 파일의 경로를 Express에 등록하여 클라이언트에게 제공합니다.
    ```javascript
    const path = require('path');
    const publicPath = path.join(__dirname, 'my-project/dist');

    app.use(express.static(publicPath));
    ```
3. API 작성
    - Express에서 API를 작성할 수 있습니다.
    ```javascript
    app.get('/api/users', (req, res) => {
       // 사용자 정보 반환
       res.json({ name: 'John', age: 30 });
    });
    ```

## 예시
### 라우팅
- Express에서 라우팅을 처리할 때는 HTTP 요청 종류(GET, POST, PUT, DELETE)와 URI가 필요합니다.
```javascript
// GET 요청
app.get('/api/users', (req, res) => {
    // 사용자 정보 반환
    res.json({ name: 'John', age: 30 });
});

// POST 요청
app.post('/api/users', (req, res) => {
   // form 데이터 받아서 처리
   const user = { name: req.body.name, age: req.body.age };
   res.json(user);
});

// PUT 요청
app.put('/api/users/:userId', (req, res) => {
   // 사용자 정보 수정
   const userId = req.params.userId;
   const newName = req.body.name;
   const newAge = req.body.age;
   
   // DB에서 사용자 정보 수정
   // ...

   res.json({ message: '사용자 정보가 수정되었습니다.' });
});

// DELETE 요청
app.delete('/api/users/:userId', (req, res) => {
   // 사용자 정보 삭제
   const userId = req.params.userId;

   // DB에서 사용자 정보 삭제
   // ...

   res.json({ message: '사용자 정보가 삭제되었습니다.' });
});
```

### 데이터베이스 연동
- 데이터베이스 연동을 위해서는 해당 데이터베이스에 맞는 Node.js 모듈을 설치해야 합니다.
- 예를 들어, MySQL 데이터베이스에 연동하고자 할 경우 다음과 같은 방법을 사용할 수 있습니다.
```javascript
const mysql = require('mysql');

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'mydb',
    port: '3306'
});

// MySQL 연결
connection.connect((err) => {
    if (err) throw err;
    console.log('MySQL 연결 성공');
});

// SQL 쿼리 실행
connection.query('SELECT * FROM users', (error, results, fields) => {
    if (error) throw error;
    console.log('유저 정보:', results);
});

// MySQL 연결 종료
connection.end();
```  
남은 부분 다써줘  
### 에러 처리
- 서버 개발에서 에러 처리는 매우 중요합니다. Express에서는 다음과 같은 방법으로 에러를 처리할 수 있습니다.
```javascript
// 에러 처리 미들웨어 등록
app.use((error, req, res, next) => {
    console.error(error.stack);
    // 클라이언트에게 에러 메시지 전달
    res.status(500).send('Something broke!');
});
```

### 모듈화
- 서버 코드를 작성할 때, 코드의 가독성과 유지보수성을 높이기 위해서 모듈화를 적극적으로 활용해야 합니다.
- 디렉토리 구조 예시
```
my-project/
├─ dist/
│  ├─ index.html
│  └─ js/
│      └─ app.js
├─ server/
│  ├─ api/
│  │  └─ users.js
│  ├─ dao/
│  │  └─ users-dao.js
│  ├── middleware/
│  │  └─ auth.js
│  ├── routes/
│  │  └─ index.js
│  ├── services/
│  │  └─ users-service.js
│  └─ index.js
├─ src/
│  ├─ assets/
│  ├─ components/
│  ├─ router/
│  ├─ store/
│  └─ views/
├─ package.json
└─ vue.config.js
```

### 보안
- 웹 개발에서 보안은 매우 중요합니다. Express에서는 다음과 같은 방법으로 보안을 처리할 수 있습니다.
    - 기본적으로 모든 API에 대해 CORS를 설정하여 외부에서의 요청을 차단합니다.
    ```javascript
    const cors = require('cors');

    app.use(cors());
    ```
    - SSL을 사용하여 데이터를 암호화합니다.
    ```javascript
    const https = require('https');
    const fs = require('fs');

    const options = {
        key: fs.readFileSync('./key.pem'),
        cert: fs.readFileSync('./cert.pem')
    };

    https.createServer(options, app);
    ```

## 참고 문서
- [Vue CLI 공식 문서](https://cli.vuejs.org/)
- [Express 공식 문서](https://expressjs.com/)
- [MySQL 모듈](https://github.com/mysqljs/mysql)
- [Node.js 보안 가이드](https://nodejs.org/en/docs/guides/security-best-practices/)  
