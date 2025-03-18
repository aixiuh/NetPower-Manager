#!/usr/bin/env python
# -*- coding: utf-8 -*-

from netpower import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
