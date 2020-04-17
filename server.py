#!/usr/bin/env python
# -*- coding: utf-8 -*-

from web import app

if __name__ == '__main__':
    app.run(debug="debug", port=8081, host="127.0.0.1")
