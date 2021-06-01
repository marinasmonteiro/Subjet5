var gender="KIG";
if (gender=="female"){
    console.log("hello Madame! Welcome back!");
} else if(gender=="male"){
    console.log("hello Sir Welcome back!");
} else {
    console.log("Hello! Welcome back!");
};

function greet(gender){
    if(gender=="male"){
        return("Hello Sir! Welcome Back!");
    } else if(gender=="female"){
        return("Hello Madam!Welcome Back!");
    } else{
        return("Hello! Welcome back!");
    }
}

console.log(greet("male"));
console.log(greet("female"));
console.log(greet("ddddd"));