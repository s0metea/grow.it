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


        $('#sys_on').click(function () {
            $.post(control, {sensor: "fertigator_state", state: 1}).done(function (data) {
                console.log(data);
                $(this).prop('disabled', true);
                $('#sys_off').prop('disabled', false);
            })
        });

        $('#sys_off').click(function () {
            $.post(control, {sensor: "fertigator_state", state: 0}).done(function (data) {
                $(this).prop('disabled', true);
                $('#sys_on').prop('disabled', false);
            })
        });

        $('#acid_pump').click(function () {
            $.post(control, {sensor: "acid_pump", state: 1}).done(function (data) {
                console.log(data);
            });
        })
});

