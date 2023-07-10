from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def get_blog():
    blog_url = "https://api.npoint.io/51a1d33e06a64627f0ce"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", blog_posts=all_posts)

@app.route('/post/<int:id>')
def get_post(id):
    post_url = "https://api.npoint.io/51a1d33e06a64627f0ce"
    response = requests.get(post_url)
    all_posts = response.json()
    return render_template("post.html", blog_posts=all_posts, num=id)


if __name__ == "__main__":
    app.run(debug=True)