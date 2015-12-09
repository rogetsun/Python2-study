# coding:utf-8
__author__ = 'uv2sun'

import httplib, urllib, json


def post(url, data, host="127.0.0.1", port='5000', form_json="json"):
    """
    发起post请求
        :param port: 端口
        :param host: 服务器地址
        :param url: url路径
        :param data: post数据
    """
    if url:
        h1 = httplib.HTTPConnection(host, port)
        endata = form_json == "json" and json.JSONEncoder().encode(data) or urllib.urlencode(data)
        json_content_type = "application/json"
        form_content_type = "application/x-www-form-urlencoded;charset=UTF-8"
        headers = {"Content-type": form_json == "json" and json_content_type or form_content_type,
                   'X-Requested-With': 'XMLHttpRequest'}
        h1.request(method="POST", url=url, body=endata, headers=headers)
        resp = h1.getresponse()
        res = resp.read()
        h1.close()
        return res
    else:
        return False
