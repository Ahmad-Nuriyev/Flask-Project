from flask import url_for, redirect, render_template

from app import app
from extensions import db


@app.route ('/')
def main():
    return render_template ('frontend/templates/detail.html')