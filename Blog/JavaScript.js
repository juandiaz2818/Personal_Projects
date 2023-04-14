 $(document).ready(function(){
//this script is for the carousel of images//
$('.img-Poli').slick({
    dots: true,
    infinite: true,
    speed: 500,
    fade: true,
    cssEase: 'linear'
  });

  $('.armenia').slick({
    dots: true,
    infinite: true,
    speed: 500,
    fade: true,
    cssEase: 'linear'
  });
    });
//end of the second carousel script//


//this script change the css for each radio button
const OP1 =document.querySelector('input[value="Option1"]');
const OP2 =document.querySelector('input[value="Option2"]');
const OP3 =document.querySelector('input[value="Option3"]');
const examp1 = document.getElementById('examp');

function fadeIn(){
  examp1.style.opacity =0.5;
  
  setTimeout(function(){
    examp1.style.opacity =1;
  },150);


}



OP1.addEventListener('click', function() {
 
  examp1.style.backgroundColor = '#D88123';
  examp1.style.borderRadius = '20px';
  examp1.style.color = '#23D832';
  examp1.style.borderBlockColor = '#9B00FF';
  examp1.style.boxShadow = '0 0 15px #9B00FF';

  fadeIn();
});

OP2.addEventListener('click', function() {
  examp1.style.backgroundColor = '#D82A23';
  examp1.style.borderRadius = '20px';
  examp1.style.color = '#0022B1';
  examp1.style.borderBlockColor = '#F9DE01';
  examp1.style.boxShadow = '0 0 15px #F9DE01';

  fadeIn();
  
});

OP3.addEventListener('click', function() {
  examp1.style.backgroundColor = 'white';
  examp1.style.borderRadius = '20px';
  examp1.style.color = '#000000';
  examp1.style.borderBlockColor = '#0176F9';
  examp1.style.boxShadow = '0 0 15px #0176F9';

  fadeIn();
  
});
//end of radio buttoms css

const mibutton = document.getElementById("buttom")

  mibutton.addEventListener("click", function() {
  mibutton.classList.toggle("change1");
});

const mibutton2 = document.getElementById("buttom2")

  mibutton2.addEventListener("click", function() {
  mibutton2.classList.toggle("change2");
});

const mibutton3 = document.getElementById("buttom3")

  mibutton3.addEventListener("click", function() {
  mibutton3.classList.toggle("change3");
});


const checkStyles = document.getElementById("checkbox2");

checkStyles.addEventListener('change', function(){

  const Style = document.getElementById('stylesheet');

  if (checkStyles.checked){
    Style.disabled = false;
  }else{
    Style.disabled = true;
  }
});



