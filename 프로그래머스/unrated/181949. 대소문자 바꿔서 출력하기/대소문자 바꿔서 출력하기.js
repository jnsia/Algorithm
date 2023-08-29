const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    
    var str2 = ''
    
    for (var i = 0; i < str.length; i++) {
        if (str[i].match(/[A-Z]/g)) {
            str2 = str2 + str[i].toLowerCase()
        } else {
            str2 = str2 + str[i].toUpperCase()
        }        
    }
    
    console.log(str2)
});