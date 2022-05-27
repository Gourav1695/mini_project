#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;

///////////////  Basic Functions  //////////////////////
/*
* Filter Images and Videos:
        Homogeneous Blur
		Gaussian Blur
		Invert Images and Videos
 Morphological Operations:
		Erode Images and Videos
		Dilate Images and Videos
*/

void main() {

	string path = "Resources/test.png";
	Mat img = imread(path);
	Mat imgGray, imgBlur, imgCanny, imgDil, imgErode;

	cvtColor(img, imgGray, COLOR_BGR2GRAY); // First Source Image, then Destination Image
	GaussianBlur(imgGray, imgBlur, Size(7, 7), 7, 0); // more increase in 2nd last value - more blur
	Canny(imgBlur, imgCanny, 25, 75); // edge detector - standard practice to blur image before
									  // Lesser the Last 2 values - more the edges

	// Detected edges are not often completely filled or not joined,
	// or very thin to actually detect properly.
	// Therefore, dilate - increase thickness
	//            erode - decrease thickness

	Mat kernel = getStructuringElement(MORPH_RECT, Size(3, 3)); // Size increase - dilate more
	                                                            // use only odd no.s like (3,3),(5,5),(7,7)... and so on.
	dilate(imgCanny, imgDil, kernel);
	erode(imgDil, imgErode, kernel);

	imshow("Image", img);
	imshow("Image Gray", imgGray);
	imshow("Image Blur", imgBlur);
	imshow("Image Canny", imgCanny);
	imshow("Image Dilation", imgDil);
	imshow("Image Erode", imgErode);
	waitKey(0);
}