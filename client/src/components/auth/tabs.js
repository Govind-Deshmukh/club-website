import React from "react";
import Login from "./login";
import Register from "./register";
export default function tabs() {
  return (
    <div className="container tab-container w-75 mt-4 mb-3">
      <ul className="nav nav-pills mb-3" id="pills-tab" role="tablist">
        <li className="nav-item" role="presentation">
          <button
            className="nav-link active"
            id="pills-home-tab"
            data-bs-toggle="pill"
            data-bs-target="#pillsLogin"
            type="button"
            role="tab"
            aria-controls="pillsLogin"
            aria-selected="true"
          >
            Login
          </button>
        </li>
        <li className="nav-item" role="presentation">
          <button
            className="nav-link"
            id="pills-profile-tab"
            data-bs-toggle="pill"
            data-bs-target="#pillsRegister"
            type="button"
            role="tab"
            aria-controls="pillsRegister"
            aria-selected="false"
          >
            Register
          </button>
        </li>
      </ul>
      <div className="tab-content" id="pills-tabContent">
        <div
          className="tab-pane fade show active"
          id="pillsLogin"
          role="tabpanel"
          aria-labelledby="pills-home-tab"
          tabindex="0"
        >
          {/* Login container  */}
          <Login />
        </div>
        <div
          className="tab-pane fade"
          id="pillsRegister"
          role="tabpanel"
          aria-labelledby="pills-profile-tab"
          tabindex="0"
        >
          {/* Register container */}
          <Register />
        </div>
      </div>
    </div>
  );
}
