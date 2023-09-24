PROMPT:

<html> <head> <style> body { font-family: open-sans; color: white; margin: 20px; width: 960px; margin: 0 auto; background: black; } a.button1 { display: inline-block; padding:0.35em 1.2em; border:0.1em solid #FFFFFF; margin:0 0.3em 0.3em 0; border-radius:0.12em; box-sizing: border-box; text-decoration:none; font-family:'Roboto',sans-serif; font-weight:300; color:#FFFFFF; text-align:center; transition: all 0.2s; } a.button1:hover{ color:#000000; background-color:#FFFFFF; } @media all and (max-width:30em){ a.button1{ display:block; margin:0.4em auto; } } .bouncy{ animation:bouncy 3s infinite linear; position:relative; } @keyframes bouncy { 0%{top:0em} 40%{top:0em} 43%{top:-0.9em} 46%{top:0em} 48%{top:-0.4em} 50%{top:0em} 100%{top:0em;} } .bullish { background: green; } .bearish { background: red; } table { text-align: center; } form { text-align: center; } h1 { text-align: center; } </style> </head> <body> <h1>Chart Screener</h1> <a class="button1 bouncy" href="{{ url\_for('snapshot\_upbit') }}" target="\_blank" rel="noopener noreferrer">Update upbit-Charts!</a> <table> <tr> <th> symbol </th> <th> U\_pattern\_name </th> <th> signal </th> </tr> {% for stock in stocks %} <!-- <td>{{ stock.split('-')\[1\] }}</td> --> <tr> <td>{{stock}}</td> <td>{{ alldicts\[stock\]\['U\_pattern\_name'\]}}</td> <td>불장불장</td> </tr> {% endfor %} </table> </body> </html> 보기 좋게 css 수정해줘, 문자들은 좌측정렬

RESPONSE:

<html> <head> <style> body { font-family: open-sans; color: white; margin: 20px; width: 960px; margin: 0 auto; background: black; }
```css
        a.button1 {
            display: inline-block;
            padding: 0.35em 1.2em;
            border: 0.1em solid #FFFFFF;
            margin: 0 0.3em 0.3em 0;
            border-radius: 0.12em;
            box-sizing: border-box;
            text-decoration: none;
            font-family: 'Roboto', sans-serif;
            font-weight: 300;
            color: #FFFFFF;
            text-align: center;
            transition: all 0.2s;
        }
        a.button1:hover {
            color: #000000;
            background-color: #FFFFFF;
        }

        @media all and (max-width: 30em) {
            a.button1 {
                display: block;
                margin: 0.4em auto;
            }
        }

        .bouncy {
            animation: bouncy 3s infinite linear;
            position: relative;
        }
        @keyframes bouncy {
            0% {top: 0em}
            40% {top: 0em}
            43% {top: -0.9em}
            46% {top: 0em}
            48% {top: -0.4em}
            50% {top: 0em}
            100% {top: 0em;}
        } 

        .bullish { 
            background: green; 
        }
        .bearish { 
            background: red; 
        }

        table {
            text-align: left;
            margin: 0 auto;
        }

        th, td {
            padding: 10px;
        }

        th {
            background-color: #FFFFFF;
            color: black;
        }

        tr:nth-child(even) {
            background-color: #222222;
        }

        tr:nth-child(odd) {
            background-color: #333333;
        }

        h1 {
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Chart Screener</h1>

    <a class="button1 bouncy" href="{{ url_for('snapshot_upbit') }}" target="_blank" rel="noopener noreferrer">Update upbit-Charts!</a>
   
    <table>
       
        <tr>
            <th>Symbol</th>
            <th>U_pattern_name</th>
            <th>Signal</th>
        </tr>
        
        {% for stock in stocks %}
            <tr>
                <td>{{stock}}</td>
                <td>{{alldicts[stock]['U_pattern_name']}}</td>
                <td>불장불장</td>
            </tr>
        {% endfor %}
    </table>
</body>
```
</html>