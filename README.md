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
        "description": "device description",
        "status": "online",
        "group": "group-foo",
        "coordinates": "-3.71839,-38.5434"
    },
    {
        "id": "bar",
        "description": "device description",
        "status": "offline",
        "group": "group-bar",
        "coordinates": "-4.83093,-37.7816"
    }
]
```

Or when the database is empty:

```json
{
    "message": "no devices registered!"
}
```

- **500** on failure

```json
{
    "message": "internal server error!"
}
```
