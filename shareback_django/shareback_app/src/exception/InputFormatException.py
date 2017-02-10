class InputFormatException(Exception):
    def __init__(self, msg):
        super(InputFormatException, self).__init__("Invalid Input Format "+msg)