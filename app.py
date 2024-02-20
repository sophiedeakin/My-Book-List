from flask import Flask, render_template, request, redirect,  url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/booklist', methods=['POST'])
def booklist():
        title = request.form['title']
        author = request.form['author']
        comments = request.form['comments']
        status = request.form['status']
        var1 = title
        var2 = author
        var3 = comments
        var4 = status
        return render_template('booklist.html', var1 = var1, var2 = var2, var3 = var3, var4 = var4)

if __name__ == '__main__':
    app.run(debug=True)