import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Profile from "./pages/profile/Profile.jsx";
import Home from "./pages/home/Home.jsx";
import Login from "./pages/login/Login.jsx";
import Register from "./pages/register/Register.jsx";
import useToken from "./utils/useToken.js";
function App() {
  const { token, setToken } = useToken();

  if (!token) {
    return (
      <>
        <BrowserRouter>
          <Routes>
            <Route index element={<Login setToken={setToken} />}></Route>

            <Route path="/register" element={<Register />} />
          </Routes>
        </BrowserRouter>
      </>
    );
    // return <Login setToken={setToken} />;
  }
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
