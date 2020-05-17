
$(function(){
    $("#id_booking_time").timepicker({
        timeFormat: 'HH:mm:ss',
        interval: 60,
        minTime: '00:00:00',
        maxTime: '23:00:00',
        defaultTime: '00:00:00',
        startTime: '08:00:00',
    });
    $("#id_booked_time").timepicker({
        timeFormat: 'HH:mm:ss',
        interval: 60,
        minTime: '00:00:00',
        maxTime: '23:00:00',
        defaultTime: '00:00:00',
        startTime: '08:00:00',
    });

