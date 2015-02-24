#!/usr/bin/python
#-*- coding:utf-8 -*-


import webapp
import sys
import random


class aleat(webapp.webApp):
    """Root of a hierarchy of classes implementing web applications

    This class does almost nothing. Usually, new classes will
    inherit from it, and by redefining "parse" and "process" methods
    will implement the logic of a web application in particular.
    """

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        nextPage = str (random.randint (0,10000))
        nextUrl = "http://" + "localhost" + ":" + "1234" +'/aleat/' + nextPage
        htmlBody = '<p>Quieres mas: <a href="' \
            + nextUrl + '">'+ nextPage + "</a></p>"
        return ("HTTP/1.1 200 OK\r\n\r\n", "<html><body><h1>" + htmlBody +"</h1></body></html>")

if __name__ == "__main__":
	testAleat = aleat("localhost", 1234)
