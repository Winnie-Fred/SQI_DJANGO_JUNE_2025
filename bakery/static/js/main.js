const signUpModal = document.getElementsByClassName('signUpModal')[0]

setTimeout(() => {
    signUpModal.style.display = "block";
}, 3000);

const closeBtn = document.getElementById("closeBtn");

closeBtn.addEventListener("click", function () {
    signUpModal.style.display = "none";
})
