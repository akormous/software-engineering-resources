# MongoDB

MongoDB is a document database designed for ease of development and scaling.

<details>
    <summary>Document Database</summary>

- A record in MongoDB is a document, which is a data structure composed of field and value pairs.
- It is similar to JSON.
- Example

```js
{
    name: "Cypher",
    rank: "Radiant",
    location: "Morocco",
    type: "Sentinel"
}
```
### Advantages of using documents:
- Documents (objects) correspond to native data types in many programming languages.
- Embedded documents and arrays reduce need for expensive joins.
- Dynamic schema supports fluent polymorphism.

</details>

<details>
    <summary>Connect MongoDB with Node.js</summary>

- Install the MongoDB Node driver
```
npm install mongodb
```
- Check out this documentation - [MongoDB Node Driver](https://docs.mongodb.com/drivers/node/current/)
</details>

<details>
    <summary>Basics</summary>

- MongoDB stores data records as **BSON documents** which are gathered together in **collections**.
- A database stores one or more collections
</details>