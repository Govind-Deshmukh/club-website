import React from "react";
import swal from "sweetalert";
import { useState } from "react";

export default function Auth() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  // Login function
  const handleSubmit = (e) => {
    e.preventDefault();
    const article = { username: email, password: password };
    try {
      fetch("http://localhost:5000/api/admin/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(article),
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          if (data.status) {
            localStorage.setItem("admin", true);
            localStorage.setItem("name", data.name);
            localStorage.setItem("email", data.email);
            swal(data.message);
            window.location.href = "/dashboard";
          } else {
            swal(data.message);
          }
        });
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label">Email address</label>
          <input
            type="email"
            className="form-control"
            aria-describedby="emailHelp"
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Password</label>
          <input
            type="password"
            className="form-control"
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <button type="submit" className="btn btn-primary">
          Submit
        </button>
      </form>
    </div>
  );
}
