var firebaseConfig = {
  apiKey: "AIzaSyDjGYijrdvaOMXq26Lc2IS9OQKKL7D_KXI",
  authDomain: "someprojectbi.firebaseapp.com",
  projectId: "someprojectbi",
  storageBucket: "someprojectbi.appspot.com",
  messagingSenderId: "311803201634",
  appId: "1:311803201634:web:c878ce2f7be0cba463e93b",
  measurementId: "G-5RH59VY3QQ",
};
//Initialize Firebase
firebase.initializeApp(firebaseConfig);

const auth = firebase.auth();

//Signup Function
let signUpButton = document.getElementById("signup");
signUpButton.addEventListener("click", (e) => {
  //Prevent Default Form Submission Behavior
  e.preventDefault();
  console.log("clicked");

  var email = document.getElementById("inputEmail");
  var password = document.getElementById("inputPassword");

  auth
    .createUserWithEmailAndPassword(email.value, password.value)
    .then((userCredential) => {
      location.reload();
      // Signed in
      var user = userCredential.user;
      console.log("user", user.email);
    })
    .catch((error) => {
      var errorCode = error.code;
      var errorMessage = error.message;
      console.log("error code", errorCode);
      console.log("error Message", errorMessage);
    });
});

let signInButton = document.getElementById("signin");
signInButton.addEventListener("click", (e) => {
  //Prevent Default Form Submission Behavior
  e.preventDefault();
  console.log("clicked");

  var email = document.getElementById("inputEmail");
  var password = document.getElementById("inputPassword");

  auth
    .signInWithEmailAndPassword(email.value, password.value)
    .then((userCredential) => {
      // location.reload();
      // Signed in
      var user = userCredential.user;
      console.log("user", user.email);
      window.location = "messages.html";
    })
    .catch((error) => {
      var errorCode = error.code;
      var errorMessage = error.message;
      // alert("error code", errorCode)
      alert(errorMessage);
    });
});

//Lifecycle hooks
auth.onAuthStateChanged(function (user) {
  if (user) {
    var email = user.email;

    var users = document.getElementById("user");
    var text = document.createTextNode(email);

    users.appendChild(text);

    console.log(users);
    //is signed in
  } else {
  }
});
