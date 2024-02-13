# This is the development branch for all the coding and testing, anything officially submitted will be in [production branch](https://github.com/Kamikamer/capstone/tree/main), we are in [development branch](https://github.com/Kamikamer/capstone/tree/development)
# capstone

# Home page


# Run the code
python src/lala.ipynb -o jupyter-server -p 4331 -u http://localhost:4331/lala.ipynb

Run python file in X package

``python -m package.X``

E.g. python -m posture_fit_development.Webcam
E.g. python -m posture_fit_algorithm.Detector

# Common error
If you installed the libraries manually and you are facing error with the sound system such as ![The driver cannot recognize the spececified command parameter.](/assets/driver_error_sp.png)<br>
Reinstall playsound (lib) with version 1.2.2<br>
`pip uninstall playsound -y; pip install playsound==1.2.2` <br>
`pip uninstall playsound -y && pip install playsound==1.2.2`

If you face errors with icecream, you might need to install it with 
`pip install icecream` instead of `conda install icecream`
