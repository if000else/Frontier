import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print(111)
        u = self.get_argument('user')
        e = self.get_argument('email')
        p = self.get_argument('psd')
        if u == 'alex' and p == '123' and e == 'alex@126.com':
            self.write("Ok")
        else:
            self.write("Gun")

    def post(self, *args, **kwargs):
        u = self.get_arguments('gender')
        # e = self.get_argument('email')
        # p = self.get_argument('psd')
        file_meta = self.request.files['file']
        print(file_meta)
        for meta in file_meta:
            filename = meta['filename']
            with open(filename, 'wb') as f:
                f.write(meta['body'])
        print(u)
        self.write("OK")


app = tornado.web.Application([
    (r'/index', MainHandler),
])
if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
