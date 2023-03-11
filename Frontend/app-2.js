var firebaseConfig = {
  apiKey: "AIzaSyDjGYijrdvaOMXq26Lc2IS9OQKKL7D_KXI",
  authDomain: "someprojectbi.firebaseapp.com",
  projectId: "someprojectbi",
  storageBucket: "someprojectbi.appspot.com",
  messagingSenderId: "311803201634",
  appId: "1:311803201634:web:c878ce2f7be0cba463e93b",
  measurementId: "G-5RH59VY3QQ",
};

firebase.initializeApp(firebaseConfig);

const auth = firebase.auth();

console.log(auth);

let signOutButton = document.getElementById("signout");
signOutButton.addEventListener("click", (e) => {
  //Prevent Default Form Submission Behavior
  e.preventDefault();
  console.log("clicked");

  auth.signOut();
  alert("Signed Out");
  window.location = "index.html";
});
