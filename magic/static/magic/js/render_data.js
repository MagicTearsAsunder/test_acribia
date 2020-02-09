function render_data(){

  var $data = $('#responses')

  $.ajax({
    type: 'GET',
    url: 'api/response/',
    success: function (data) {
      $data.empty()
      $.each(data, function(i, data) {
        $data.append('<li>'+ data.response +'</li>')
      });
    }
  });
};

$(document).ready(function(){ setInterval('render_data()', 3000); });
