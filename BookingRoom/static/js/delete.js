$(document).ready(function () {
    $('a[id="del"]').on('click', function () {

        var action = confirm("Are you sure you want to delete this reservation?")

        if (action) {
            let object_id = $(this).attr('pk');
            //let object_id = $(this).parents('tr').first().attr('id');
            //console.log(object_id); Проверка id
            let data_url = $('#del').attr("data_url");
            // весь ajax передается в view
            $.ajax({
                url: data_url,
                //url: "http://127.0.0.1:8000/delete/" +  object_id + '/' , захардкоженный урл
                type: "get",
                data: {'pk': object_id},
                headers: {'X-Requested-With': 'XMLHttpRequest'},
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
            },
                success: function (data) {
                    if (data.deleted){
                    alert("Успешно");
                    $('#' + object_id).remove()
                    }else{
                        alert("Уже удалено");
                    }

                },
                 error: function  (error) {
                     console.log(error);
                     alert("error")
                 }
            });


        }
    });
})
