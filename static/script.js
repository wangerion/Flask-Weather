function showdrop (){
    let dp = document.getElementsByClassName('weather-info-dropdown-content')[0];
    if (dp.style.display == "none"){
        dp.style.display = "block";
    }
    else {
        dp.style.display = "none";
    }
    var list = document.getElementsByName('values');
    console.log(list.innerHTML);
}
