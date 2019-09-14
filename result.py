class Result(object):
    def __init__(self, result, dates, stats, ):
        self.result = result
        self.dates = dates



def object_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'User':
        return Result(obj['name'], obj['username'])
    return obj