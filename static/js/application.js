var control = '/api/1/control';
var monitor = '/api/1/monitor';

$(document).ready(function() {
  $('#mixer_on').change(function() {
    $.post( control, { sensor: "mixer", state: "1" }).done(function( data ) {
        $(this).prop('disabled',true);
        $('#mixer_off').prop('disabled',false);
    });
  });

  $('#mixer_off').change(function() {
    $.post( control, { sensor: "mixer", state: "0" }).done(function( data ) {
        $(this).prop('disabled',true);
        $('#mixer_on').prop('disabled',false);
    });
  });

  // Increase (state=1) or decrease (state=0) ph to 0.1
  $('#inc_ph').click(function() {
    $.post( control, { sensor: "ph", state: "1" }).done(function(data) {
        $('#ph_level').text(data["state"]);
    });
  });

  $('#dec_ph').click(function() {
    $.post( control, { sensor: "ph", state: "0" }).done(function(data) {
        console.log(data);
        $('#ph_level').text(data["state"]);
    });
  });
});
