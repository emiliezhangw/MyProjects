#include "helpers.h"
#include <math.h>
#include <stdio.h>

int valid_color(int gx, int gy);
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gray = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtBlue = gray;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE image_reflect[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image_reflect[i][width - 1 - j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = image_reflect[i][j];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (j > 0 && j < width - 1 && i > 0 && i < height - 1)
            {
                image[i][j].rgbtRed = round((copy[i - 1][j - 1].rgbtRed + copy[i - 1][j].rgbtRed + copy[i - 1][j + 1].rgbtRed + copy[i][j -
                                             1].rgbtRed + copy[i][j].rgbtRed + copy[i][j + 1].rgbtRed + copy[i + 1][j - 1].rgbtRed + copy[i + 1][j].rgbtRed + copy[i + 1][j +
                                                     1].rgbtRed) / 9.0);
                image[i][j].rgbtGreen = round((copy[i - 1][j - 1].rgbtGreen + copy[i - 1][j].rgbtGreen + copy[i - 1][j + 1].rgbtGreen + copy[i][j -
                                               1].rgbtGreen + copy[i][j].rgbtGreen + copy[i][j + 1].rgbtGreen + copy[i + 1][j - 1].rgbtGreen + copy[i + 1][j].rgbtGreen + copy[i +
                                                       1][j + 1].rgbtGreen) / 9.0);
                image[i][j].rgbtBlue = round((copy[i - 1][j - 1].rgbtBlue + copy[i - 1][j].rgbtBlue + copy[i - 1][j + 1].rgbtBlue + copy[i][j -
                                              1].rgbtBlue + copy[i][j].rgbtBlue + copy[i][j + 1].rgbtBlue + copy[i + 1][j - 1].rgbtBlue + copy[i + 1][j].rgbtBlue + copy[i + 1][j
                                                      + 1].rgbtBlue) / 9.0);
            }
            else if (i == 0 && j == 0)
            {
                image[i][j].rgbtRed = round((copy[i][j].rgbtRed + copy[i][j + 1].rgbtRed + copy[i + 1][j].rgbtRed + copy[i + 1][j + 1].rgbtRed) /
                                            4.0);
                image[i][j].rgbtGreen = round((copy[i][j].rgbtGreen + copy[i][j + 1].rgbtGreen + copy[i + 1][j].rgbtGreen + copy[i + 1][j +
                                               1].rgbtGreen) / 4.0);
                image[i][j].rgbtBlue = round((copy[i][j].rgbtBlue + copy[i][j + 1].rgbtBlue + copy[i + 1][j].rgbtBlue + copy[i + 1][j +
                                              1].rgbtBlue) / 4.0);
            }
            else if (i == height - 1 && j == 0)
            {
                image[i][j].rgbtRed = round((copy[i - 1][j].rgbtRed + copy[i - 1][j + 1].rgbtRed + copy[i][j].rgbtRed + copy[i][j + 1].rgbtRed) /
                                            4.0);
                image[i][j].rgbtGreen = round((copy[i - 1][j].rgbtGreen + copy[i - 1][j + 1].rgbtGreen + copy[i][j].rgbtGreen + copy[i][j +
                                               1].rgbtGreen) / 4.0);
                image[i][j].rgbtBlue = round((copy[i - 1][j].rgbtBlue + copy[i - 1][j + 1].rgbtBlue + copy[i][j].rgbtBlue + copy[i][j +
                                              1].rgbtBlue) / 4.0);
            }
            else if (i == 0 && j == width - 1)
            {
                image[i][j].rgbtRed = round((copy[i][j - 1].rgbtRed + copy[i][j].rgbtRed + copy[i + 1][j - 1].rgbtRed + copy[i + 1][j].rgbtRed) /
                                            4.0);
                image[i][j].rgbtGreen = round((copy[i][j - 1].rgbtGreen + copy[i][j].rgbtGreen + copy[i + 1][j - 1].rgbtGreen + copy[i +
                                               1][j].rgbtGreen) / 4.0);
                image[i][j].rgbtBlue = round((copy[i][j - 1].rgbtBlue + copy[i][j].rgbtBlue + copy[i + 1][j - 1].rgbtBlue + copy[i +
                                              1][j].rgbtBlue) / 4.0);
            }
            else if (i == height - 1 && j == width - 1)
            {
                image[i][j].rgbtRed = round((copy[i - 1][j - 1].rgbtRed + copy[i - 1][j].rgbtRed + copy[i][j - 1].rgbtRed + copy[i][j].rgbtRed) /
                                            4.0);
                image[i][j].rgbtGreen = round((copy[i - 1][j - 1].rgbtGreen + copy[i - 1][j].rgbtGreen + copy[i][j - 1].rgbtGreen +
                                               copy[i][j].rgbtGreen) / 4.0);
                image[i][j].rgbtBlue = round((copy[i - 1][j - 1].rgbtBlue + copy[i - 1][j].rgbtBlue + copy[i][j - 1].rgbtBlue +
                                              copy[i][j].rgbtBlue) / 4.0);
            }
            else if (i  == 0 && j > 0 && j < width - 1)
            {
                image[i][j].rgbtRed = round((copy[i][j - 1].rgbtRed + copy[i][j].rgbtRed + copy[i][j + 1].rgbtRed + copy[i + 1][j - 1].rgbtRed +
                                             copy[i + 1][j].rgbtRed + copy[i + 1][j + 1].rgbtRed) / 6.0);
                image[i][j].rgbtGreen = round((copy[i][j - 1].rgbtGreen + copy[i][j].rgbtGreen + copy[i][j + 1].rgbtGreen + copy[i + 1][j -
                                               1].rgbtGreen + copy[i + 1][j].rgbtGreen + copy[i + 1][j + 1].rgbtGreen) / 6.0);
                image[i][j].rgbtBlue = round((copy[i][j - 1].rgbtBlue + copy[i][j].rgbtBlue + copy[i][j + 1].rgbtBlue + copy[i + 1][j - 1].rgbtBlue
                                              + copy[i + 1][j].rgbtBlue + copy[i + 1][j + 1].rgbtBlue) / 6.0);
            }
            else if (i  == height - 1 && j > 0 && j < width - 1)
            {
                image[i][j].rgbtRed = round((copy[i - 1][j - 1].rgbtRed + copy[i - 1][j].rgbtRed + copy[i - 1][j + 1].rgbtRed + copy[i][j -
                                             1].rgbtRed + copy[i][j].rgbtRed + copy[i][j + 1].rgbtRed) / 6.0);
                image[i][j].rgbtGreen = round((copy[i - 1][j - 1].rgbtGreen + copy[i - 1][j].rgbtGreen + copy[i - 1][j + 1].rgbtGreen + copy[i][j -
                                               1].rgbtGreen + copy[i][j].rgbtGreen + copy[i][j + 1].rgbtGreen) / 6.0);
                image[i][j].rgbtBlue = round((copy[i - 1][j - 1].rgbtBlue + copy[i - 1][j].rgbtBlue + copy[i - 1][j + 1].rgbtBlue + copy[i][j -
                                              1].rgbtBlue + copy[i][j].rgbtBlue + copy[i][j + 1].rgbtBlue) / 6.0);
            }
            else if (j  == 0 && i > 0 && i < height - 1)
            {
                image[i][j].rgbtRed = round((copy[i - 1][j].rgbtRed + copy[i - 1][j + 1].rgbtRed + copy[i][j].rgbtRed + copy[i][j + 1].rgbtRed +
                                             copy[i + 1][j].rgbtRed + copy[i + 1][j + 1].rgbtRed) / 6.0);
                image[i][j].rgbtGreen = round((copy[i - 1][j].rgbtGreen + copy[i - 1][j + 1].rgbtGreen + copy[i][j].rgbtGreen + copy[i][j +
                                               1].rgbtGreen + copy[i + 1][j].rgbtGreen + copy[i + 1][j + 1].rgbtGreen) / 6.0);
                image[i][j].rgbtBlue = round((copy[i - 1][j].rgbtBlue + copy[i - 1][j + 1].rgbtBlue + copy[i][j].rgbtBlue + copy[i][j + 1].rgbtBlue
                                              + copy[i + 1][j].rgbtBlue + copy[i + 1][j + 1].rgbtBlue) / 6.0);
            }
            else if (j  == width - 1 && i > 0 && i < height - 1)
            {
                image[i][j].rgbtRed = round((copy[i - 1][j - 1].rgbtRed + copy[i - 1][j].rgbtRed + copy[i][j - 1].rgbtRed + copy[i][j].rgbtRed +
                                             copy[i + 1][j - 1].rgbtRed + copy[i + 1][j].rgbtRed) / 6.0);
                image[i][j].rgbtGreen = round((copy[i - 1][j - 1].rgbtGreen + copy[i - 1][j].rgbtGreen + copy[i][j - 1].rgbtGreen +
                                               copy[i][j].rgbtGreen + copy[i + 1][j - 1].rgbtGreen + copy[i + 1][j].rgbtGreen) / 6.0);
                image[i][j].rgbtBlue = round((copy[i - 1][j - 1].rgbtBlue + copy[i - 1][j].rgbtBlue + copy[i][j - 1].rgbtBlue +  copy[i][j].rgbtBlue
                                              + copy[i + 1][j - 1].rgbtBlue + copy[i + 1][j].rgbtBlue) / 6.0);
            }
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    int gx_red;
    int gy_red;
    int gx_green;
    int gy_green;
    int gx_blue;
    int gy_blue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (j > 0 && j < width - 1 && i > 0 && i < height - 1)
            {
                gx_red = copy[i - 1][j + 1].rgbtRed + 2 * copy[i][j + 1].rgbtRed + copy[i + 1][j + 1].rgbtRed - copy[i - 1][j - 1].rgbtRed - 2 *
                         copy[i][j - 1].rgbtRed - copy[i + 1][j - 1].rgbtRed;
                gy_red = copy[i + 1][j - 1].rgbtRed + 2 * copy[i + 1][j].rgbtRed + copy[i + 1][j + 1].rgbtRed - copy[i - 1][j - 1].rgbtRed - 2 *
                         copy[i - 1][j].rgbtRed - copy[i - 1][j + 1].rgbtRed;
                gx_green = copy[i - 1][j + 1].rgbtGreen + 2 * copy[i][j + 1].rgbtGreen + copy[i + 1][j + 1].rgbtGreen - copy[i - 1][j - 1].rgbtGreen
                           - 2 * copy[i][j - 1].rgbtGreen - copy[i + 1][j - 1].rgbtGreen;
                gy_green = copy[i + 1][j - 1].rgbtGreen + 2 * copy[i + 1][j].rgbtGreen + copy[i + 1][j + 1].rgbtGreen - copy[i - 1][j - 1].rgbtGreen
                           - 2 * copy[i - 1][j].rgbtGreen - copy[i - 1][j + 1].rgbtGreen;
                gx_blue = copy[i - 1][j + 1].rgbtBlue + 2 * copy[i][j + 1].rgbtBlue + copy[i + 1][j + 1].rgbtBlue - copy[i - 1][j - 1].rgbtBlue - 2
                          * copy[i][j - 1].rgbtBlue - copy[i + 1][j - 1].rgbtBlue;
                gy_blue = copy[i + 1][j - 1].rgbtBlue + 2 * copy[i + 1][j].rgbtBlue + copy[i + 1][j + 1].rgbtBlue - copy[i - 1][j - 1].rgbtBlue - 2
                          * copy[i - 1][j].rgbtBlue - copy[i - 1][j + 1].rgbtBlue;
            }
            else if (i == 0 && j == 0)
            {
                gx_red = 2 * copy[i][j + 1].rgbtRed + copy[i + 1][j + 1].rgbtRed;
                gy_red = 2 * copy[i + 1][j].rgbtRed + copy[i + 1][j + 1].rgbtRed;
                gx_green = 2 * copy[i][j + 1].rgbtGreen + copy[i + 1][j + 1].rgbtGreen;
                gy_green = 2 * copy[i + 1][j].rgbtGreen + copy[i + 1][j + 1].rgbtGreen;
                gx_blue = 2 * copy[i][j + 1].rgbtBlue + copy[i + 1][j + 1].rgbtBlue;
                gy_blue = 2 * copy[i + 1][j].rgbtBlue + copy[i + 1][j + 1].rgbtBlue;
            }
            else if (i == height - 1 && j == 0)
            {
                gx_red = copy[i - 1][j + 1].rgbtRed + 2 * copy[i][j + 1].rgbtRed;
                gy_red = -2 * copy[i - 1][j].rgbtRed - copy[i - 1][j + 1].rgbtRed;
                gx_green = copy[i - 1][j + 1].rgbtGreen + 2 * copy[i][j + 1].rgbtGreen;
                gy_green = -2 * copy[i - 1][j].rgbtGreen - copy[i - 1][j + 1].rgbtGreen;
                gx_blue = copy[i - 1][j + 1].rgbtBlue + 2 * copy[i][j + 1].rgbtBlue;
                gy_blue = -2 * copy[i - 1][j].rgbtBlue - copy[i - 1][j + 1].rgbtBlue;
            }
            else if (i == 0 && j == width - 1)
            {
                gx_red = -2 * copy[i][j - 1].rgbtRed - copy[i + 1][j - 1].rgbtRed;
                gy_red = copy[i + 1][j - 1].rgbtRed + 2 * copy[i + 1][j].rgbtRed;
                gx_green = -2 * copy[i][j - 1].rgbtGreen - copy[i + 1][j - 1].rgbtGreen;
                gy_green = copy[i + 1][j - 1].rgbtGreen + 2 * copy[i + 1][j].rgbtGreen;
                gx_blue = -2 * copy[i][j - 1].rgbtBlue - copy[i + 1][j - 1].rgbtBlue;
                gy_blue = copy[i + 1][j - 1].rgbtBlue + 2 * copy[i + 1][j].rgbtBlue;
            }
            else if (i == height - 1 && j == width - 1)
            {
                gx_red = - copy[i - 1][j - 1].rgbtRed - 2 * copy[i][j - 1].rgbtRed;
                gy_red = - copy[i - 1][j - 1].rgbtRed - 2 * copy[i - 1][j].rgbtRed;
                gx_green = - copy[i - 1][j - 1].rgbtGreen - 2 * copy[i][j - 1].rgbtGreen;
                gy_green = - copy[i - 1][j - 1].rgbtGreen - 2 * copy[i - 1][j].rgbtGreen;
                gx_blue = - copy[i - 1][j - 1].rgbtBlue - 2 * copy[i][j - 1].rgbtBlue;
                gy_blue = - copy[i - 1][j - 1].rgbtBlue - 2 * copy[i - 1][j].rgbtBlue;
            }
            else if (i == 0 && j > 0 && j < width - 1)
            {
                gx_red = 2 * copy[i][j + 1].rgbtRed + copy[i + 1][j + 1].rgbtRed - 2 * copy[i][j - 1].rgbtRed - copy[i + 1][j - 1].rgbtRed;
                gy_red = copy[i + 1][j - 1].rgbtRed + 2 * copy[i + 1][j].rgbtRed + copy[i + 1][j + 1].rgbtRed;
                gx_green = 2 * copy[i][j + 1].rgbtGreen + copy[i + 1][j + 1].rgbtGreen - 2 * copy[i][j - 1].rgbtGreen - copy[i + 1][j -
                           1].rgbtGreen;
                gy_green = copy[i + 1][j - 1].rgbtGreen + 2 * copy[i + 1][j].rgbtGreen + copy[i + 1][j + 1].rgbtGreen;
                gx_blue = 2 * copy[i][j + 1].rgbtBlue + copy[i + 1][j + 1].rgbtBlue - 2 * copy[i][j - 1].rgbtBlue - copy[i + 1][j - 1].rgbtBlue;
                gy_blue = copy[i + 1][j - 1].rgbtBlue + 2 * copy[i + 1][j].rgbtBlue + copy[i + 1][j + 1].rgbtBlue;
            }
            else if (i == height - 1 && j > 0 && j < width - 1)
            {
                gx_red = copy[i - 1][j + 1].rgbtRed + 2 * copy[i][j + 1].rgbtRed - copy[i - 1][j - 1].rgbtRed - 2 * copy[i][j - 1].rgbtRed;
                gy_red = - copy[i - 1][j - 1].rgbtRed - 2 * copy[i - 1][j].rgbtRed - copy[i - 1][j + 1].rgbtRed;
                gx_green = copy[i - 1][j + 1].rgbtGreen + 2 * copy[i][j + 1].rgbtGreen - copy[i - 1][j - 1].rgbtGreen - 2 * copy[i][j -
                           1].rgbtGreen;
                gy_green = - copy[i - 1][j - 1].rgbtGreen - 2 * copy[i - 1][j].rgbtGreen - copy[i - 1][j + 1].rgbtGreen;
                gx_blue = copy[i - 1][j + 1].rgbtBlue + 2 * copy[i][j + 1].rgbtBlue - copy[i - 1][j - 1].rgbtBlue - 2 * copy[i][j - 1].rgbtBlue;
                gy_blue = - copy[i - 1][j - 1].rgbtBlue - 2 * copy[i - 1][j].rgbtBlue - copy[i - 1][j + 1].rgbtBlue;
            }
            else if (j == 0 && i > 0 && i < height - 1)
            {
                gx_red = copy[i - 1][j + 1].rgbtRed + 2 * copy[i][j + 1].rgbtRed + copy[i + 1][j + 1].rgbtRed;
                gy_red = 2 * copy[i + 1][j].rgbtRed + copy[i + 1][j + 1].rgbtRed - 2 * copy[i - 1][j].rgbtRed - copy[i - 1][j + 1].rgbtRed;
                gx_green = copy[i - 1][j + 1].rgbtGreen + 2 * copy[i][j + 1].rgbtGreen + copy[i + 1][j + 1].rgbtGreen;
                gy_green = 2 * copy[i + 1][j].rgbtGreen + copy[i + 1][j + 1].rgbtGreen - 2 * copy[i - 1][j].rgbtGreen - copy[i - 1][j +
                           1].rgbtGreen;
                gx_blue = copy[i - 1][j + 1].rgbtBlue + 2 * copy[i][j + 1].rgbtBlue + copy[i + 1][j + 1].rgbtBlue;
                gy_blue = 2 * copy[i + 1][j].rgbtBlue + copy[i + 1][j + 1].rgbtBlue - 2 * copy[i - 1][j].rgbtBlue - copy[i - 1][j + 1].rgbtBlue;
            }
            else if (j == width - 1 && i > 0 && i < height - 1)
            {
                gx_red = - copy[i - 1][j - 1].rgbtRed - 2 * copy[i][j - 1].rgbtRed - copy[i + 1][j - 1].rgbtRed;
                gy_red = copy[i + 1][j - 1].rgbtRed + 2 * copy[i + 1][j].rgbtRed - copy[i - 1][j - 1].rgbtRed - 2 * copy[i - 1][j].rgbtRed;
                gx_green = - copy[i - 1][j - 1].rgbtGreen - 2 * copy[i][j - 1].rgbtGreen - copy[i + 1][j - 1].rgbtGreen;
                gy_green = copy[i + 1][j - 1].rgbtGreen + 2 * copy[i + 1][j].rgbtGreen - copy[i - 1][j - 1].rgbtGreen - 2 * copy[i -
                           1][j].rgbtGreen;
                gx_blue = - copy[i - 1][j - 1].rgbtBlue - 2 * copy[i][j - 1].rgbtBlue - copy[i + 1][j - 1].rgbtBlue;
                gy_blue = copy[i + 1][j - 1].rgbtBlue + 2 * copy[i + 1][j].rgbtBlue - copy[i - 1][j - 1].rgbtBlue - 2 * copy[i - 1][j].rgbtBlue;
            }
            image[i][j].rgbtRed = valid_color(gx_red, gy_red);
            image[i][j].rgbtGreen = valid_color(gx_green, gy_green);
            image[i][j].rgbtBlue = valid_color(gx_blue, gy_blue);
        }
    }
    return;
}

int valid_color(int gx, int gy)
{
    int n = round(sqrt(gx * gx + gy * gy));
    if (n > 255)
    {
        n = 255;
    }
    return n;
}