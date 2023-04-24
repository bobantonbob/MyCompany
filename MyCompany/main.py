from flask import Flask, render_template

# from  flask import Flask, render_template
# from providers.sqlite_provider import SQLieProvider
from  services.deps_service import DepsService
from services.news_service import NewsService


app = Flask(__name__)
app.config["SECRET_KEY"] = "21232f297a57a5a743894a0e4a801fc3"
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template("home/index.html", contex={
        "page_title" : "Головна сторінка"
    })


@app.route("/about")
def about():
    return render_template("home/about.html", contex={
        "page_title" : "Про все Це..."
    })


@app.route("/news")
def news():
    return render_template("news/index.html", contex={
        "page_title" : "Що є нового"
    })


@app.route("/deps")
def deps():
    return render_template("deps/index.html", contex={
        "page_title" : "Департамент"
    })


@app.route("/contacts")
def contacts():
    return render_template("contacts/index.html", contex={
        "page_title" : "Телефони"
    })






if __name__ == "__main__":
    # app.run(debug=True)





    test_news_service = NewsService()
    test_news_list = test_news_service.get_all_news()
    for news in test_news_list:
        print(f'{news.id} - {news.name} - {news.description}')

    #
    # test_deps_service = DepsService()
    # test_deps_list = test_deps_service.get_all_departments()
    # for dep in test_deps_list:
    #     print(f'{dep.id} - {dep.name}')

    # test_news_service = NewsService()
    # print(test_news_service.get_all_news())




