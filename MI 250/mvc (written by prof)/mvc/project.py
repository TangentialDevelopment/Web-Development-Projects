from .mvccgi import BaseController, BaseModel


class MyController(BaseController):
    model = BaseModel("session.json", ["user", "logged_in"])

    def home_POST(self, params):
       
        if 'myname' in params:
            name = params['myname'].value
            self.model.updateOrAdd({"user":name},{"logged_in":True})

        elif 'logout' in params:
            self.model.update({"logged_in":True},{"logged_in":False})

        return self.home_GET(params)


    def home_GET(self, params):
        result = self.getStandardHeader()

        logged_in = self.model.find({"logged_in":True})

        if len(logged_in) > 0:
            name = logged_in[0]["user"]
            result += self.viewer.getPage("home_logged_in.html", {"name": name})

        else:
            result += self.viewer.getPage("home_not_logged_in.html")

        return result
