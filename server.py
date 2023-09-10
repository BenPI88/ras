from flask import Flask, render_template
import os

app = Flask("RAS Server")

@app.route('/')
def index():
  os.system("bash shellcode.sh")
  return "Executing shellcode.sh"

app.run(host="0.0.0.0")
