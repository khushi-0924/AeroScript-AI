# 🚀 AeroScript AI - Markerless Gesture-Driven Virtual Environment

**An AI-powered gesture-controlled air drawing system that transforms your webcam into a virtual canvas.**

AeroScript AI is a sophisticated real-time gesture recognition system that allows you to draw, annotate, and interact with a digital canvas using natural hand movements—no stylus, touch screen, or additional hardware required. Built with Python, OpenCV, and MediaPipe.

[![Python 3.7+](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Latest-green.svg)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Solutions-blue.svg)](https://mediapipe.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Features

### ✍️ Advanced Drawing System
- **Real-time Hand Tracking**: Precise finger position detection using MediaPipe Hand Landmarks
- **Smooth Stroke Rendering**: Continuous, fluid drawing strokes without lag
- **Index Finger Drawing**: Natural drawing interface using your index finger as a digital pencil
- **Customizable Brush Sizes**: Adjust brush thickness on-the-fly for detailed or bold strokes

### 🎨 Intuitive Gesture-Based Controls

| Gesture | Action | Description |
|---------|--------|-------------|
| ☝️ **Index Finger** | Draw | Use index finger as a digital pen |
| ✌️ **Index + Middle** | Select Blue | Switch to blue color |
| 🤟 **Index + Middle + Ring** | Select Red | Switch to red color |
| 🖖 **Index + Middle + Ring + Pinky** | Select Green | Switch to green color |
| 🖐️ **Open Palm** | Eraser Mode | Activate area-based eraser tool |
| 🤏 **Thumb + Index Pinch** | Pause/Stop | Pause or stop drawing |

### 🧽 Smart Eraser System
- **Palm Center Detection**: Uses palm landmark (landmark 9) for precise positioning
- **Area-Based Eraser**: Erases a large circular region for efficient clearing
- **Natural Interaction**: Intuitive hand gesture mimics real-world eraser behavior

### 📊 Dynamic Real-Time UI
Live system information displayed on canvas:
```
MODE: DRAW | COLOR: GREEN | BRUSH: 5 | ERASER: 60 | FPS: 30
```
- **MODE**: Current operation mode (DRAW, ERASE, PAUSE)
- **COLOR**: Active drawing color
- **BRUSH**: Current brush size in pixels
- **ERASER**: Eraser radius in pixels
- **FPS**: Real-time frames per second

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.7+** | Core application language |
| **OpenCV** | Real-time video processing and rendering |
| **MediaPipe** | Hand detection and gesture recognition |
| **NumPy** | Efficient image and numerical operations |

---

## 📁 Project Structure

```
air-drawing/
├── main.py                 # Application entry point
├── hand_tracking.py        # Hand detection and landmark extraction
├── gesture_control.py      # Gesture recognition and mapping
├── drawing_utils.py        # Canvas rendering and drawing utilities
├── ui.py                   # Dynamic UI overlay and information display
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── LICENSE                # MIT License
```

### File Descriptions

- **main.py**: Orchestrates the entire application, manages video capture, and coordinates modules
- **hand_tracking.py**: Wraps MediaPipe Hand detector, extracts 21 hand landmarks, and manages hand frame data
- **gesture_control.py**: Interprets finger positions and gestures, maps to drawing actions
- **drawing_utils.py**: Manages the virtual canvas, renders strokes, and handles color/eraser operations
- **ui.py**: Renders real-time statistics and visual feedback on the canvas

---

## ⚙️ Installation

### Prerequisites
- Python 3.7 or higher
- Webcam (integrated or external)
- 4GB RAM minimum

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/air-drawing.git
cd air-drawing
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### requirements.txt
```
opencv-python==4.8.0.76
mediapipe==0.10.1
numpy==1.24.3
```

---

## ▶️ Running the Application

### Basic Startup
```bash
python main.py
```

### With Command-Line Arguments (Optional)
```bash
# Specify camera index (default: 0)
python main.py --camera 0

# Set initial brush size (default: 5)
python main.py --brush 10

# Set eraser size (default: 60)
python main.py --eraser 80

# Combine arguments
python main.py --camera 0 --brush 8 --eraser 50
```

---

## 🎮 Controls & Keyboard Shortcuts

| Input | Action |
|-------|--------|
| **ESC** | Exit application |
| **C** | Clear canvas |
| **R** | Reset to default settings |
| **B** | Increase brush size |
| **V** | Decrease brush size |
| **E** | Increase eraser size |
| **D** | Decrease eraser size |
| **S** | Save current drawing |
| **Hand Gestures** | See Gesture Controls table above |

---

## 🧠 How It Works

### Pipeline Overview
1. **Video Capture** → Webcam captures live video feed at 30 FPS
2. **Hand Detection** → MediaPipe detects hands and extracts 21 landmark coordinates
3. **Gesture Recognition** → Finger positions analyzed to determine current action
4. **Action Mapping** → Gestures translated to drawing operations
5. **Canvas Rendering** → Strokes rendered on virtual canvas in real-time
6. **UI Overlay** → System information and visual feedback displayed on top

### Gesture Recognition Algorithm
- **Landmark Analysis**: 21 hand landmarks processed per frame
- **Finger State Detection**: Each finger classified as extended or folded
- **Multi-Finger Combinations**: Recognizes 2-4 finger combinations for color selection
- **Smoothing Filter**: Reduces jitter from detection noise for stable drawing

### Performance Optimization
- Efficient NumPy operations for image processing
- GPU acceleration via OpenCV (when available)
- Frame-based processing with adjustable resolution

---

## 📊 Use Cases

### 🎓 Education & Online Teaching
- Zoom/Google Meet presentations with gesture-controlled annotations
- Real-time diagram drawing during lectures
- Interactive whiteboarding without stylus hardware

### 👨‍💼 Professional Presentations
- Gesture-based slide annotations
- Real-time diagram creation
- Interactive data visualization

### 🎨 Digital Art & Creativity
- Air-based creative drawing
- Gesture-controlled sketching
- Novel artistic expression through hand movements

### 🔬 Human-Computer Interaction
- Research platform for gesture recognition systems
- Touchless interface development
- Accessibility solutions for alternative input methods

### 🤖 AI/ML Applications
- Training data for gesture recognition models
- Real-time inference demonstrations
- Computer vision system showcase

---

## 🔥 Future Enhancements

### Planned Features
- ✨ **Advanced Gesture Stabilization**: Reduce flickering and jitter using temporal filtering
- 🎨 **Enhanced UI**: Interactive color palette, brush shape preview, transparency controls
- 💾 **Save Functionality**: Export drawings as PNG, SVG, or video
- 🔷 **Shape Detection**: Automatic recognition of circles, squares, triangles
- 📱 **Web/Mobile Integration**: Browser-based version using TensorFlow.js
- 🎯 **Multi-Hand Support**: Simultaneous tracking of both hands for collaborative drawing
- 🎨 **Advanced Filters**: Blur, sharpen, and artistic effects on-canvas
- 🌐 **Cloud Sync**: Save and share drawings online
- 🎥 **Recording Mode**: Capture drawing sessions as videos

### Under Consideration
- Pressure sensitivity simulation based on hand distance
- Advanced color palette system
- Undo/Redo functionality
- Layer support for complex compositions

---

## 📸 Demo

*Demo video and screenshots coming soon!*

To see the project in action:
1. Clone the repository
2. Install dependencies
3. Run `python main.py`
4. Perform hand gestures in front of your webcam
5. Watch your drawings appear on the digital canvas in real-time

---

## 📝 Configuration

### Customizing Behavior

Edit the following parameters in `main.py` to customize the application:

```python
# Canvas properties
CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720
BACKGROUND_COLOR = (0, 0, 0)  # Black background

# Drawing properties
DEFAULT_BRUSH_SIZE = 5
DEFAULT_ERASER_SIZE = 60
BRUSH_COLOR_BLUE = (255, 0, 0)      # BGR format
BRUSH_COLOR_RED = (0, 0, 255)       # BGR format
BRUSH_COLOR_GREEN = (0, 255, 0)     # BGR format

# Performance settings
TARGET_FPS = 30
HAND_DETECTION_CONFIDENCE = 0.8
HAND_TRACKING_CONFIDENCE = 0.5
```

---

## 🚨 Troubleshooting

### Issue: Webcam not detected
**Solution**: Check camera permissions and ensure no other application is using the webcam.
```bash
# On Linux, list available cameras
ls /dev/video*
```

### Issue: High latency/lag
**Solution**: Reduce canvas resolution or close background applications.
```python
# In main.py, reduce resolution
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480
```

### Issue: Poor hand tracking
**Solution**: Ensure good lighting and clear background contrast.
- Increase ambient lighting
- Use a contrasting background
- Adjust hand detection confidence threshold

### Issue: Application crashes
**Solution**: Ensure all dependencies are correctly installed.
```bash
pip install -r requirements.txt --upgrade
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guide for Python code
- Add docstrings to all functions
- Include comments for complex logic
- Test changes before submitting PR
- Update README if adding new features

### Report Issues
Found a bug? Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs. actual behavior
- System information (OS, Python version, etc.)

---

## 📜 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

### Summary
You are free to:
- ✅ Use commercially
- ✅ Modify the code
- ✅ Distribute
- ✅ Use privately

With the condition that:
- ⚠️ Include a copy of the license
- ⚠️ State changes made to the code

---

## 👨‍💻 Author

**Khushi Patel**
- GitHub: [@khushi-patel](https://github.com/khushi-patel)
- Email: khushi.patel@example.com

---

## ⭐ Show Your Support

If you found this project helpful or interesting:
- ⭐ **Star** the repository
- 🍴 **Fork** to contribute
- 💬 **Share** with others
- 📧 **Provide feedback**

Your support means a lot! Thank you for using AeroScript AI.

---

## 📚 References & Resources

### Libraries & Documentation
- [OpenCV Documentation](https://docs.opencv.org/)
- [MediaPipe Hand Landmarks Guide](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)
- [NumPy Documentation](https://numpy.org/doc/)

### Related Projects
- [OpenCV Webcam Tutorial](https://docs.opencv.org/master/dd/d43/tutorial_py_video_basics.html)
- [MediaPipe Solutions](https://mediapipe.dev/)
- [Python Image Processing Handbook](https://realpython.com/image-processing-with-the-python-pillow-library/)

### Academic Papers
- Hand Pose Estimation: *Hand-Object Interaction Recognition* (2021)
- Gesture Recognition: *Real-time Hand Gesture Detection* (2020)

---

## 🐛 Known Issues

- Occasional hand detection loss in low-light conditions
- Gesture recognition may be inconsistent with partial hand visibility
- Performance varies based on system specifications

These issues are being addressed in future releases.

---

## 📞 Support & Contact

Have questions or need help?

- 📧 Email: support@aeroscriptai.com
- 💬 GitHub Discussions: [Open a discussion](https://github.com/your-username/air-drawing/discussions)
- 🐛 Bug Reports: [Report a bug](https://github.com/your-username/air-drawing/issues)

---

## 🎯 Roadmap

### Version 1.1 (Q2 2024)
- [ ] Gesture stabilization improvements
- [ ] Enhanced UI with color palette
- [ ] Save/Export functionality
- [ ] Documentation improvements

### Version 1.2 (Q3 2024)
- [ ] Shape detection system
- [ ] Multi-hand support
- [ ] Advanced filters
- [ ] Undo/Redo system

### Version 2.0 (Q4 2024)
- [ ] Web-based interface
- [ ] Mobile app version
- [ ] Cloud synchronization
- [ ] Collaborative drawing features

---

<div align="center">

Made with ❤️ by Khushi Patel

**[⬆ Back to Top](#-aeroscript-ai---markerless-gesture-driven-virtual-environment)**

</div>
