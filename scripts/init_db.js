db_name = 'delator-db'
db = db.getSiblingDB(db_name)

db.createRole(
    {
        role: 'device-role',
        privileges : [
            { resource : { 'db' : db_name, 'collection': 'ocurrences' }, actions: ['insert'] },
            { resource : { 'db' : db_name, 'collection': 'devices' }, actions: ['insert'] }
        ],
        roles : []
    }
);

db.createRole(
    {
        role: 'front-role',
        privileges : [
            { resource : { 'db' : db_name, 'collection': 'ocurrences' }, actions: ['find'] },
            { resource : { 'db' : db_name, 'collection': 'devices' }, actions: ['insert', 'remove', 'find', 'update'] }
        ],
        roles : []
    }
);

db.createUser(
    {
        user: 'front-user',
        pwd: 'front-pass',
        roles: [
            { role: 'front-role', db: db_name, collection: 'ocurrences' },
            { role: 'front-role', db: db_name, collection: 'devices' }
        ]
    }
);

db.createUser(
    {
        user: 'device-user',
        pwd: 'device-pass',
        roles: [
            { role: 'device-role', db: db_name, collection: 'ocurrences' },
            { role: 'device-role', db: db_name, collection: 'devices' }
        ]
    }
);
