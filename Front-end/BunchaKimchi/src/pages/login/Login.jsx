import React from "react";
import "./login.css";
import PropTypes from "prop-types";
import { useState } from "react";
import { LoginUsers } from "./dummyLoginData";
async function loginUser(credentials) {
  // var formBody = [];
  // for (var property in credentials) {
  //   var encodedKey = encodeURIComponent(property);
  //   var encodedValue = encodeURIComponent(credentials[property]);
  //   formBody.push(encodedKey + "=" + encodedValue);
  // }
  // formBody = formBody.join("&");
  // const data = await fetch("http://172.16.0.84:8000/user/login", {
  //   method: "POST",
  //   headers: {
  //     "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
  //   },
  //   body: formBody,
  // })
  //   .then((data) => data.json())
  //   .catch((err) => {
  //     console.log(credentials);
  //     console.log(err);
  //   });
  // const newData = { token: data.token };
  // return newData;
  const filteredLoginUser = await LoginUsers.filter((user) => {
    return (
      user.email === credentials.username &&
      user.password === credentials.password
    );
  });
  console.log("users", credentials);
  console.log("filtereduser", filteredLoginUser[0]);
  if (filteredLoginUser[0] == undefined) {
    return 0;
  }
  console.log("con", filteredLoginUser);
  return { token: filteredLoginUser[0].token };
}

export default function Login({ setToken }) {
  const [username, setUserName] = useState();
  const [password, setPassword] = useState();
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [accountError, setAccountError] = useState("");
  const [showPassword, setShowPassword] = useState("password");
  const isValidEmail = (email) => {
    const emailRegex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,}$/i;
    const isEmail = emailRegex.test(email);
    if (!isEmail) {
      setEmailError("Please enter valid email");
      return;
    }
    setEmailError("");
    return isEmail;
  };
  const isValidPassWord = (password) => {
    if (password.length >= 8) {
      setPasswordError("");
      return true;
    }
    setPasswordError("Password must be at least 8 characters");
    return;
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (isValidEmail(username) && isValidPassWord(password)) {
      const token = await loginUser({
        username,
        password,
      });
      if (!token) {
        setAccountError("Your account doesnt't exist");
      }
      setToken(token);
    }
  };
  const handlePassword = () => {
    if (showPassword === "password") {
      setShowPassword("text");
    } else setShowPassword("password");
  };
  return (
    <div className="login">
      <div className="loginWrapper">
        <div className="loginLeft">
          <h3 className="loginLogo">KoreanSocial</h3>
          <span className="loginDesc">
            Connect with friends in HaNoi around you on NewSocial
          </span>
        </div>
        <div className="loginRight">
          <div className="loginBox">
            <input
              type="email"
              placeholder="Email"
              className="loginInput relative"
              onChange={(e) => setUserName(e.target.value)}
            />
            <p className="redtext">{emailError}</p>
            <input
              type={showPassword}
              placeholder="Password"
              className="loginInput"
              onChange={(e) => setPassword(e.target.value)}
            />
            <p className="redtext">{passwordError}</p>
            <div className="showPassword">
              <input type="checkbox" onClick={handlePassword} />
              <span>Show Password</span>
            </div>
            <p className="redtext">{accountError}</p>
            <button className="loginButton" onClick={handleSubmit}>
              Log In
            </button>
            <button className="loginRgisterButton">
              <a href="/register">Create a new Account</a>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
Login.propTypes = {
  setToken: PropTypes.func.isRequired,
};
