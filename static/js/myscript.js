
timer_id = 0
let counter
function start_counter(){
    counter = document.getElementById('counter');
    start_button = document.getElementById('start')
    if (start_button.innerText == 'Start'){
      start_button.innerText = 'Pause';
      timer_id = setInterval(function() {
        counter.innerText = parseInt(counter.innerText) + 1;
      }, 1000);
    }
    else{
      start_button.innerText = 'Start';
      clearInterval(timer_id);
    }
}

function pause_counter(){
  pause_button = document.getElementById('stop');
  if (pause_button.innerText == 'Pause'){
    pause_button.innerText = "Resume";
    clearInterval(timer_id)
  }
  else{
    pause_button.innerText = "Pause";
    timer_id = setInterval(function() {
      counter.innerText = parseInt(counter.innerText) + 1;
    }, 1000);
  }
  
}