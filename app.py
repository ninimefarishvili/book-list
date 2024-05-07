from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

books = [
    {"book_id":1, "title": "Sherlock Holmes", "author": "Arthur Conan Doyle", "year": 1892},
    {"book_id":2, "title": "Moonlocket", "author": "Peter Bunzl", "year": 2017},
    {"book_id":3, "title": "Cogheart", "author": "Peter Bunzl", "year": 2016}
]



@app.route('/')
def home():
    return render_template('index.html', books=books)


@app.route("/book/<int:book_id>")
def book(book_id):
    # Assuming books is a list of dictionaries containing book information
    return render_template("book.html", book_id=book_id, books=books)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        new_book = {
            "book_id": len(books) + 1,
            "title": request.form["title"],
            "author": request.form["author"],
            "year": request.form["year"]
        }
        books.append(new_book)
        return redirect(url_for("home"))

    return render_template("add_book.html")



if __name__ == '__main__':
    app.run(debug=True)
