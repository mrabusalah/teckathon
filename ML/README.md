To run the machine learning part:
run in the ML dir
```python3
pip3 install -r requirements
```
then place your video in the training_models dir and run:
```python3
python3 detect.py <video_name>
```
or if you want to use it with your video cam
```python3
python3 detect.py <camera_index>
```