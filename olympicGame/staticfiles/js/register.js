// • June 4, 2018 
// • CSS Daily Practice
// • Day #5
// • Friends_Code_Challenge


// Start From Here 
ctop = $("#wrapper-content").offset().top;
cleft = $("#wrapper-content").offset().left;
cheight = $("#wrapper-content").height();
cwidth = $("#wrapper-content").width();

function loop() {
  $("#circle__1").each(function() {
    randomtop = ctop + Math.floor(Math.random() * (cheight - ctop));
    randomleft = cleft + Math.floor(Math.random() * (cwidth - cleft));
    $(this).animate(
      {
        top: randomtop,
        left: randomleft
      },8000, 'linear', function() {
        loop();
      }
    );
  });
  $("#circle__2").each(function() {
    randomtop = ctop + Math.floor(Math.random() * (cheight - ctop) );
    randomleft = cleft + Math.floor(Math.random() * (cwidth - cleft - 100) * 1.2);
    $(this).animate(
      {
        top: randomtop,
        left: randomleft
      },8000, 'linear', function() {
        loop();
      }
    );
  });
  $("#circle__3").each(function() {
    randomtop = ctop + Math.floor(Math.random() * (cheight - ctop) *1.4);
    randomleft = cleft + Math.floor(Math.random() * (cwidth - cleft - 100) * .8);
    $(this).animate(
      {
        top: randomtop,
        left: randomleft
      },8000, 'linear', function() {
        loop();
      }
    );
    
  });
  $("#circle__4").each(function() {
    randomtop = ctop + Math.floor(Math.random() * (cheight - ctop) *.6);
    randomleft = cleft + Math.floor(Math.random() * (cwidth - cleft - 100) * .3);
    $(this).animate(
      {
        top: randomtop,
        left: randomleft
      },8000, 'linear', function() {
        loop();
      }
    );
  });
  $("#circle__5").each(function() {
    randomtop = ctop + Math.floor(Math.random() * (cheight - ctop) *.2);
    randomleft = cleft + Math.floor(Math.random() * (cwidth - cleft - 100) * .6);
    $(this).animate(
      {
        top: randomtop,
        left: randomleft
      },8000, 'linear', function() {
        loop();
      }
    );
  });
};
loop();

$(".welcome__content").hide();

$('#form-btn').on('click', function() {
  $(".form__content").fadeOut(800, function() {
    $(".welcome__content").fadeIn(1000);
  });
});

$('#welcome-btn').on('click', function() {
  $(".welcome__content").fadeOut(1000, function() {
    $(".form__content").fadeIn(800);
  });
});
