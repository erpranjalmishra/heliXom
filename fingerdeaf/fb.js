// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBeMJiHy4WB0SBq3ZbPqAAJCaE19uEvBnY",
  authDomain: "glogin-34b11.firebaseapp.com",
  projectId: "glogin-34b11",
  storageBucket: "glogin-34b11.appspot.com",
  messagingSenderId: "555647419945",
  appId: "1:555647419945:web:459c291879a8f36d26fe38",
  measurementId: "G-PBG5G4FRFK"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);