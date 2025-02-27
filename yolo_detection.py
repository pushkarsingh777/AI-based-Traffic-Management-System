import serial
import time
import cv2
import torch
from ultralytics import YOLO
import serial.tools.list_ports
import os

def get_available_port():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if "USB" in port.description or "Arduino" in port.description:
            return port.device
    return None

com_port = get_available_port()
if com_port:
    arduino = serial.Serial(port=com_port, baudrate=9600, timeout=1)
    time.sleep(2)
else:
    print("No available serial port found. Check your connection!")
    arduino = None

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLO("yolov8n.pt").to(device)

def count_vehicles(frame):
    results = model(frame)
    vehicle_count = 0

    for result in results:
        for box in result.boxes:
            conf = box.conf[0].item()
            if conf > 0.5:
                vehicle_count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])  
                label = f"Vehicle {conf:.2f}"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return vehicle_count, frame

def calculate_green_time(vehicle_count):
    base_time = 10
    additional_time = 2 * vehicle_count
    return min(base_time + additional_time, 60)

def detect_vehicles_image(image_path):
    if not os.path.exists(image_path):
        print(f"Error: Image '{image_path}' not found!")
        return
    
    frame = cv2.imread(image_path)
    if frame is None:
        print("Error: Could not read the image!")
        return

    frame = cv2.resize(frame, (640, 480))
    vehicle_count, frame_with_boxes = count_vehicles(frame)
    green_time = calculate_green_time(vehicle_count)

    print(f"Vehicles detected: {vehicle_count}, Green time: {green_time} sec")

    if arduino:
        try:
            arduino.write(f"{green_time}\n".encode())
        except serial.SerialException:
            print("Error: Serial communication failed!")

    cv2.imshow("YOLO Vehicle Detection (Image)", frame_with_boxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_vehicles_video(video_source):
    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print("Error: Cannot open video source!")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        vehicle_count, frame_with_boxes = count_vehicles(frame)
        green_time = calculate_green_time(vehicle_count)

        print(f"Vehicles detected: {vehicle_count}, Green time: {green_time} sec")

        if arduino:
            try:
                arduino.write(f"{green_time}\n".encode())
            except serial.SerialException:
                print("Error: Serial communication failed!")

        cv2.imshow("YOLO Vehicle Detection (Video)", frame_with_boxes)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

input_path = "traffic.mp4"

if input_path.endswith(('.jpg', '.png', '.jpeg')):  
    detect_vehicles_image(input_path)
elif input_path.endswith(('.mp4', '.avi', '.mov')):  
    detect_vehicles_video(input_path)
else:
    print("Error: Unsupported file format!")

if arduino:
    arduino.close()
