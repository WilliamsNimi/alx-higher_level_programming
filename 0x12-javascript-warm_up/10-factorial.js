#!/usr/bin/node
function fact (a)
{
    if (a === 1)
    {
        return 1;
    }
    return fact(a - 1) * fact(a - 2);
}

console.log(fact(process.argv[2]));
