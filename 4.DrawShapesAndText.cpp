#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;

//////////////  Draw Shapes and Text //////////////////////

void main() {

	// Blank Image 
	Mat img(512, 512, CV_8UC3, Scalar(255, 255, 255)); // white image
	// CV_8 - 8-bit - each pixel has value 0 to 255
	// CV_8U - unsigned. If it was signed value -128 to 127
	// CV_8UC3 - 3 colour channels BGR
	// color defined as Scalar(B,G,R)
	// Scalar(255, 0, 0) - BLUE colourspace
	// Scalar(255, 0, 255) -  PURPLE
	// Scalar(0, 0, 0) -  BLACK
	circle(img, Point(256, 256), 155, Scalar(0, 69, 255), FILLED); // orange 
	// Point(256,256) - origin/center point
	// circle(img, Point(256, 256), 155, Scalar(0, 69, 255)); // thin orange bordered circle
	// circle(img, Point(256, 256), 155, Scalar(0, 69, 255),10); // thick orange bordered circle

	rectangle(img, Point(130, 226), Point(382, 286), Scalar(255, 255, 255), FILLED);
	// see chapter 3 for alternative implementation
	// Top Left, Bottom Right points given in order 
	// Point(130, 226) - Top Left
	// Point(382, 286) - Bottom Right
	// wihout filled it looks like white bordered recatngle inside red circle 
	line(img, Point(130, 296), Point(382, 296), Scalar(255, 255, 255), 2);
	// starting point, ending point
	// 2 - thickness
	// white horizontal line under rectangle

	putText(img, "Hello World!", Point(137, 262), FONT_HERSHEY_DUPLEX, 0.75, Scalar(0, 69, 255), 2);
	// 0.75 - scale. If it was a large value like 2 text wouldn't have fitted on window.
	// Random Font selected.
	// orange colour.
	// 2- thickness of text

	imshow("Image", img);
	waitKey(0);
}
