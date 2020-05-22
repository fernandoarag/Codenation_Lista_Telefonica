from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
     'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
     'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
     'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
     'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
     'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
     'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
     'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
     'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
     'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
     'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564627800, 'start': 1564626000}
]


def calcPrice(records):
    x = 0

    for x in range(len(records)):
        start = datetime.fromtimestamp(records[x].get('start'))
        end = datetime.fromtimestamp(records[x].get('end'))
        time = end - start
        posicao = x
        records[posicao]['custo'] = round(calcPriceList(start, end, time), 2)


def calcPriceList(start, end, time):
    enc = 0.36
    calcPriceCall = 0

    if start.hour >= 6:
        if end.hour <= 21 and end.minute <= 59:
            calcPriceCall = (((time.total_seconds())//60) * 0.09)+enc

        if end.hour >= 22 and end.minute > 0:
            calcPriceCall += enc
    else:
        calcPriceCall = enc

    return round(calcPriceCall, 2)


def classify_by_phone_number(records):
    calcPrice(records)
    result = {}
    adc = 0
    y = 0

    for x in range(len(records)):
        if not result:
            result = [{'source': records[x]['source'],
                       'total': records[x]['custo']}]
        else:
            for y in range(len(result)):
                if result[y]['source'] == records[x]['source'] and adc == 0:
                    result[y]['total'] = round(
                        (result[y]['total'] + records[x]['custo']), 2)
                    adc = 1

            if result[y]['source'] != records[x]['source'] and adc == 0:
                result.append(
                    {'source': records[x]['source'],
                     'total': round(records[x]['custo'], 2)})
                adc = 1
        adc = 0
    result.sort(key=lambda k: k['total'], reverse=True)
    print(result)
    return result


classify_by_phone_number(records)
