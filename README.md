Web Vulnerability Scanner (SQL Injection & XSS)

A simple Python-based web vulnerability scanner that detects common SQL Injection and Cross-Site Scripting (XSS) flaws in web applications. This tool automatically analyzes HTML forms, injects test payloads, and inspects server responses to identify potential security weaknesses.

Features

Automatic HTML form detection

SQL Injection vulnerability scanning

Cross-Site Scripting (XSS) detection

Supports GET and POST methods

Payload-based response analysis

Beginner-friendly security testing tool

How It Works

Fetches the target web page

Extracts all HTML forms

Submits predefined SQL and XSS payloads

Analyzes responses for error messages or reflected scripts

Reports detected vulnerabilities

Requirements

Python 3.7 or higher

requests

beautifulsoup4

lxml

Install dependencies:

pip install requests beautifulsoup4 lxml

Usage
python scanner.py


Example target:

http://testphp.vulnweb.com

Disclaimer

This project is intended strictly for educational purposes and authorized security testing only. Do not use this tool against systems without explicit permission.

Future Enhancements

Login-protected form testing

Multi-page crawling

Stored XSS detection

Automated vulnerability reports

Expanded payload library
