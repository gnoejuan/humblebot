import facebook

class HumbleFacebook(object):
    """This is the servants interface to facebook"""
    def __init__(self, passedAccessToken):
        self.classAccessToken = passedAccessToken
        ##self.graph = facebook.GraphAPI(access_token=localAccessToken)
    ##@classmethod
    ## 2 hours later and I find out that @classmethod was the reason nothing was working
    ## Zipeedeedoooooooooooooooh dah.     
    def postMessage(self, Humblemessage):
        graph = facebook.GraphAPI(access_token=self.classAccessToken)
        graph.put_object(parent_object='me', connection_name='feed', message=Humblemessage)
