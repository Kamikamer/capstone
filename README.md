# This is the production branch. This is the ready to submit code to submit. No working code will be here.

# capstone

## Home page

## Run the code

python src/lala.ipynb -o jupyter-server -p 4331 -u http://localhost:4331/lala.ipynb

Run python file in X package

``python -m package.X``

E.g. python -m posture_fit_development.Webcam
E.g. python -m posture_fit_algorithm.Detector

# Common error

If you installed the libraries manually and you are facing error with the sound system such as ![The driver cannot recognize the spececified command parameter.](/assets/driver_error_sp.png)<br>
Reinstall playsound (lib) with version 1.2.2  
`pip uninstall playsound -y; pip install playsound==1.2.2`  
`pip uninstall playsound -y && pip install playsound==1.2.2`

If you face errors with icecream, you might need to install it with  
`pip install icecream` instead of `conda install icecream`

pyupdater build --app-version v1.0.0 --console --name "PostureFit" --log-level "ERROR" --add-data "C:/Users/Ivene/miniconda3/envs/capstone/Lib/site-packages/mediapipe;mediapipe/" --add-data "C:/Users/Ivene/Documents/Github/capstone/posture_fit_algorithm;posture_fit_algorithm/" --add-data "C:/Users/Ivene/Documents/Github/capstone/posture_fit_development;posture_fit_development/" --add-data "C:/Users/Ivene/Documents/Github/capstone/assets;assets/" --hidden-import "playsound" --hidden-import "mediapipe" "./index.py"


