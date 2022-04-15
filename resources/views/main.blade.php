<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/css/main.css">
    <title> Individuele opdracht IPMEDT5 </title>
</head>
<body>  
    <form method="GET" action="/display">
        <h3>Display</h3>
        <p> Write 4 characters to display on the Arduino </p>
        <textarea name="digits" maxlength="4"></textarea><br>
        <h3>LDR</h3>
        <img src="/img/ldrgraph.png" alt="LDR graph" /><br>
        <button type="submit">Display input and/or refresh graph</button> 
    </form>
    
</body>
</html>