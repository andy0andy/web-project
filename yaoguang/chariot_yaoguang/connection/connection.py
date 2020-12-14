import chariot
from .schema import ConnectionSchema, Input
# Custom imports below


from ..util.yaoguang_sdk import YaoGaung


class Connection(chariot.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        """
        Connection config params are supplied as a dict in
        params or also accessible in self.parameters['key']

        The following will setup the var to be accessed
          self.blah = self.parameters['blah']
        in the action and trigger files as:
          blah = self.connection.blah
        """
        # TODO: Implement connection or 'pass' if no connection is necessary
        self.logger.info("Connect: Connecting...")

        token = params.get(Input.TOKEN)
        host = params.get(Input.HOST)

        yaoguang = YaoGaung(host=host, token=token)


        self.yaoguang = yaoguang



    def test(self):
        # TODO: Implement connection test
        pass
