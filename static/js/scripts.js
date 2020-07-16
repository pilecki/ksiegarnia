function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
  document.body.style.backgroundColor = "white";
}

// Variables for up and down quantity buttons and input field 

let countDownBtn = document.querySelector('.decrement-qty');
let input = document.querySelector('.qty_input');
let countUpBtn = document.querySelector('.increment-qty');

// Function to check input value

const checkInputValue = function (){

    let num3 = (input.value = parseInt(input.value))
    
    countDownBtn.setAttribute('disabled', '');

    if (num3 > 1 ) {
       countDownBtn.removeAttribute('disabled', ''); 
    }
    if ( num3 >= 98 ){
        countUpBtn.setAttribute('disabled', '');
    }
    if (num3 < 99 ) {
       countUpBtn.removeAttribute('disabled', ''); 
    }
} 


// Incerement quantity
   
countUpBtn.addEventListener('click', (event) => {
event.preventDefault()
input.value = parseInt(input.value) +1
checkInputValue();
});

// Decrement quantity

countDownBtn.addEventListener('click', (event) => {
    event.preventDefault()
    input.value = parseInt(input.value) - 1
  checkInputValue();
}); 
