#!/usr/bin/node
if(typeof(process.argv[2]) === 'number'){
    for (let i = 0; i < parseInt(process.argv[2]); i++){
        for (let j = 0; j < parseInt(process.argv[2]); j++)
        {
            console.log('X');
        }
    }
}
else{
    console.log('Missing size');
}
