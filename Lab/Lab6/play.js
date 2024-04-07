let fac = 0;
let number = prompt("Enter number : ");
number = parseInt(number)
for(let i = 1 ; i<number ; i++){
    fac *= i
    console.log(fac)
}