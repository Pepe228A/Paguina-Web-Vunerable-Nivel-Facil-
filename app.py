from flask import Flask, request, session, redirect, render_template
# … resto del código …

@app.route('/', methods=['GET','POST'])
def index():
    error = None

    # Login
    if 'user' not in session:
        if request.method == 'POST':
            u = request.form['username']
            p = request.form['password']
            sql = f"SELECT * FROM users WHERE username='{u}' AND password='{p}'"
            if len(query(sql)) == 1:
                session['user'] = u
                return redirect('/')
            error = 'Credenciales inválidas'
        return render_template('index.html', user=None, error=error)

    # Comentarios
    if request.method == 'POST':
        with open(COMMENTS, 'a') as f:
            f.write(f"<p><b>{session['user']}:</b> {request.form['comment']}</p>\n")

    stored = open(COMMENTS).read() if os.path.exists(COMMENTS) else ''
    return render_template('index.html', user=session['user'], stored=stored)
