from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4]

@app.get('/contact', response_class=HTMLResponse)
def get_html_contact_page():
    return """<!DOCTYPE html>
        <html lang="en">
        <head><meta charset='utf-8'>
            <title>Contact us</title>
        </head>
        <body style="background: #f0e6d7;">
            <div class="container" >
                <h1 align=center style="color:#ff9a0c; font-family:'Times New Roman', Times, serif;">Welcome to the jungle</h1>
                <h2>Contact Us</h2>
                <p>Email: JRQ@example.com, Phone number: +91 9999999999, Bangalore</p>
            <div/>
        </body>
    """