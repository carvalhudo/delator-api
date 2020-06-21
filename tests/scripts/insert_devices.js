
db = connect('front-user:front-pass@localhost/delator-db')

db.devices.insertMany(
    [
        {
            'id': 'dev_01',
            'description': 'foo',
            'status': 'online',
            'group': 'bar',
            'coordinates': '-3.14:3.14'
        },
        {
            'id': 'dev_02',
            'description': 'foo',
            'status': 'online',
            'group': 'bar',
            'coordinates': '4.14:-22.1'
        },
        {
            'id': 'dev_03',
            'description': 'foo',
            'status': 'online',
            'group': 'bar',
            'coordinates': '4.51:-66.6'
        },
        {
            'id': 'dev_04',
            'description': 'foo',
            'status': 'online',
            'group': 'bar',
            'coordinates': '4.444:123.4'
        },
        {
            'id': 'dev_05',
            'description': 'foo',
            'status': 'online',
            'group': 'bar',
            'coordinates': '44.2:32.3'
        },
        {
            'id': 'dev_06',
            'description': 'foo',
            'status': 'online',
            'group': 'bar',
            'coordinates': '22.3:123.3'
        }
    ]
)
