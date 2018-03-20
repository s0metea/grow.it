var control = '/api/1/control';
var monitor = '/api/1/monitor';

$(document).ready(function() {
        $('#mixer_on').change(function () {
            $.post(control, {sensor: "mixer_state", state: 1}).done(function (data) {
                $(this).prop('disabled', true);
                $('#mixer_off').prop('disabled', false);
            });

        });

        $('#mixer_off').change(function () {
            $.post(control, {sensor: "mixer_state", state: 0}).done(function (data) {
                $(this).prop('disabled', true);
                $('#mixer_on').prop('disabled', false);
            });
        });

        // Increase (state=1) or decrease (state=0) ph to 0.1
        $('#inc_ph').click(function () {
            $.post(control, {sensor: "plant_ph", state: 0.1}).done(function (data) {
                console.log(data);
                $('#plant_ph').text(data["state"]);
            })
        });

        $('#dec_ph').click(function () {
            $.post(control, {sensor: "plant_ph", state: -0.1}).done(function (data) {
                console.log(data);
                $('#plant_ph').text(data["state"]);
            })
        });


        $('#sys_on').change(function () {
            $.post(control, {sensor: "fertigator_state", state: 1}).done(function (data) {
                console.log(data);
                $(this).prop('disabled', true);
                $('#sys_off').prop('disabled', false);
            })
        });

        $('#sys_off').change(function () {
            $.post(control, {sensor: "fertigator_state", state: 0}).done(function (data) {
                console.log(data);
                $(this).prop('disabled', true);
                $('#sys_on').prop('disabled', false);
            })
        });


        var update_pumps = function () {
            $.get( monitor + "/all").done(function( data ) {success(data)});
        };

        var success = function(data) {
            update_pump_state("#tank_pump_in", data['tank_pump_in']);
            update_pump_state("#tank_pump_out", data['tank_pump_out']);
            update_pump_state("#water_pump", data['water_pump']);
            update_pump_state("#acid_pump", data['acid_pump']);
            update_pump_state("#alkali_pump", data['alkali_pump']);
            update_pump_state("#fertilizer_pump", data['fertilizer_pump']);
            setTimeout(update_pumps, 300);
        };

        var update_pump_state = function(pump, state) {
            if(state)
                $(pump).removeClass('alert-danger').addClass('alert-success');
            else
                $(pump).removeClass('alert-success').addClass('alert-danger');
        };

        update_pumps();

        $('#acid_pump').click(function () {
            $.post(control, {sensor: "acid_pump", state: 1}).done(function (data) {
                console.log(data);
            });
        });
});

