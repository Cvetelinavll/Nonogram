import firebase from "firebase/app";
import "firebase/auth";
import "firebase/firestore";

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  // Your Firebase configuration object goes here
  apiKey: "AIzaSyBFqvta_ckcTU7u_NKeN2AcCUC5TCboGxo",
  authDomain: "nonogram-82919.firebaseapp.com",
  projectId: "nonogram-82919",
  storageBucket: "nonogram-82919.appspot.com",
  messagingSenderId: "240868843524",
  appId: "1:240868843524:web:5c10e1e0765f96040f9551",
  measurementId: "G-07LW9FHV4F"
};

firebase.initializeApp(firebaseConfig);

export const auth = firebase.auth();
export const firestore = firebase.firestore();

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);