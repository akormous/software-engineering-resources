/**
 * You started a search for an uber driver, => promise pending
 * The driver arrived at your location => promise fulfilled
 * The driver rejected your request => promise rejected
 */

let arrived = true;

// creating a promise
const ride = new Promise((resolve, reject) => {
    if(arrived) {
        resolve("Driver arrived! + ride data"); // resolve the promise with some data
    }
    else {
        reject("Driver not arrived! ERROR"); // reject the promise with an error and a reason
    }
});



// consuming a promise
ride
    .then(value => {
        // data that was resolved in the promise
        console.log(value);
    })
    .catch(error => {
        // error and reason that sent via reject method
        console.log(error);
    })
    .finally(() => {
        console.log("Process completed!")
    });

