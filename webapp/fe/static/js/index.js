let statusBtn = false

document.getElementById("actionbtn").addEventListener("click", () => {
    if(statusBtn){
        statusBtn = false
        document.getElementById("actionbtn").innerText = "Press to display";
    }else{
        statusBtn = true
        document.getElementById("actionbtn").innerText = "Press to hide";
    }

})
