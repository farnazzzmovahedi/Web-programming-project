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




