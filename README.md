# Using the Webflow CDN for large amount of images

**Challenge:**

-   Dynamically generating url paths to Webflow CDN
-   Difficult to use webflow CDN due image names are given a dynamically generated identifier in the upload phase

**Solution:**

-   Using GitHub as a CDN for images in Webflow
-   Generating a python script
-   Script outputs a list of DNS url's with a list filenames in GitHub

**Step-by-step**

-   Upload images to GitHub
-   Use terminal ls command to get all image names as strings
-   Paste list of strings to script
-   Script adds image name in correct format to GitHub raw url
-   Copy output list of CDN urls
-   Paste list to CSV containing all entries to Webflow collection
-   Upload CSV to Webflow and enjoy a large set of collections with images

![Example Process](https://raw.githubusercontent.com/alluster/cdn-image-url/master/image-naming-problem-webflow.jpg)
