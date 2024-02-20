# How to build

pyinstaller --noconfirm --onefile --console --name "PostureFit" --log-level "ERROR" --add-data "C:/Users/Ivene/miniconda3/envs/capstone/Lib/site-packages/mediapipe;mediapipe/" --add-data "C:/Users/Ivene/Documents/Github/capstone/posture_fit_algorithm;posture_fit_algorithm/" --add-data "C:/Users/Ivene/Documents/Github/capstone/posture_fit_development;posture_fit_development/" --add-data "C:/Users/Ivene/Documents/Github/capstone/assets;assets/" --hidden-import "playsound" --hidden-import "mediapipe"  "C:/Users/Ivene/Documents/Github/capstone/index.py"

pyinstaller --noconfirm --onefile --console --name "PostureFit" --log-level "ERROR" --add-data "D:/Public/miniconda/envs/capstone/Lib/site-packages/mediapipe;mediapipe/" --add-data "D:/Private/Github/capstone/posture_fit_algorithm;posture_fit_algorithm/" --add-data "D:/Private/Github/capstone/posture_fit_development;posture_fit_development/" --add-data "D:/Private/Github/capstone/assets;assets/" --hidden-import "playsound" --hidden-import "mediapipe"  "D:/Private/Github/capstone/index.py"

pyinstaller --noconfirm --onefile --console --name "PostureFit" --log-level "ERROR" --add-data "D:/Public/miniconda/envs/capstone/Lib/site-packages/mediapipe;mediapipe/" --add-data "D:/Public/miniconda/envs/capstone/Lib/site-packages/icecream;icecream/"  --add-data "D:/Private/Github/capstone/posture_fit_algorithm;posture_fit_algorithm/" --add-data "D:/Private/Github/capstone/posture_fit_development;posture_fit_development/" --add-data "D:/Private/Github/capstone/assets;assets/" --hidden-import "playsound" --hidden-import "mediapipe"  "D:/Private/Github/capstone/index.py"

pyupdater build --app-version v1.0.0 --console --name "PostureFit" --log-level "ERROR" --add-data "C:/Users/Ivene/miniconda3/envs/capstone/Lib/site-packages/mediapipe;mediapipe/" --add-data "C:/Users/Ivene/Documents/Github/capstone/posture_fit_algorithm;posture_fit_algorithm/" --add-data "C:/Users/Ivene/Documents/Github/capstone/posture_fit_development;posture_fit_development/" --add-data "C:/Users/Ivene/Documents/Github/capstone/assets;assets/" --hidden-import "playsound" --hidden-import "mediapipe" "./index.py"

 /d/Apps/gcc/bin/gcc.exe -I/d/Apps/curl-8.6.0/include posture_fit_development/Updater.c  -o posture_fit_development/Updater && ./posture_fit_development/Updater.exe

Kami@DESKTOP-ESPIPOT MINGW64 /d/Private/Github/capstone/build (Auto-Updater)
$ cmake .. -G "MinGW Makefiles" -DCMAKE_MAKE_PROGRAM="/d/Apps/llvm-mingw-20240207-msvcrt-x86_64/bin/mingw32-make.exe" -DCMAKE_C_COMPILER="/d/Apps/gcc/bin/gcc.exe

cmake .. && make && ./Updater

cmake .. && make && ./Updater.exe

cmake .. -G Ninja  -DVCPKG_TARGET_TRIPLET=x64-mingw-dynamic "-DCMAKE_MAKE_PROGRAM=C:/Users/Kami/AppData/Local/Programs/CLion Nova/bin/ninja/win/x64/ninja.exe" -DCMAKE_TOOLCHAIN_FILE=D:\\Private\\Github\\vcpkg\\scripts\\buildsystems\\vcpkg.cmake -B D:\\Private\\Github\\capstone\\cmake-build-debug;
cmake --build ../cmake-build-debug --target Updater -j 10;
D:\\Private\\Github\\capstone\\cmake-build-debug\\Updater.exe;

cmake .. -G Ninja  -DVCPKG_TARGET_TRIPLET=x64-mingw-dynamic "-DCMAKE_MAKE_PROGRAM=C:/Users/Kami/AppData/Local/Programs/CLion Nova/bin/ninja/win/x64/ninja.exe" -DCMAKE_TOOLCHAIN_FILE=D:\\Private\\Github\\vcpkg\\scripts\\buildsystems\\vcpkg.cmake -B D:\\Private\\Github\\capstone\\cmake-build-debug; \
cmake --build ../cmake-build-debug --target Updater -j 10; \
D:\\Private\\Github\\capstone\\cmake-build-debug\\Updater.exe;