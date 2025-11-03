// Done as part of Cs50x

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Checks if there is 1 command line argument
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    // Opens file
    FILE *image = fopen(argv[1], "r");
    // Checks if file is empty
    if (image == NULL)
    {
        printf("There was an error opening the file\n");
        return 1;
    }
    BYTE buffer[512];
    int count = 0;
    FILE *pointer = NULL;
    char filename[8];

    // Iterates through the end until the end
    while (fread(&buffer, 512, 1, image) == 1)
    {
        // Checks for the start of a new jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (!(count == 0))
            {
                fclose(pointer);
            }
            // Initialises file
            sprintf(filename, "%03i.jpg", count);
            pointer = fopen(filename, "w");
            count++;
        }
        if (!(count == 0))
        {
            fwrite(&buffer, 512, 1, pointer);
        }
    }
    fclose(image);
    fclose(pointer);
    return 0;
}