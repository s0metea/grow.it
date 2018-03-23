var control = '/api/1/control';
var monitor = '/api/1/monitor';

$(document).ready(function() {
        $('#mixer_on').change(function () {
            $.post(control, {sensor: "mixer_state", state: true}).done(function (data) {
                $(this).prop('disabled', true);
                $('#mixer_off').prop('disabled', false);
            });
        });

        $('#mixer_off').change(function () {
            $.post(control, {sensor: "mixer_state", state: false}).done(function (data) {
                $(this).prop('disabled', true);
                $('#mixer_on').prop('disabled', false);
            });
        });

        // Increase (state=1) or decrease (state=0) ph to 0.1
        $('#inc_ph').click(function () {
            $.post(control, {sensor: "plant_ph", state: true}).done(function (data) {
                console.log(data);
                $('#plant_ph').text(data["state"]);
            })
        });

        $('#dec_ph').click(function () {
            $.post(control, {sensor: "plant_ph", state: false}).done(function (data) {
                console.log(data);
                $('#plant_ph').text(data["state"]);
            })
        });

        $('#pour_off').click(function () {
            $.post(control, {sensor: "pour_off", state: true}).done(function (data) {
                console.log(data);
            })
        });


        $('#sys_on').change(function () {
            $.post(control, {sensor: "fertigator_state", state: true}).done(function (data) {
                console.log(data);
                $(this).prop('disabled', true);
                $('#sys_off').prop('disabled', false);
            })
        });

        $('#sys_off').change(function () {
            $.post(control, {sensor: "fertigator_state", state: false}).done(function (data) {
                console.log(data);
                $(this).prop('disabled', true);
                $('#sys_on').prop('disabled', false);
            })
        });


        var update_data = function () {
            $.get( monitor + "/all").done(function( data ) {success(data)});
        };

        var success = function(data) {
            $("#water_level").html(data['water_level']);
            $("#current_ph").html(data['current_ph']);
            update_pump_state("#tank_pump_in", data['tank_pump_in']);
            update_pump_state("#tank_pump_out", data['tank_pump_out']);
            update_pump_state("#water_pump", data['water_pump']);
            update_pump_state("#acid_pump", data['acid_pump']);
            update_pump_state("#alkali_pump", data['alkali_pump']);
            update_pump_state("#fertilizer_pump", data['fertilizer_pump']);
            setTimeout(update_data, 500);
        };

        var update_pump_state = function(pump, state) {
            if(state)
                $(pump).removeClass('alert-danger').addClass('alert-success');
            else
                $(pump).removeClass('alert-success').addClass('alert-danger');
        };

        update_data();

        var tank_pump_in_state = false;
        var tank_pump_out_state = false;
        var water_pump_state = false;
        var acid_pump_state = false;
        var alkali_pump_state = false;
        var fertilizer_pump_state = false;


        $('#tank_pump_in').click(function () {
            tank_pump_in_state = !tank_pump_in_state;
            $.post(control, {sensor: "tank_pump_in", state: tank_pump_in_state}).done(function (data) {
                console.log(data);
            });
        });
        $('#tank_pump_out').click(function () {
            tank_pump_out_state = !tank_pump_out_state;
            $.post(control, {sensor: "tank_pump_out", state: !tank_pump_out_state}).done(function (data) {
                console.log(data);
            });
        });
        $('#water_pump').click(function () {
            water_pump_state = !water_pump_state;
            $.post(control, {sensor: "water_pump", state: !water_pump_state}).done(function (data) {
                console.log(data);
            });
        });
        $('#acid_pump').click(function () {
            acid_pump_state = !acid_pump_state;
            $.post(control, {sensor: "acid_pump", state: !acid_pump_state}).done(function (data) {
                console.log(data);
            });
        });
        $('#alkali_pump').click(function () {
            alkali_pump_state = !alkali_pump_state;
            $.post(control, {sensor: "alkali_pump", state: !alkali_pump_state}).done(function (data) {
                console.log(data);
            });
        });
        $('#fertilizer_pump').click(function () {
            fertilizer_pump_state = !fertilizer_pump_state;
            $.post(control, {sensor: "fertilizer_pump", state: !fertilizer_pump_state}).done(function (data) {
                console.log(data);
            });
        });
});

