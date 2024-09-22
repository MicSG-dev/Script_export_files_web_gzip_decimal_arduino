# Script export files web gzip decimal Arduino
Repository of a Python Script to export WEB project to Gzip encoded in decimal array.

- [How to Use - Command Line (CMD)](#how-to-use---command-line-cmd)
  - Practical Example of Use in CMD
- How to Use - Bootstrap Studio
- Settings
  - Default Configuration
  - Customizing the Export Path
- Understanding the Exported File
  - Example of Export
- Using the Exported File
- Note
- Benefits of Gzip in the Project

## How to Use - Command Line (CMD)
1. Download the executable from [Releases](github.com/MicSG-dev/Script_export_files_web_gzip_decimal_arduino/releases);
2. Open the Windows Command Prompt (cmd):
   - press the shortcut `Win + R`;
   - type  `cmd` in the Run box;
   - press the `Enter` key;
3. Navigate to the directory where the executable was downloaded:
   - in cmd, navigate to the drive where the directory of the downloaded executable is located, replacing `drive_letter` with the corresponding drive letter:
   ```
   <drive_letter>:
   ```
   - in cmd, to access the directory where the executable is located, use the `cd` command, replacing `path_to_executable_directory ` with the path to the directory of the downloaded executable:
   ```
   cd <path_to_executable_directory >
   ```
4. Execute the following command to perform the export, replacing `path_project_web` with the path to your web project directory:
   ```
   export_files_gzip_decimal_arduino.exe <path_project_web>
   ```
   
### Practical Example of Use in CMD

- Step 3:
```
G:
```

- Step 4:
```
cd G:\Downloads
```

- Step 5:
```
export_files_gzip_decimal_arduino.exe C:\Users\micsg-dev\Desktop\test
```

## How to Use - Bootstrap Studio
1. Download the executable from [Releases](github.com/MicSG-dev/Script_export_files_web_gzip_decimal_arduino/releases);
2. Open Bootstrap Studio and access the project settings:

   ![image](https://github.com/user-attachments/assets/2affe83c-0e2d-4713-b9b4-e4ff649bfb34)
4. Go to the **Export** tab: ![image](https://github.com/user-attachments/assets/f2a5446f-9f49-4f7b-a973-b240415374a8)
5. Click on the **Advanced** tab: ![image](https://github.com/user-attachments/assets/6d3c6a1c-9723-4523-b90b-076c5932f51c)
6. In **Export Script**, enter the path to the directory of the downloaded executable: ![image](https://github.com/user-attachments/assets/88fc10c3-b8e7-488a-834c-636c636d3edd)
6.Now just click on **Export** to perform the exports.![image](https://github.com/user-attachments/assets/6e8e841f-c864-4281-ba67-276b9eceb3ab)

## Settings
When performing the first export, the file `___config_export.txt`. will be created. This file allows you to change the destination of the export.

### Default Configuration:
On the first run, the file will contain the following:
```
PATH_ARDUINO_INCLUDE_FOLDER=

```
The default export location is within the `data` folder (automatically created by the executable) located in your web project directory. 

### Customizing the Export Path:
If you want to change the export location, simply add the path of the new location in front of the `PATH_ARDUINO_INCLUDE_FOLDER` parameter. Example of use:
```
PATH_ARDUINO_INCLUDE_FOLDER=G:\Documentos\PlatformIO\Projects\HelloWorld\include

```

## Understanding the Exported File
The export generates the file `web_gzip.h`, which organizes the content in namespaces to maintain the structure of the web project files. Each file is exported with two variables:
- `size`: stores the size of the `content` array;
- `content`: the array containing the Gzip decimals of the file.

### Example of Export:
If the web project contains the files:
- /assets/js/script.min.js
- /my-folder/index.html
- /index.html
- /other.html

The file `web_gzip.h` will be generated with the following structure:
```
#ifndef WEB_GZIP_h
#define WEB_GZIP_h

#include "Arduino.h"

namespace web_gzip
{
	namespace _INDEX_HTML
	{
		const uint32_t size = 382;
		const uint8_t content[] PROGMEM = {
			31, 139, 8, 0, 94, 99, 239, 102, 2, 255, 165, 82, 77, 75, 196, 48, 16, 253, 43, 49, 231, 109, 227, 34, 130, 72, 91, 68, 93, 60, 137, 194, 42, 226, 169, 164, 201, 180, 153, 53, 77, 74, 50, 187, 235, 250, 235, 77, 91, 193, 15, 60, 233, 37, 97, 38, 239, 189, 201, 123, 73, 113, 116, 125, 119, 245, 240, 124, 191, 98, 134, 122, 91, 21, 227, 202, 180, 36, 153, 53, 49, 35, 3, 61, 148, 220, 98, 103, 136, 51, 43, 93, 87, 114, 112, 60, 161, 64, 234, 170, 232, 129, 36, 83, 70, 134, 8, 84, 242, 45, 181, 217, 25, 255, 232, 58, 57, 18, 119, 8, 251, 193, 135, 196, 85, 222, 17, 184, 132, 218, 163, 38, 83, 106, 216, 161, 130, 108, 42, 22, 12, 29, 18, 74, 155, 69, 37, 45, 148, 203, 252, 120, 193, 162, 9, 232, 94, 50, 242, 89, 139, 84, 58, 159, 116, 9, 201, 66, 245, 232, 166, 93, 23, 98, 174, 11, 155, 112, 44, 128, 45, 121, 164, 131, 133, 104, 0, 210, 60, 19, 160, 45, 185, 33, 26, 226, 185, 16, 74, 187, 124, 19, 53, 88, 220, 133, 220, 1, 9, 55, 244, 162, 241, 158, 34, 5, 57, 92, 156, 230, 39, 249, 137, 208, 24, 73, 168, 24, 63, 15, 242, 30, 93, 158, 58, 105, 184, 152, 29, 55, 94, 31, 146, 251, 101, 245, 180, 186, 100, 247, 193, 111, 64, 17, 91, 189, 142, 30, 33, 36, 31, 236, 230, 13, 7, 166, 65, 97, 47, 109, 34, 45, 171, 66, 254, 184, 75, 135, 100, 182, 77, 174, 124, 47, 110, 81, 173, 111, 178, 148, 133, 88, 171, 128, 3, 213, 48, 41, 213, 45, 38, 31, 245, 30, 154, 186, 75, 114, 245, 135, 92, 45, 131, 222, 162, 243, 130, 51, 146, 161, 27, 35, 175, 155, 244, 38, 47, 188, 250, 183, 102, 33, 100, 85, 196, 137, 192, 98, 80, 127, 73, 110, 243, 53, 184, 102, 235, 180, 133, 41, 191, 205, 20, 223, 172, 253, 125, 134, 140, 233, 223, 196, 145, 56, 119, 127, 129, 139, 57, 112, 49, 253, 205, 119, 182, 136, 93, 141, 171, 2, 0, 0, 
		};
	}

	namespace _OTHER_HTML
	{
		const uint32_t size = 330;
		const uint8_t content[] PROGMEM = {
			31, 139, 8, 0, 94, 99, 239, 102, 2, 255, 157, 82, 193, 78, 3, 33, 16, 253, 21, 228, 220, 93, 108, 26, 19, 99, 216, 141, 81, 27, 143, 237, 65, 99, 60, 178, 48, 45, 172, 44, 16, 102, 218, 90, 191, 94, 118, 215, 68, 77, 60, 121, 129, 204, 227, 189, 153, 247, 0, 121, 241, 176, 185, 127, 122, 221, 174, 153, 165, 193, 183, 114, 92, 153, 81, 164, 170, 14, 43, 178, 48, 64, 195, 189, 219, 91, 226, 204, 171, 176, 111, 56, 4, 94, 88, 160, 76, 43, 7, 32, 197, 180, 85, 25, 129, 26, 126, 160, 93, 117, 205, 191, 208, 160, 70, 225, 209, 193, 41, 197, 92, 180, 58, 6, 130, 80, 88, 39, 103, 200, 54, 6, 142, 78, 67, 53, 21, 11, 230, 130, 35, 167, 124, 133, 90, 121, 104, 150, 245, 229, 130, 161, 205, 46, 188, 85, 20, 171, 157, 163, 38, 196, 210, 151, 28, 121, 104, 159, 195, 180, 27, 41, 230, 90, 250, 194, 99, 25, 124, 195, 145, 206, 30, 208, 2, 148, 121, 54, 195, 174, 225, 150, 40, 225, 141, 16, 218, 132, 186, 71, 3, 222, 29, 115, 29, 128, 68, 72, 131, 232, 98, 36, 164, 172, 210, 237, 85, 189, 170, 87, 194, 56, 36, 161, 17, 191, 15, 234, 193, 133, 186, 32, 101, 184, 152, 19, 119, 209, 156, 75, 250, 101, 251, 178, 190, 99, 219, 28, 123, 208, 196, 214, 239, 99, 70, 200, 37, 7, 123, 252, 112, 137, 25, 208, 110, 80, 190, 136, 150, 173, 76, 237, 166, 92, 99, 102, 91, 181, 7, 41, 82, 43, 81, 103, 151, 136, 97, 214, 255, 49, 216, 255, 244, 215, 29, 130, 241, 48, 217, 236, 39, 151, 115, 239, 223, 51, 20, 150, 231, 193, 81, 56, 163, 127, 208, 197, 156, 75, 76, 95, 224, 19, 176, 185, 101, 37, 18, 2, 0, 0, 
		};
	}

	namespace _ASSETS_JS_SCRIPT_MIN_JS
	{
		const uint32_t size = 105;
		const uint8_t content[] PROGMEM = {
			31, 139, 8, 0, 94, 99, 239, 102, 2, 255, 5, 193, 49, 10, 128, 48, 12, 0, 192, 175, 132, 78, 45, 136, 31, 16, 29, 132, 226, 226, 224, 230, 92, 76, 134, 72, 109, 75, 12, 86, 20, 255, 238, 93, 229, 132, 185, 182, 1, 209, 95, 148, 116, 230, 83, 41, 145, 88, 19, 115, 64, 211, 88, 235, 250, 225, 13, 145, 68, 173, 89, 253, 8, 139, 228, 157, 54, 5, 127, 151, 44, 74, 2, 156, 96, 122, 184, 0, 210, 198, 71, 136, 198, 125, 206, 117, 63, 28, 19, 142, 204, 86, 0, 0, 0, 
		};
	}

	namespace _MY_FOLDER_INDEX_HTML
	{
		const uint32_t size = 330;
		const uint8_t content[] PROGMEM = {
			31, 139, 8, 0, 94, 99, 239, 102, 2, 255, 157, 82, 193, 78, 3, 33, 16, 253, 21, 202, 185, 11, 54, 141, 137, 49, 176, 49, 106, 163, 55, 123, 208, 24, 143, 44, 76, 11, 43, 11, 4, 166, 173, 250, 245, 178, 187, 38, 106, 226, 201, 11, 100, 102, 222, 155, 247, 94, 64, 44, 110, 31, 110, 30, 95, 182, 27, 98, 113, 240, 173, 24, 79, 98, 20, 170, 166, 43, 13, 90, 24, 64, 82, 239, 246, 22, 41, 241, 42, 236, 37, 133, 64, 43, 10, 148, 105, 197, 0, 168, 136, 182, 42, 23, 64, 73, 15, 184, 107, 46, 232, 87, 55, 168, 145, 120, 116, 112, 74, 49, 87, 174, 142, 1, 33, 84, 212, 201, 25, 180, 210, 192, 209, 105, 104, 166, 98, 73, 92, 112, 232, 148, 111, 138, 86, 30, 228, 138, 157, 45, 73, 177, 217, 133, 215, 6, 99, 179, 115, 40, 67, 172, 123, 209, 161, 135, 246, 41, 76, 183, 17, 124, 174, 133, 175, 56, 146, 193, 75, 90, 240, 221, 67, 177, 0, 85, 207, 102, 216, 73, 106, 17, 83, 185, 228, 92, 155, 192, 250, 98, 192, 187, 99, 102, 1, 144, 135, 52, 240, 46, 70, 44, 152, 85, 186, 58, 103, 107, 182, 230, 198, 21, 228, 186, 148, 239, 1, 27, 92, 96, 181, 83, 197, 249, 156, 184, 139, 230, 189, 166, 95, 181, 207, 155, 107, 178, 205, 177, 7, 141, 100, 243, 54, 102, 132, 92, 115, 144, 187, 15, 151, 136, 1, 237, 6, 229, 43, 105, 213, 138, 212, 222, 131, 247, 113, 177, 16, 60, 181, 162, 232, 236, 18, 146, 146, 245, 127, 220, 245, 63, 205, 117, 135, 96, 60, 76, 30, 251, 201, 226, 188, 251, 183, 6, 99, 92, 149, 250, 60, 101, 228, 206, 131, 63, 24, 124, 206, 197, 167, 47, 240, 9, 141, 234, 83, 232, 18, 2, 0, 0, 
		};
	}
}

#endif
```
## Using the Exported File
After generating the `web_gzip.h` file, usage in the Arduino environment is quite straightforward:
1. Include the exported file in your project using: `#include "web_gzip.h"`;
2. Include the necessary libraries for the web server (refer to the example [simple_server.ino](https://github.com/me-no-dev/ESPAsyncWebServer/blob/master/examples/simple_server/simple_server.ino) from the ESPAsyncWebServer library using the ESP32 board);
3. Set up the page on the server in `void setup`:
   ```
   server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    AsyncWebServerResponse *response = request->beginResponse_P(200, "text/html", web_gzip::_INDEX_HTML::content, web_gzip::_INDEX_HTML::size);
    response->addHeader("Content-Encoding","gzip");
    request->send(response);
   });
   ```
4. When the web page is accessed, the server will send the compressed content, which will be decompressed and displayed correctly in the browser.

## Note
Always remember to keep the files of your web project updated, as all files within the project directory will be used for Gzip decimal export.

## Benefits of Gzip in the Project
Using Gzip in your project brings several advantages, such as:
- **Reduced loading time**: Compressed files take up less space, resulting in faster transfers and saving bandwidth.
- **Improved overall performance**: For embedded devices with limited capacity, using Gzip allows for more efficient use of memory and flash storage.
- **Compatibility with modern browsers**: All modern browsers support automatic decompression of Gzip content, making implementation transparent to the end user.
- **Simplified OTA updates**: In an OTA (Over-the-Air) update, it is not necessary to send both the firmware and the filesystem, as web files are already embedded and compressed within the firmware. This reduces the total size of the update and streamlines the sending process, making it more efficient and faster.
- **Ease of distribution**: Keeping web files as part of the source code simplifies project distribution and maintenance, as well as streamlining the deployment process, since all critical system parts are centralized.
