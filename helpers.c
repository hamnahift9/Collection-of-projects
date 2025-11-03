// Done as a part of Cs50x

#include <math.h>
#include <stdio.h>
#include <cs50.h>
#include "helpers.h"

//Prototypes
int get_average(int r, int g, int b);
void swap(RGBTRIPLE *a, RGBTRIPLE *b);
RGBTRIPLE blurs_pixel(int h, int w, int height, int width, RGBTRIPLE image[height][width]);
bool is_valid_pixel(int i, int j, int height, int weight);
RGBTRIPLE edged_pixel(int h, int w, int height, int width, RGBTRIPLE image[height][width]);


// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //Iterates over rows
    for (int i = 0 ; i < height ; i++)
    {
        //Iterates over pixels in ith row
        for (int j = 0 ; j < width ; j++)
        {
            //Gets average of RGB
            int average = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

            //Changes all values of RGB to average
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //Iterates over rows
    for (int i = 0 ; i < height ; i++)
    {
        for (int j = 0 ; j < width / 2 ; j++)
        {
            //Swaps pixel at jth position with pixel at the horizontally opposite end
            swap(&image[i][j], &image[i][width - 1 - j]);
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE blurred_image[height][width];
    //iterates over rows
    for (int i = 0 ; i < height ; i++)
    {
        //iterates over pixels in ith row
        for (int j = 0 ; j < width ; j++)
        {
            //puts blurred pixels of image at i j into a copy
            blurred_image[i][j] = blurs_pixel(i, j, height, width, image);
        }
    }
    for (int i = 0 ; i < height ; i++)
    {
        for (int j = 0 ; j < width ; j++)
        {
            //copies blurred pixels into the original image
            image[i][j] = blurred_image[i][j];
        }
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE new_image[height][width];
    for (int i = 0 ; i < height ; i++)
    {
        for (int j = 0 ; j < width ; j++)
        {
            //copies edged pixels into new image
            new_image[i][j] = edged_pixel(i, j, height, width, image);
        }
    }

    for (int i = 0 ; i < height ; i++)
    {
        for (int j = 0 ; j < width ; j++)
        {
            //copies new image into image
            image[i][j] = new_image[i][j];
        }
    }
}

//Other functions

//Swaps two pixels
void swap(RGBTRIPLE *a, RGBTRIPLE *b)
{
    //Stores value at 'a' to a temp variable
    RGBTRIPLE tmp = *a;

    //Changes value of 'a' to value of 'b'
    *a = *b;

    //Changes value of 'b' to value of 'temp'
    *b = tmp;
}


//Blurs pixels
RGBTRIPLE blurs_pixel(int h, int w, int height, int width, RGBTRIPLE image[height][width])
{
    //Stores values of R,G,B
    int count_red = 0;
    int count_green = 0;
    int count_blue = 0;


    //Stores number of pixels surrounding the pixel
    int pixel_count = 0;

    //Iterates over rows starting from the row before h
    for (int i = h - 1 ; i <= h + 1 ; i++)
    {
        //Iterates over pixels in ith row starting from the pixel before w
        for (int j = w - 1 ; j <= w + 1 ; j++)
        {
            //Checks if the pixel at i j exists or not
            if (is_valid_pixel(i, j, height, width))
            {
                //Updates pixel count
                pixel_count ++;

                //Updates values of R,G,B
                count_red += image[i][j].rgbtRed;
                count_green += image[i][j].rgbtGreen;
                count_blue += image[i][j].rgbtBlue;
            }
        }
    }
    RGBTRIPLE new_pixel;
    //Puts average values of R,G,B into the new pixel
    new_pixel.rgbtRed = round((float)count_red / pixel_count);
    new_pixel.rgbtGreen = round((float)count_green / pixel_count);
    new_pixel.rgbtBlue = round((float)count_blue / pixel_count);
    return new_pixel;
}

//Checks if pixel at given position exists
bool is_valid_pixel(int i, int j, int height, int weight)
{
    if (i >= 0 && i < height && j >= 0 && j < weight)
    {
        return true;
    }
    else
    {
        return false;
    }
}

//Checks if value of i is greater than i
int is_capped(int i)
{
    if (i <= 255)
    {
        return i;
    }
    else
    {
        return 255;
    }
}

//Creates new edged pixel
RGBTRIPLE edged_pixel(int h, int w, int height, int width, RGBTRIPLE image[height][width])
{
    //Gx and Gy matrix
    int Xmatrix_values [3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Ymatrix_values [3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    //Initialization of rgb values for x and y
    int Xred_value = 0, Xgreen_value = 0, Xblue_value = 0, Yred_value = 0, Ygreen_value = 0, Yblue_value = 0;

    for (int i = -1 ; i <= 1 ; i++)
    {
        for (int j = -1 ; j <= 1 ; j++)
        {
            int nh = h + i;
            int nw = w + j;
            if (is_valid_pixel(nh, nw, height, width))
            {
                //Adds values of r,g,b multiplied by the gx matrix at their position to the total of r,g,b values of x
                int gx_value = Xmatrix_values[i + 1][j + 1];
                Xred_value += gx_value * image[nh][nw].rgbtRed;
                Xgreen_value += gx_value * image[nh][nw].rgbtGreen;
                Xblue_value += gx_value * image[nh][nw].rgbtBlue;

                //Adds values of r,g,b multiplied by the gy matrix at their position to the total of r,g,b values of y
                int gy_value = Ymatrix_values[i + 1][j + 1];
                Yred_value += gy_value * image[nh][nw].rgbtRed;
                Ygreen_value += gy_value * image[nh][nw].rgbtGreen;
                Yblue_value += gy_value * image[nh][nw].rgbtBlue;
            }
        }
    }
    RGBTRIPLE new_pixel;

    //Assigns new rgb values to the pixel
    new_pixel.rgbtRed = is_capped(round(sqrt(Xred_value * Xred_value + Yred_value * Yred_value)));
    new_pixel.rgbtGreen = is_capped(round(sqrt(Xgreen_value * Xgreen_value + Ygreen_value * Ygreen_value)));
    new_pixel.rgbtBlue = is_capped(round(sqrt(Xblue_value * Xblue_value + Yblue_value * Yblue_value)));

    return new_pixel;
}

