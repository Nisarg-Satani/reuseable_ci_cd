$(document).ready(function() {
console.log("Success!")
$('#submit_btn').click(function (e) {
            e.preventDefault();
            e.stopPropagation();
            toastr.success("submitted!");
            var formData = new FormData();
			formData.append('Project_name',$('#Project_name').val());
			formData.append('Authenticate', $('#Authenticate').val());
			formData.append('Git_Url', $('#Git_Url').val());
			formData.append('Branch_Name',$('#Branch_Name').val());
            formData.append('username', $('#username').val());
            formData.append('token', $('#token').val());
            console.log(formData)
             $.ajax({
                url: '/submit',
                type: 'POST',
                data: formData,
                processData: false,  // tell jQuery not to process the data
                contentType: false,  // tell jQuery not to set contentType
                success: function (data) {
                    console.log("data", data);
                    if (data['status']==502){
//                        alert(data['message'])
                          toastr.error(data['message']);
                    } else if (data['status']==200) {
                        toastr.success(data['message']);
                    }
                }
            });
            $('#myform')[0].reset();  // Reset all form data after submit
        })

});

