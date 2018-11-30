class CustomException(Exception):
    pass


def re():
    raise CustomException('自定义异常')


re()
