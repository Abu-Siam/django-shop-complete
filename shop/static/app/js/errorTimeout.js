var message_elements = document.querySelectorAll('#error-message');
var newList = [...message_elements]

setTimeout(function(){
   console.log(message_elements)
   for(const message_ele of newList){
   message_ele.style.display = "none";}
}, 3000);

