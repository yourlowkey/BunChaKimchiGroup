import "./register.css";
import { useState } from "react";
// const navigate = useNavigate();

export default function Register() {
  const [username, setUsername] = useState();
  const [password, setPassword] = useState();
  const [confirmPassword, setConfirmPassword] = useState();
  const [email, setEmail] = useState("");
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");
  const [usernameError, setUsernameError] = useState("");
  const [confirmPasswordError, setConfirmPasswordError] = useState();
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
      if (confirmPassword != password) {
        setConfirmPasswordError("Please enter valid confirm password");
        return;
      }
      setConfirmPasswordError("");
      setPasswordError("");
      return true;
    }
    setPasswordError("Password must be at least 8 characters");
    return;
  };
  const isValidUserName = (username) => {
    if (username.length < 2 || username.length > 4) {
      setUsernameError("Please enter nickname from 2 to 4 characters");
      return false;
    }
    setUsernameError("");
    return true;
  };
  async function registerUser() {
    // return fetch('http://localhost:8080/login', {
    //   method: 'POST',
    //   headers: {
    //     'Content-Type': 'application/json'
    //   },
    //   body: JSON.stringify(credentials)
    // })
    //   .then(data => data.json())
    window.location.href = "http://localhost:5173/register";
  }
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (
      isValidUserName(username) &&
      isValidEmail(email) &&
      isValidPassWord(password)
    ) {
      // const register = await registerUser({
      //   email,
      //   password,
      //   username,
      // });
      registerUser();
    }
    return;
  };
  return (
    <div className="login">
      <div className="loginWrapper">
        <div className="loginLeft">
          <h3 className="loginLogo">NewSocial</h3>
          <span className="loginDesc">
            Connect with friends and the world around you on NewSocial
          </span>
        </div>
        <div className="loginRight">
          <div className="loginBox">
            <input
              placeholder="Username"
              className="loginInput"
              onChange={(e) => setUsername(e.target.value)}
            />
            <p>{usernameError}</p>
            <input
              placeholder="Email"
              className="loginInput"
              onChange={(e) => setEmail(e.target.value)}
            />
            <p>{emailError}</p>
            <input
              placeholder="Password"
              className="loginInput"
              onChange={(e) => setPassword(e.target.value)}
            />
            <p>{passwordError}</p>
            <input
              placeholder="Password Again"
              className="loginInput"
              onChange={(e) => setConfirmPassword(e.target.value)}
            />
            <p>{confirmPasswordError}</p>
            <button className="loginButton" onClick={handleSubmit}>
              Sign up
            </button>
            <button className="loginRgisterButton">Log into account</button>
          </div>
        </div>
      </div>
    </div>
  );
}
