/* Bunch of utility function defined here */
const {MongoClient} = require('mongodb');


class utility {
    constructor() {
        console.log("Utility functions: READY");
    }

    // listDatabases: returns list of databases available
    async listDatabases(client) {

        try {
            let dbs = await client.db().admin().listDatabases();
            
            let db_list = [];
            dbs.databases.forEach(db => db_list.push(db.name));
            return db_list;

        } catch(e) {
            console.log(e);
            throw(e);
        }
    }
};

module.exports = utility;
