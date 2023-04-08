#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// Number of bytes in a block
const int BLOCK_SIZE = 512;
typedef uint8_t BYTE;
char filename[8];

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        printf("Usage: $ ./recover infile\n");
        return 1;
    }

    //Open memory card as input file
    FILE *infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    // Create buffer to read into
    BYTE buffer[BLOCK_SIZE];

    //Repeat until end of card
    int i = 0;
    FILE *img = fopen("000.jpg", "w");
    while (fread(buffer, 1, BLOCK_SIZE, infile) == BLOCK_SIZE)
    {
        //Read 512 bytes into a buffer
        //If start of new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //If first JPEG
            if (img == NULL)
            {
                fwrite(&buffer, BLOCK_SIZE, 1, img);
                i++;
            }
            //Else
            else
            {
                fclose(img);
                sprintf(filename, "%03i.jpg", i);
                img = fopen(filename, "w");
                fwrite(&buffer, BLOCK_SIZE, 1, img);
                i++;
            }
        }
        //Else
        else
        {
            //If already found JPEG
            if (img != NULL)
            {
                fwrite(&buffer, BLOCK_SIZE, 1, img);
            }
        }
    }
    //Close any remaining files
    fclose(infile);
    fclose(img);
}