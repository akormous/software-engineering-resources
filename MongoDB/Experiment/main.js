// Importing MongoClient from mongodb (npm) library
const {MongoClient} = require('mongodb');
const utility = require('./utility.js');

const agents_data = require('./sample_data.json');

const utils = new utility();

async function main() {
    // URI for local MongoDB instance
    const uri = "mongodb://localhost:27017";

    const client = new MongoClient(uri);

    try {
        await client.connect();
        console.log("\nCONNECTED to Local MongoDB\n");

        /* 
            DO ALL YOUR STUFF HERE
        */

        console.log(await utils.listDatabases(client));
        
        
        console.log(agents_data);        
        await client.close();
        console.log("\nDISCONNECTED from Local MongoDB\n");
    } catch(e) {
        console.log(e);
    }
    
}

main();