$(document).ready(function(){
  $('#submit').click(function(e){
    e.preventDefault();
    $.ajax({
      type:'POST',
      url:'/xyz/user/',
      data:{
        ids:$('#fa4e2a34ab06a').val(),
        password:$("#faa2da1ad083").val(),
      },
      dataType:"json",
      success:function(response){
        window.location.href="http://localhost:8000/signup/";
      }
    });
  });    
})

'<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>'