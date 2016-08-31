#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid
import messagehandler

from tornado.options import define, options

define("port", default=10000, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
        	(r"/", MainHandler),
            (r"/game", GameSocketHandler),
        ]
        settings = dict(
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
        )
        super(Application, self).__init__(handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class GameSocketHandler(tornado.websocket.WebSocketHandler):
    waiters = set()
    cache = []
    cache_size = 200

    def get_compression_options(self):
        # Non-None enables compression with default options.
        return {}

    def open(self):
        GameSocketHandler.waiters.add(self)

    def on_close(self):
        GameSocketHandler.waiters.remove(self)

    def on_message(self, message):
        try:
            parsed = tornado.escape.json_decode(message)
            pass
        except Exception, e:
            self.close();
            pass
        logging.info("got message %r", message)
        messagehandler.dealmessge(self,parsed)
        


def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()