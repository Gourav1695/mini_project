#include <opencv2/opencv.hpp>

#include <iostream>

using namespace cv;
using namespace std;

//  Webcam

// All we have to do is to extract frames (images) from the camera and show it in a continuous loop.

void main() 
{

	VideoCapture cap(0); // 0 = id of default camera;
	Mat img;
	
	while (true) {
	
		cap.read(img);
			imshow("Image", img);
			waitKey(1); // 1 so that it's not too slow
		}
}
