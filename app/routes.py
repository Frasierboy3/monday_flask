from app import app
from flask import render_template

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/fav')
def fav():
    artists = [{
        'name': "bbno$",
        'picture': "https://e.snmc.io/i/600/w/3f61176578332d8398a837b945cd618b/9854632/bbno-mathematics-Cover-Art.jpg"
        },
        {
        'name': "Amine",
        'picture': "https://i.scdn.co/image/c1ec6da0896ff7efe6fd63ea6894c0bf44dbfaf6"
        },
        {
        'name':"Tyler Childers",
        'picture': "https://i.guim.co.uk/img/media/02053144d2ebfbff0a45c635323cd02b2852ee83/0_84_3838_2303/master/3838.jpg?width=1020&quality=45&dpr=2&s=none"
        },
        {
        'name':"Tyler,The Creator",
        'picture':"https://image-cdn.hypb.st/https%3A%2F%2Fhypebeast.com%2Fimage%2F2022%2F10%2FTyler-the-Creator-Joins-Season-6-of-%E2%80%98Big-Mouth-0.jpg?fit=max&cbr=1&q=90&w=1125&h=750"
        },
        {
        'name':"Jack Harlow",
        'picture':"https://pbs.twimg.com/media/FPrttgEVEAASpXo?format=jpg&name=small"
        }]
    return render_template('login.html', artists= artists)

