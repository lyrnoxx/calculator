add=(a,b)=>a+b;
sub=(a,b)=>a-b;
mul=(a,b)=>a*b;
div=(a,b)=>a/b;

operate=(x,a,b)=>{
    if(x=='+'){
        add(a,b);
    };
    if(x=='-'){
        sub(a,b);
    };
    if(x=='*'){
        mul(a,b);
    };
    if(x=='/'){
        div(a,b);
    };
}

console.log(operate("+",10,5))