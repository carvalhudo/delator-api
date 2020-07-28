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

- **404** on error (when there's no devices registered on database):

```json
{
    "message": "there's no devices registered on database!"
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
    "message": "the device 'dev_id' isn't registered on database!"
}
```

**Register a new device**

`POST /devices`

**Arguments**

- ```user```: The user name registered on server
- ```pass```: The password associated to the user
- ```device-id```: The ID of device
- ```serial-number```: The serial number of device
- ```description```: The description of device
- ```group```: The group of device

**Expected response**

- **201** on success

```json
{
    "message": "device registered with success!"
}
```

- **409** on error

```json
{
    "message": "the device 'dev_id' already exist on database!"
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
    "message": "device unregistered with success!"
}
```

- **404** on error

```json
{
    "message": "the device 'dev_id' isn\'t registered on database!"
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
    "message": "device updated with success!"
}
```

- **404** on error

```json
{
    "message": "the device 'dev_id' isn\'t registered on database!"
}
```

#### 2.2 Ocurrences

**Get all ocurrences**

`GET /ocurrences`

**Arguments**

- ```user```: The user name registered on server
- ```pass```: The password associated to the user

**Expected response**

- **200** on success

```json
[
    {
        "device-id": "foo",
        "timestamp": "sáb jul 11 00:31:07 -03 2020"
    },
    {
        "device-id": "bar",
        "timestamp": "dom jun 7 10:10:07 -03 2020"
    }
]
```

- **404** on error (when there's no ocurrences registered on database):

```json
{
    "message": "there's no ocurrences registered on database!"
}
```

**Register a new ocurrence**

`POST /ocurrences`

**Arguments**

- ```user```: The user name registered on server
- ```pass```: The password associated to the user
- ```device-id```: The ID of device
- ```timestamp```: The timestamp of ocurrence

**Expected response**

- **201** on success

```json
{
    "message": "ocurrence registered with success!"
}
```
