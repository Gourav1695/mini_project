#include<opencv2/imgcodecs.hpp>
#include<opencv2/highgui.hpp>
#include<opencv2/imgproc.hpp>
#include<iostream>

using namespace cv;
using namespace std;

// Images

void main()
{
	// Importing Images

	string path = "Resources/test.png";
	//Mat - matrix datatype to handle images
	Mat img = imread(path); // reads image from paths
	imshow("ArabicMan", img);
	/* If you try to execute this code the output window flickers just once.To
	   appreciate the output we need : waitKey(number);

	   -If 0 or negative number is given as input: - Waits indefinitely till key
	   press and returns the ASCII value of the key pressed.

	   -If positive number is given as input: - Waits for corresponding milliseconds.

	*/
	waitKey(0);

}
