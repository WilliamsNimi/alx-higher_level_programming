#!usr/bin/node
class Square extends Square{
    constructor(size)
    {
        super(size, size);
    }
    
    charPrint(c)
    {
        if (typeof(c) === "undefined")
        {
            this.print();
        }
        else
        {
            for (let i = 0; i < this.width; i++){
                for (let j = 0; j < this.height; j++)
                {
                    console.log("X");
                }
            }
        }
    }
}