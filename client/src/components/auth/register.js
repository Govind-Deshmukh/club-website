import React from "react";
import { useState } from "react";
import swal from "sweetalert";
export default function Register() {
  const [name, setName] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [domain, setDomain] = useState("");
  const [yera, setYear] = useState("");
  const [password, setPassword] = useState("");

  // Register function
  const handleSubmit = (e) => {
    e.preventDefault();

    const article = {
      name: name,
      username: username,
      email: email,
      domain: domain,
      year: yera,
      password: password,
    };

    try {
      fetch("http://localhost:5000/api/student/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(article),
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          if (data.status) {
            swal("Success", "Register Successfull", "success");
            // wait for 1 second
            setTimeout(() => {
              window.location.href = "/";
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
          <label className="form-label">Full Name</label>
          <input
            required
            type="text"
            className="form-control"
            aria-describedby="emailHelp"
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Create username</label>
          <input
            required
            type="text"
            className="form-control"
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Email address</label>
          <input
            required
            type="email"
            className="form-control"
            aria-describedby="emailHelp"
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Select domain</label>
          <select
            required
            className="form-select"
            name="domain"
            aria-label="Default select example"
            onChange={(e) => setDomain(e.target.value)}
          >
            <option selected value="None">
              Select . . .
            </option>
            <option value="Computer Science & Engineering">
              Computer Science & Engineering
            </option>
            <option value="Information Technology">
              Information Technology
            </option>
            <option value="Mechnical Engineering">Mechnical Engineering</option>
            <option value="Civil Engineering">Civil Engineering</option>
            <option value="Electronics & Telecom Engineering">
              Electronics & Telecom Engineering
            </option>
            <option value="BCA">BCA</option>
            <option value="BCS">BCS</option>
          </select>
        </div>
        <div className="mb-3">
          <label className="form-label" for="form3Example4">
            Current educational year
          </label>
          <select
            required
            className="form-select"
            name="year"
            aria-label="Default select example"
            onChange={(e) => setYear(e.target.value)}
          >
            <option selected>Select . . .</option>
            <option value="First Year (B.E / B.Tech)">
              First Year (B.E / B.Tech)
            </option>
            <option value="Second Year (B.E / B.Tech)">
              Second Year (B.E / B.Tech)
            </option>
            <option value="Third Year (B.E / B.Tech)">
              Third Year (B.E / B.Tech)
            </option>
            <option value="Final Year (B.E / B.Tech)">
              Final Year (B.E / B.Tech)
            </option>
            <option value="First Year (BCA / BCS)">
              First Year (BCA / BCS)
            </option>
            <option value="Second Year (BCA / BCS)">
              Second Year (BCA / BCS)
            </option>
            <option value="Third Year (BCA / BCS)">
              Third Year (BCA / BCS)
            </option>
          </select>
        </div>

        <div className="form-group mb-3">
          <label className="form-label">Password</label> <br />
          <div className="input-group">
            <input
              required
              type="password"
              id="password"
              className="form-control"
              onChange={(e) => setPassword(e.target.value)}
            />
            <span className="input-group-text" onClick={showPassword}>
              <i className="fa-solid fa-eye" id="eye"></i>
            </span>
          </div>
        </div>

        <button type="submit" className="btn btn-warning btn-lg">
          Register
        </button>
      </form>
    </div>
  );
}
