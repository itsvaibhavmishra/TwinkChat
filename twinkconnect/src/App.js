import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          TwinkChat | Real-Time <code>MERN</code> Chat App.
        </p>
        <a
          className="App-link"
          href="https://twinkconnect.netlify.app"
        >
          Connect Now!
        </a>
      </header>
    </div>
  );
}

export default App;
