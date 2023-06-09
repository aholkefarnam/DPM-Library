from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "aj-dpm"

friends_dict = [
    {"title": "The Hobbit", 
     "author": "J. R. R. Tolkien", 
     "pages": "310", 
     "type": "nonfiction",
     "details": "own",
     "acquire": "purchase"}
]

# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def not_found_error(error):
    return render_template("500.html"), 500

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", friends=friends_dict
    )

@app.route('/about', methods=["GET","POST"])
def about():
    return render_template(
        "about.html", pageTitle="About", friends=friends_dict
    )



@app.route('/add', methods=["GET", "POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        title = form["title"]
        author = form["author"]
        pages = form["pages"]
        type = form["type"]
        details = form.getlist("details")  # this is a Python list
        acquire = form["acquire"]

        print(title)
        print(author)
        print(pages)
        print(type)
        print(details)
        print(acquire)

        details_string = ", ".join(details)  # make the Python list into a string

        friend_dict = {
            "title": title,
            "author": author,
            "pages": pages,
            "type": type,
            "details": details_string,
            "acquire": acquire
        }

        print(friend_dict)
        friends_dict.append(
            friend_dict
        )  # append this dictionary entry to the larger friends dictionary
        print(friends_dict)

        flash('The book ' + title + ' has been added. ', 'success')

        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
