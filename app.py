from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {"id": 1, "title": "First Post", "content": "This is the first blog post."},
    {"id": 2, "title": "Second Post", "content": "This is the second blog post."},
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        return "Post not found", 404
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)