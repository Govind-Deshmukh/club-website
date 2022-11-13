import React from "react";
import { useState } from "react";
import swal from "sweetalert";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  // Login function
  const handleSubmit = (e) => {
    e.preventDefault();

    const article = { username: email, password: password };

    try {
      fetch("http://localhost:5000/api/student/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(article),
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          if (data.status) {
            localStorage.setItem("name", data.name);
            localStorage.setItem("email", data.email);
            swal("Success", data.message, "success");
            setTimeout(() => {
              window.location.href = "/dashboard";
            }, 2000);
          } else {
            swal("Error", data.message, "error");
          }
        });
    } catch (err) {
      console.log(err);
    }
  };

  // show password on click eye icon
  const showPassword = () => {
    const password = document.getElementById("password");
    const eye = document.getElementById("eye");
    if (password.type === "password") {
      password.type = "text";
      eye.classList.remove("fa-eye");
      eye.classList.add("fa-eye-slash");
    } else {
      password.type = "password";
      eye.classList.remove("fa-eye-slash");
      eye.classList.add("fa-eye");
    }
  };

  return (
    <div className="">
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label">email address</label>
          <input
            required
            type="email"
            className="form-control"
            aria-describedby="emailHelp"
            onChange={setEmail}
          />
        </div>
        <div className="form-group mb-3">
          <label className="form-label">password</label> <br />
          <div className="input-group">
            <input
              required
              type="password"
              id="password"
              className="form-control"
              onChange={setPassword}
            />
            <span className="input-group-text" onClick={showPassword}>
              <i className="fa-solid fa-eye eye"></i>
            </span>
          </div>
        </div>

        <button type="submit" className="btn btn-success btn-lg">
          Login
        </button>
      </form>
    </div>
  );
}
