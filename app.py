import webapp2
import handlers

routes = [
    ('/', handlers.MainPage),
	('/search', handlers.Search),

]
webapp = webapp2.WSGIApplication(routes, debug=True)


