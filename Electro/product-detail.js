function openTab(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("detail-menu-text");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    if(evt) evt.currentTarget.className += " active";
    else document.querySelector('button.detail-menu-text').className += " active";
    
    // document.getElementById(tabName).style.display = "block";
    // evt.currentTarget.className += " active";
  }
  document.body.addEventListener('DOMContentLoaded', openTab(event, 'descriptions-content'));

    /* Set the width of the side navigation to 250px */
function openAssideNav() {
  document.getElementById("add-to-cart").style.width = "352px";
  document.getElementById("gray-bg").style.backgroundColor = "rgba(0,0,0,0.5)";
}

/* Set the width of the side navigation to 0 */
function closeAssideNav() {
  document.getElementById("add-to-cart").style.width = "0";
  document.getElementById("gray-bg").style.backgroundColor = "unset";
}

function incrementCartItemNum(){
  cartNum = document.getElementById("card-num-text").innerHTML;
  if(cartNum < 2){
    cartNum++;
    document.getElementById("card-num-text").innerHTML = cartNum;
  }
}

function changePrice(whichColor){
  let colors = document.getElementsByClassName("color-shape");



  switch (whichColor.className) {
    case "color-shape color-shape1":
    document.getElementsByClassName("price-text")[0].innerHTML = "$1999.00";
    for (let i = 0; i < colors.length; i++) {
      colors[i].style.width = "36px";
      colors[i].style.height = "36px";
    }
    document.getElementById("color1").style.width = "45px";
    document.getElementById("color1").style.height = "45px";
    break;

    case "color-shape color-shape2":
    document.getElementsByClassName("price-text")[0].innerHTML = "$2100.00";
    for (let i = 0; i < colors.length; i++) {
      colors[i].style.width = "36px";
      colors[i].style.height = "36px";
    }
    document.getElementById("color2").style.width = "45px";
    document.getElementById("color2").style.height = "45px";
    break;

    case "color-shape color-shape3":
    document.getElementsByClassName("price-text")[0].innerHTML = "$1850.00";
    for (let i = 0; i < colors.length; i++) {
      colors[i].style.width = "36px";
      colors[i].style.height = "36px";
    }
    document.getElementById("color3").style.width = "45px";
    document.getElementById("color3").style.height = "45px";
    break;

    case "color-shape color-shape4":
    document.getElementsByClassName("price-text")[0].innerHTML = "$1800.00";
    for (let i = 0; i < colors.length; i++) {
      colors[i].style.width = "36px";
      colors[i].style.height = "36px";
    }
    document.getElementById("color4").style.width = "45px";
    document.getElementById("color4").style.height = "45px";
    break;
  }

}


function removeItem(whichTrash , price){
  const parentElement = whichTrash.parentNode;
  parentElement.style.display = "none";
  let num = document.getElementById("cart-item-numbers").innerHTML;
  num--;
  switch(num) {
    case 1:
      document.getElementById("cart-item-numbers").innerHTML = num;
      document.getElementById("items").innerHTML = "item";
      break;
    case 0:
      document.getElementById("cart-item-numbers").innerHTML = "no";
      document.getElementById("items").innerHTML = "items";
      break;
    default:
      document.getElementById("cart-item-numbers").innerHTML = num;
  }
  let subtotal = document.getElementById("subtotal").innerHTML;
  subtotal = subtotal.replace("$", "");
  subtotal = (subtotal - price).toFixed(2);
  document.getElementById("subtotal").innerHTML = "$" + subtotal;

  cartNum = document.getElementById("card-num-text").innerHTML;
  cartNum--;
  document.getElementById("card-num-text").innerHTML = cartNum;
}


