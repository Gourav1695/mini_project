#include <opencv2/opencv.hpp>

#include <iostream>

using namespace cv;
using namespace std;

///////////////  Video  //////////////////////

// All we have to do is to extract frames (images) from the video file and show it in a continuous loop.

// More Details : 

/* How to play a video file:
First, a VideoCapture object should be constructed by passing a valid location to a video file. 
Then the VideoCapture object should be read frame by frame. 
Finally those frames should be displayed in a window sequentially.
*/
void main() {

	string path = "Resources/test_video.mp4";

	//1. First, a VideoCapture object should be constructed by passing a valid location to a video file.

	VideoCapture cap(path);/*The destructor of this class will de-allocate any associated memory with the opened video file. 
						   Therefore you don't need to de-allocate memory explicitly in your program.*/

	//It is essential to check whether the VideoCapture object is initialized successfully before playing the video to avoid a possible crash.
	if (cap.isOpened() == false)
	{
		cout << "Cannot open the video file" << endl;
		cin.get(); //wait for any key press
		return ;
	}

	Mat img;

	while (true) 
	{
		// 2. Then the VideoCapture object should be read frame by frame.
		cap.read(img);

		// 3. Finally those frames should be displayed in a window sequentially.
		imshow("Image", img);
		waitKey(1); // OR //wait for for 10 ms until any key is pressed.  
                          //If the 'Esc' key is pressed, break the while loop.
                          //If the any other key is pressed, continue the loop 
                          //If any key is not pressed withing 10 ms, continue the loop 
		                  /*if (waitKey(10) == 27)
		                  {
			                   cout << "Esc key is pressed by user. Stoppig the video" << endl;
			                   break;
						  }*/
	}
}
