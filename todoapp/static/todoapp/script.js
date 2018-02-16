var tick = function(){
  time -= 1;
  // console.log("tick", time);
  document.getElementById("timer").textContent = time;

  if (time <= 10 && time > 5){  
  document.getElementById("timer").style.color = "orange";
  }
    else if (time <= 5){  
  document.getElementById("timer").style.color = "red";
  }
    if (time <= 0){
    clearInterval(interval);
  }
}