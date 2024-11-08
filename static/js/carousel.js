currentSlideID = 1

sliderElement = document.getElementById("slider")
totalslides = sliderElement.childElementCount
console.log(totalslides)


function next(){
    if(currentSlideID<totalslides){
    currentSlideID++
    showslide()
       
    }

}

function prev(){
    if(currentSlideID > 1){
    currentSlideID--
    showslide()
   
    }

}
function showslide(){
    slides = document.getElementById("slider").getElementsByTagName("div")
    for (let index = 0; index < totalslides; index++) {
        const element = slides[index];
        if (currentSlideID===index+1){
                element.classList.remove("hidden")
        }else{
            element.classList.add("hidden")
        }

    }

}