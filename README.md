# DELATOR API

### 1. Brief Introduction

This document aims to describe the usage of all resources provided by API, giving all information
related to each defined endpoint (arguments, available operations and expected results).

### 2. Endpoints

#### 2.1 Devices

**Get all devices**

`GET /devices`

**Arguments**

- ```user```: The user name registered on server
- ```pass```: The password associated to the user

**Expected response**

- **200** on success

```json
[
    {
        "id": "foo",
        "serial-number": "bar",
        "description": "device description",
        "status": "online",
        "group": "group-foo",
        "coordinates": "-3.71839,-38.5434"
    },
    {
        "id": "bar",
        "serial-number": "foo",
        "description": "device description",
        "status": "offline",
        "group": "group-bar",
        "coordinates": "-4.83093,-37.7816"
    }
]
```

- **404** on error (when the database is empty):

```json
{
    "message": "no devices registered!"
}
```

**Get a specific device**

`GET /device/<string:id>`

**Arguments**

- ```user```: The user name registered on server
- ```pass```: The password associated to the user

**Expected response**

- **200** on success

```json
{
    "id": "foo",
    "serial-number": "bar",
    "description": "device description",
    "status": "online",
    "group": "group-foo",
    "coordinates": "-3.71839,-38.5434"
}
```

- **404** on error (when the device doesn't exist):

```json
{
    "message": "device not registered!"
}
```

**Register a new device**

`POST /device/<string:id>`

**Arguments**

- ```user```: The user name registered on server
- ```pass```: The password associated to the user
- ```serial-number```: The serial number of device
- ```description```: The description of device
- ```group```: The group of device

**Expected response**

- **200** on success

```json
{
    "message": "device registered!"
}
```

- **409** on error

```json
{
    "message": "the device is already registered!"
}
```

**Unregister a device**

`DELETE /device/<string:id>`

**Arguments**

- ```user```: The user name registered on server
- ```pass```: The password associated to the user

**Expected response**

- **200** on success

```json
{
    "message": "device unregistered!"
}
```

- **404** on error

```json
{
    "message": "the device does not exist on database!"
}
```

**Update a device**

`PUT /device/<string:id>`

**Arguments**

- ```user```: The user name registered on server
- ```pass```: The password associated to the user
- ```param```: The name of parameter to be updated
- ```value```: The new value of the parameter

**Expected response**

- **200** on success

```json
{
    "message": "device updated!"
}
```

- **404** on error

```json
{
    "message": "the device does not exist on database!"
}
```
