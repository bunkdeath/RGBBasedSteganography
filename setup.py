from distutils.core import setup

setup(
    name="RGBBasedSteganography",
    version="0.1.0",
    author="Amrit Kshetri - bunkdeath",
    author_email="kshetriamrit@gmail.com",
    py_modules=['RGBBasedSteganography'],
    # app=["RGBBasedSteganography"],
    description="Hide message on RGB value of image",
    long_description=open("README").read(),
    install_requires=[]
)
