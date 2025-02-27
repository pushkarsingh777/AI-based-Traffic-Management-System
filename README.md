# Traffic-Management-System

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YOLO Vehicle Detection</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; padding: 20px; background-color: #f4f4f4; }
        h1, h2 { color: #333; }
        pre { background: #ddd; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>YOLO Vehicle Detection</h1>
    <p>This project uses YOLO (You Only Look Once) for real-time vehicle detection and calculates adaptive green signal timing based on traffic density.</p>
    
    <h2>Features</h2>
    <ul>
        <li>Detects vehicles from images and video feeds</li>
        <li>Calculates adaptive green light timing</li>
        <li>Communicates with an Arduino to adjust traffic signals</li>
    </ul>
    
    <h2>Installation</h2>
    <p>Ensure you have Python installed, then install dependencies:</p>
    <pre>pip install -r requirements.txt</pre>
    
    <h2>Usage</h2>
    <p>Run the script with an image or video file:</p>
    <pre>python main.py</pre>
    
    <h2>Requirements</h2>
    <p>Make sure you have the following installed:</p>
    <pre>
        Python 3.x
        OpenCV
        PyTorch
        Ultralytics YOLO
        PySerial
    </pre>
    
    <h2>License</h2>
    <p>MIT License</p>
</body>
</html>
