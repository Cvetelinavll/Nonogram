// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAT2Pa_7HG0nOtZ8PPOE-LN85UDPZd8S0E",
  authDomain: "nonogrambackend.firebaseapp.com",
  projectId: "nonogrambackend",
  storageBucket: "nonogrambackend.appspot.com",
  messagingSenderId: "165792213409",
  appId: "1:165792213409:web:c74bcf6098866cf38683e0",
  measurementId: "G-RB2L5MZ43L"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);