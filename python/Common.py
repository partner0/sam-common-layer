import datetime
import traceback

class LambdaBase(object):
    @classmethod
    def get_handler(cls, *args, **kwargs):
        def handler(event, context):
            try:
                print("# LambdaBase - Payload: ", event)
                return cls(*args, **kwargs).handle(event, context)
            except:
                return {
                    "statusCode": 500,
                    "source": "LambdaBase",
                    "message": traceback.format_exc().split("\n"),
                }
            return
        return handler

    def handle(self, event, context):
        raise NotImplementedError