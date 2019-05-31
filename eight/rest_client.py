import jsonschema




def validate_response(schema, resp, body):

    '''
    这个方法属于类级别，
    如果返回的状态在成功的里
    :param schema: 契约里面规定的这个接口的大概要求，从中取出状态码，
    :param resp: 响应是返回
    :param body: 响应中返回的body体的内容
    分两部分验证，一部分是头信息，一部分是body体信息，如果验证有问题抛出异常
    :return:
    '''

