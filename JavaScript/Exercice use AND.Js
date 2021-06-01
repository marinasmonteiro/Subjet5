function advise_weather(a,b){
    if (a=="raining" && b=="cold"){
        return ("take an umbrella and a jacket!");
    } 
    else if (a=="raining" && b=="warm") {
        return("take an umbrella and a T-shirt!");
    } 
    else if (a=="sunny" && b=="cold") {
        return("take sunglasses and a jacket!");
    } 
    else if  (a=="sunny" && b=="warm") {
        return("take sunglasses and T-Shirt!");
    } 
    else {
        return("stay at home!")
    }
}
console.log(advise_weather("raining","warm"))
console.log(advise_weather("sunny","warm"))
console.log(advise_weather("sunny","cold"))
console.log(advise_weather("raining","cold"))
console.log(advise_weather("foggy","normal"))