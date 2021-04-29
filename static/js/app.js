const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");
// transfer the view to the sign up part of the page with animation
sign_up_btn.addEventListener("click", () => {
	container.classList.add("sign-up-mode");
});
// transfer the view to the sign in part of the page with animation
sign_in_btn.addEventListener("click", () => {
	container.classList.remove("sign-up-mode");
});
