const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('close', function () {
    var sstr = `!@#$%^&*(\\'"<>?:;`
    
    console.log(sstr)
});