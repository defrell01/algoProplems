//O(nlogn) time O(1) time
// need to place two people group in the back raw or in the front depends on their height
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

bool classPhotos(std::vector<int> redShirtHeights, std::vector<int> blueShirtHeights) 
{
    std::sort(redShirtHeights.begin(), redShirtHeights.end());
    std::sort(blueShirtHeights.begin(), blueShirtHeights.end());

    std::string shirtColorInTheFirstRow = 
        redShirtHeights[0] < blueShirtHeights[0] ? "RED" : "BLUE";

    for (int i = 0; i < redShirtHeights.size(); ++i)
    {
        int redShirtHeight = redShirtHeights[i];
        int blueShirtHeight = blueShirtHeights[i];

        if (shirtColorInTheFirstRow == "RED"){
            if (redShirtHeight >= blueShirtHeight)
                return false;
        }
        else if (blueShirtHeight >= redShirtHeight)
            return false;
    }

    return true;
}

int main()
{
    std::vector<int> redShirtHeight = {5, 8, 1, 3, 4};
    std::vector<int> blueShirtHeight = {6, 9, 2, 4, 5};

    std::cout << classPhotos(redShirtHeight, blueShirtHeight) << std::endl;
}

// just take two vectors and sort them
// decide by the first one guy which vector is the first row
// and depends on that if other one's member is greater than
// first one's member then we return false