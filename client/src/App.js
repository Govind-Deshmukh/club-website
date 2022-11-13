import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import React from "react";
import Auth from "./components/auth/auth";
function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Auth />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
