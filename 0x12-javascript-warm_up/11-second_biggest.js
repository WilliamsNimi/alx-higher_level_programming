#!/usr/bin/node
x = 0;
if (process.argv.length === 3){
    console.log("0");
}
else if(process.argv){
    for (let i = 2; i < process.argv.length; i++)
    {
        if (x < process.argv[i])
        {
            x = process.argv[i];
        }
    }
}
else{
    console.log("0");
}

console.log(x)