#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;


///////////////  Resize and Crop //////////////////////

//void main() {
//
//	string path = "Resources/test.png";
//	Mat img = imread(path);
//	Mat imgResize, imgCrop;
//
//	//cout << img.size() << endl;  // O/P: [768 * 559]
//	 
//	// resize(img, imgResize, Size(640,480)); // format used when we have particular specifications in mind
//	                                          // For our e.g. image, aspect ratio will have reduced ... - sqeueezed a little bit on the width.
//
//	resize(img, imgResize, Size(), 0.5, 0.5); // when we just want to scale it down and have no particular numbers in mind 
//
//	Rect roi(200, 100, 300, 250); // (x,y,height,width)
//								  // (x,y) = Top left corner
//	                              //  From (100,100) we go 300 pixel forwards & 250 downwards.
//	                              // add extra 50 downwards for full face.
//	imgCrop = img(roi);
//
//	imshow("Image", img);
//	imshow("Image Resize", imgResize);
//	imshow("Image Crop", imgCrop);
//	waitKey(0);
//}
