jQuery(function($){

  var status = $('#status'),
      btn = $('.btn-primary');

  $('form#connect').submit(function(event) {
      event.preventDefault();
      status.text('');
      btn.prop('disabled', true);

      var form = $(this),
          url = form.attr('action'),
          type = form.attr('type'),
          data = new FormData(this);

      $.ajax({
          url: url,
          type: type,
          data: data,
          success: callback,
          cache: false,
          contentType: false,
          processData: false
      });

  });

  function callback(msg) {
    // console.log(msg);
    if (msg.status) {
      status.text(msg.status);
      setTimeout(function(){
        btn.prop('disabled', false);
      }, 3000);
      return;
    }

    var ws_url = window.location.href.replace('http', 'ws');
        // join = (ws_url[ws_url.length-1] == '/' ? '' : '/');
    if(ws_url.indexOf("?") != -1 ){
        var join = ws_url.split("?")[0];
    }
    var url = join + 'ws?id=' + msg.id,
        socket = new WebSocket(url),
        terminal = document.getElementById('#terminal'),
        term = new Terminal({cursorBlink: true});

    console.log(url);
    term.on('data', function(data) {
      // console.log(data);
      socket.send(data);
    });

    socket.onopen = function(e) {
      $('.container').hide();
      term.open(terminal, true);
      term.toggleFullscreen(true);
    };

    socket.onmessage = function(msg) {
      // console.log(msg);
      term.write(msg.data);
    };

    socket.onerror = function(e) {
      console.log(e);
    };

    socket.onclose = function(e) {
      console.log(e);
      term.destroy();
      $('.container').show();
      status.text(e.reason);
      btn.prop('disabled', false);
    };
  }
});
