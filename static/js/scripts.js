$("form[name=signup_form").submit(function (e) {
	// grap the input data from the form
	var $form = $(this);
	var $error = $form.find(".error");
	var data = $form.serialize();
	// send the input data to the sign up route to be saved in the mongodb
	$.ajax({
		url: "/user/signup",
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/dashboard/";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("error--hidden");
		},
	});

	e.preventDefault();
});

//send the user data to the login route to assign a session to the logged in user

$("form[name=login_form").submit(function (e) {
	var $form = $(this);
	var $error = $form.find(".error");
	var data = $form.serialize();

	$.ajax({
		url: "/user/login",
		type: "POST",
		data: data,
		dataType: "json",
		success: function (resp) {
			window.location.href = "/dashboard/";
		},
		error: function (resp) {
			$error.text(resp.responseJSON.error).removeClass("error--hidden");
		},
	});

	e.preventDefault();
});
