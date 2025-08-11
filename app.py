from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>SUPERTRAM Fatigue Risk Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }
        .container {
            max-width: 700px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
            color: #0078D4;
        }
        form {
            display: grid;
            gap: 12px;
        }
        input[type=number], input[type=submit] {
            padding: 10px;
            font-size: 16px;
            width: 100%;
        }
        input[type=submit] {
            background-color: #0078D4;
            color: white;
            border: none;
            cursor: pointer;
        }
        input[type=submit]:hover {
            background-color: #005fa3;
        }
        .logo {
            text-align: center;
            margin-bottom: 20px;
        }
        .logo img {
            max-width: 180px;
        }
        .readme-link {
            text-align: center;
            margin-top: 30px;
        }
        .readme-link a {
            background-color: #0078D4;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
        }
        .readme-link a:hover {
            background-color: #005fa3;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <img src="https://github.com/abuckley-1/SUPERTRAM-Fatigue-Risk-Calculator/raw/main/Super
