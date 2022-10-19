# Airtable

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | Airtable                           |
| Version        | v1.0.0                                |
| DockerHub | [weevenetwork/airtable](https://hub.docker.com/r/weevenetwork/airtable) |
| authors        | Jakub Grzelak                    |

- [Airtable](#airtable)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Write single or batch of data to a selected Airtable base and table. IMPORTANT: **all** data labels must match exactly column names in the selected Airtable table.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| Base ID    | BASE_ID         | string   | ID of Airtable base that holds the table.            |
| API Key    | API_KEY         | string  | User API key to Airtable.            |
| Data Table    | TABLE         | string  | Table in Airtable where data will be written.            |


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)  |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
pyairtable
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "label-1": 12,
    "label-2": "speed"
}
```

* batch of JSON body objects, example:

```json
[
    {
        "temperature": 12,
        "device": "Konin-1"
    },
    {
        "temperature": 15,
        "device": "Konin-1"
    }
]
```

## Output

New records written to a selected TABLE in Airtable.
