// src/firebase.js
import { initializeApp } from 'firebase/app';
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut } from 'firebase/auth';

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
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

export { auth, provider, signInWithPopup, signOut };
