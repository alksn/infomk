

from bottle import Bottle, run, template, request, route, post, default_app, static_file
from bottle import error

from infomk import infomk
from infomk2 import infomk2
from mrzdoc import mrzdoc


path_page = './index.tpl'
# '/home/alksn/mysite/page.tpl'
path_src = 'dist'
# '/home/alksn/mysite/dist/'



@route('/dist/:path#.+#')      # regular expression between ## (old syntax)
def static(path):
    return static_file(path, root=path_src)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/')
def hello():
    return template(path_page, stat={})


if __name__ == "__main__":


    application = default_app()
    application.mount('/infomk', infomk)
    application.mount('/infomk2', infomk2)
    application.mount('/mrz', mrzdoc)
    application.run(host='localhost', port=8080, debug=True)
#run(host='localhost', port=8080, debug=True)
