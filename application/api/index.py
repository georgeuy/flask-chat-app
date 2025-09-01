from flask import render_template, request, flash, session, url_for, redirect

from . import api


@api.route('/chat')
def chat():
    return render_template('chat.html')


@api.route('/', methods=['GET','POST'])
def index():

    if request.method == 'POST':

        nickname = request.form.get('nickname')
        room = request.form.get('room', 'default')

        if not nickname:
            flash('Nickname es requerido', 'danger')
            return render_template('index.html')
        
        session['nickname'] = nickname
        session['room'] = room

        return redirect(url_for('.chat'))

        
    return render_template('index.html')


