<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Traffic Management System</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
      color: #333;
    }
    .container {
      max-width: 800px;
      margin: 20px auto;
      padding: 20px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    h1 {
      text-align: center;
      margin-bottom: 20px;
    }
    h2 {
      border-bottom: 2px solid #2c3e50;
      padding-bottom: 5px;
      margin-top: 30px;
    }
    a {
      color: #3498db;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    code {
      background: #eaeaea;
      padding: 2px 5px;
      border-radius: 3px;
      font-family: monospace;
    }
    .button {
      display: inline-block;
      padding: 10px 20px;
      background: #3498db;
      color: #fff;
      border-radius: 5px;
      text-align: center;
      margin: 10px 0;
    }
    .button:hover {
      background: #2980b9;
    }
    .features, .installation, .usage, .contributing, .license {
      margin-top: 20px;
    }
    .features ul, .installation ol {
      padding-left: 20px;
    }
    .footer {
      text-align: center;
      margin-top: 40px;
      color: #777;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🚦 Traffic Management System 🚗</h1>
    <p>
      The <strong>Traffic Management System</strong> is an intelligent system designed to manage and optimize traffic flow using real-time vehicle detection and adaptive signal control. This project leverages <strong>YOLOv8</strong> for vehicle detection and <strong>Arduino</strong> for controlling traffic lights.
    </p>

<div class="features">
      <h2>✨ Features</h2>
      <ul>
        <li>Real-time vehicle detection using YOLOv8.</li>
        <li>Adaptive traffic signal control based on vehicle density.</li>
        <li>Integration with Arduino for hardware control.</li>
        <li>Support for both images and video inputs.</li>
        <li>Easy-to-use Python script for detection and control.</li>
      </ul>
    </div>

<div class="installation">
      <h2>🚀 Installation</h2>
      <ol>
        <li>Clone the repository:
          <pre><code>git clone https://github.com/pushkarsingh777/Traffic-Management-System.git</code></pre>
        </li>
        <li>Navigate to the project directory:
          <pre><code>cd Traffic-Management-System</code></pre>
        </li>
        <li>Install the required Python libraries:
          <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Connect your Arduino and upload the provided sketch.</li>
      </ol>
    </div>

<div class="usage">
      <h2>📋 Usage</h2>
      <p>To run the Traffic Management System:</p>
      <ol>
        <li>Ensure your Arduino is connected and the correct COM port is set in the Python script.</li>
        <li>Run the Python script:
          <pre><code>python traffic_management.py</code></pre>
        </li>
        <li>Input the path to an image or video file when prompted.</li>
        <li>View the detection results and observe the traffic light control.</li>
      </ol>
    </div>

<div class="contributing">
      <h2>🤝 Contributing</h2>
      <p>Contributions are welcome! If you'd like to contribute to this project, please follow these steps:</p>
      <ol>
        <li>Fork the repository.</li>
        <li>Create a new branch for your feature or bugfix.</li>
        <li>Commit your changes and push to your branch.</li>
        <li>Submit a pull request.</li>
      </ol>
    </div>

<div class="license">
      <h2>📜 License</h2>
      <p>This project is licensed under the <strong>MIT License</strong>. See the <a href="LICENSE">LICENSE</a> file for details.</p>
    </div>

<div class="footer">
      <p>Made with ❤️ by <a href="https://github.com/pushkarsingh777">Pushkar Singh</a></p>
    </div>
  </div>
</body>
</html>
