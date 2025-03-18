#!/usr/bin/env python
# -*- coding: utf-8 -*-

def register_helpers(app):
    """注册模板辅助函数"""
    
    @app.template_global()
    def enumerate(iterable, start=0):
        """为Jinja2模板提供enumerate功能"""
        return list(zip(range(start, len(iterable) + start), iterable))
