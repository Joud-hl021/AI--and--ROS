# Object Tracking Using OpenCV

## Project Description
This project uses OpenCV's **CSRT Tracker** to track an object in a video. The user selects an object manually with the mouse, and the tracker follows it frame by frame throughout the video.

## Requirements
Before running the script, make sure you have the required dependencies installed. Use the following command to install OpenCV:
```bash
pip install opencv-contrib-python
```

## How to Run the Code
1. **Download and place the following files in the same directory:**
   - `object_tracking.py` (Python script)
   - `mnmnmn.mp4` (Video file used for tracking)

2. **Open a terminal or Spyder, then navigate to the directory where the files are saved.**
   If using a terminal, use the following command:
   ```bash
   cd path/to/your/folder
   ```

3. **Run the Python script:**
   ```bash
   python object_tracking.py
   ```

4. **Select the object to track:**
   - A window will open showing the first frame of the video.
   - Use the mouse to draw a box around the object you want to track.

5. **Tracking starts automatically:**
   - The object will be enclosed in a green bounding box.
   - If the tracker loses the object, the message "Tracking Failed!" will be displayed.
   - Press **'Q'** to exit the tracking window at any time.

## Tracker Used
The script uses the **CSRT (Channel and Spatial Reliability Tracker)** by default for better accuracy:
```python
tracker = cv2.legacy.TrackerCSRT_create()
```
If you want to experiment with other tracking algorithms, you can replace `CSRT` with:
- `cv2.legacy.TrackerKCF_create()` – Faster but less accurate.
- `cv2.legacy.TrackerMOSSE_create()` – Very fast but less stable.

## Notes
- Make sure the video file is correctly named and in the correct directory.
- If the tracking is slow, try using `KCF` or `MOSSE` trackers for better speed.



