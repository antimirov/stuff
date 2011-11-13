#!/usr/bin/env python

import sys
import os
import math

import httplib
import SocketServer
import BaseHTTPServer


SRV = "base.maps.yandex.net"
REQ = "/tiles/%d/?layer=%d&x=%d&y=%d&scale=%d"

KIEV_MIN_X=1254600000
KIEV_MIN_Y=725000000


class Httpd(SocketServer.ThreadingTCPServer):
    allow_reuse_address = 1


class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.0"

    def do_GET(self):
        print "self.path:", self.path
        params = self.path.split("?")
        if len(params) < 2:
            return

        params = params[1]
        for pair in params.split("&"):
            (var, value) = pair.split("=")
            exec("%s=%s" % (var, value))

        scale = z+4

        shift = (1<<(scale+8)) - 1

        xx = KIEV_MIN_X + shift * x
        yy = KIEV_MIN_Y + shift * y
        
        req = REQ % (map, layer, xx, yy, scale)

        conn = httplib.HTTPConnection(SRV)
        conn.request ("GET", req)
        print "req: http://%s%s" % (SRV,req)
        res = conn.getresponse()
        if res.status == 200:
            self.send_response(res.status, res.reason)
            self.send_header("Content-Type", res.getheader("Content-Type") )
            self.end_headers()
            self.wfile.write( res.read() )
        else:
            print "Error response: ", res.status

        conn.close


if __name__ == "__main__":
    server_address = ('127.0.0.1', 8000)
    httpd = Httpd(server_address, Handler)
    httpd.serve_forever()
